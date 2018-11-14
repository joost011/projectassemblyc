
#define F_CPU 16E6
#include <stdio.h>
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define UBBRVAL 51
void init() {
	DDRC = 0xFF;							// Port C all output. PC0: RW		PC1: RS		PC2: E
	DDRC &= ~(1<<DDC5);						// Set Pin C5 as input to read Echo
	PORTC |= (1<<PORTC5);					// Enable pull up on C5
	PORTC &= ~(1<<PC4);						// Init C4 as low (trigger)

	PRR &= ~(1<<PRTIM1);					// To activate timer1 module
	TCNT1 = 0;								// Initial timer value
	TCCR1B |= (1<<CS10);					// Timer without prescaller. Since default clock for atmega328p is 1Mhz period is 1uS
	TCCR1B |= (1<<ICES1);					// First capture on rising edge

	PCICR = (1<<PCIE1);						// Enable PCINT[14:8] we use pin C5 which is PCINT13
	PCMSK1 = (1<<PCINT13);					// Enable C5 interrupt
	sei();									// Enable Global Interrupts
}
void uart_init()
{
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void transmit(uint8_t data)
{
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}
uint8_t receive(void){
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}


int main() {
	uart_init();
	init();
	while (1) {
		_delay_ms(60); 							// To allow sufficient time between queries (60ms min)

		PORTC |= (1<<PC4);						// Set trigger high
		_delay_us(10);							// for 10uS
		PORTC &= ~(1<<PC4);						// to trigger the ultrasonic module
	}
}
ISR(PCINT1_vect) {
	if (bit_is_set(PINC,PC5)) {					// Checks if echo is high
		TCNT1 = 0;								// Reset Timer
		PORTC |= (1<<PC3);
		} else {
		int numuS = TCNT1;					// Save Timer value
		uint8_t oldSREG = SREG;
		cli();									// Disable Global interrupts
		transmit(numuS/58/16);
		_delay_ms(1000);
		SREG = oldSREG;							// Enable interrupts
	}
}