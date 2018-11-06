#include "AVR_TTC_scheduler.h"

#include <avr/io.h>
#include <stdint.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <avr/interrupt.h>
#include <avr/sfr_defs.h>
	
#define UBBRVAL 51

#define LTH 200 //light threshold high
#define LTL 160 //light threshold Low
#define HTH 24	//Heat threshold high
#define HTL 20	//Heat threshold low

#define HIGH 0x01
#define LOW  0x0

// const uint8_t data = 0;
// const uint8_t clock = 1;
// const uint8_t strobe = 2;
// uint16_t countNumber = 0;
// uint8_t clear= 0;

uint8_t status = 0;

int Lstand = 0;
int LstandCount = 0;

int Htemp = 0;
int HtempCount = 0;

// The array of tasks
sTask SCH_tasks_G[SCH_MAX_TASKS];


/*------------------------------------------------------------------*-

  SCH_Dispatch_Tasks()

  This is the 'dispatcher' function.  When a task (function)
  is due to run, SCH_Dispatch_Tasks() will run it.
  This function must be called (repeatedly) from the main loop.

-*------------------------------------------------------------------*/

void SCH_Dispatch_Tasks(void)
{
   unsigned char Index;

   // Dispatches (runs) the next task (if one is ready)
   for(Index = 0; Index < SCH_MAX_TASKS; Index++)
   {
      if((SCH_tasks_G[Index].RunMe > 0) && (SCH_tasks_G[Index].pTask != 0))
      {
         (*SCH_tasks_G[Index].pTask)();  // Run the task
         SCH_tasks_G[Index].RunMe -= 1;   // Reset / reduce RunMe flag

         // Periodic tasks will automatically run again
         // - if this is a 'one shot' task, remove it from the array
         if(SCH_tasks_G[Index].Period == 0)
         {
            SCH_Delete_Task(Index);
         }
      }
   }
}

/*------------------------------------------------------------------*-

  SCH_Add_Task()

  Causes a task (function) to be executed at regular intervals 
  or after a user-defined delay

  pFunction - The name of the function which is to be scheduled.
              NOTE: All scheduled functions must be 'void, void' -
              that is, they must take no parameters, and have 
              a void return type. 
                   
  DELAY     - The interval (TICKS) before the task is first executed

  PERIOD    - If 'PERIOD' is 0, the function is only called once,
              at the time determined by 'DELAY'.  If PERIOD is non-zero,
              then the function is called repeatedly at an interval
              determined by the value of PERIOD (see below for examples
              which should help clarify this).


  RETURN VALUE:  

  Returns the position in the task array at which the task has been 
  added.  If the return value is SCH_MAX_TASKS then the task could 
  not be added to the array (there was insufficient space).  If the
  return value is < SCH_MAX_TASKS, then the task was added 
  successfully.  

  Note: this return value may be required, if a task is
  to be subsequently deleted - see SCH_Delete_Task().

  EXAMPLES:

  Task_ID = SCH_Add_Task(Do_X,1000,0);
  Causes the function Do_X() to be executed once after 1000 sch ticks.            

  Task_ID = SCH_Add_Task(Do_X,0,1000);
  Causes the function Do_X() to be executed regularly, every 1000 sch ticks.            

  Task_ID = SCH_Add_Task(Do_X,300,1000);
  Causes the function Do_X() to be executed regularly, every 1000 ticks.
  Task will be first executed at T = 300 ticks, then 1300, 2300, etc.            
 
-*------------------------------------------------------------------*/

unsigned char SCH_Add_Task(void (*pFunction)(), const unsigned int DELAY, const unsigned int PERIOD)
{
   unsigned char Index = 0;

   // First find a gap in the array (if there is one)
   while((SCH_tasks_G[Index].pTask != 0) && (Index < SCH_MAX_TASKS))
   {
      Index++;
   }

   // Have we reached the end of the list?   
   if(Index == SCH_MAX_TASKS)
   {
      // Task list is full, return an error code
      return SCH_MAX_TASKS;  
   }

   // If we're here, there is a space in the task array
   SCH_tasks_G[Index].pTask = pFunction;
   SCH_tasks_G[Index].Delay =DELAY;
   SCH_tasks_G[Index].Period = PERIOD;
   SCH_tasks_G[Index].RunMe = 0;

   // return position of task (to allow later deletion)
   return Index;
}

/*------------------------------------------------------------------*-

  SCH_Delete_Task()

  Removes a task from the scheduler.  Note that this does
  *not* delete the associated function from memory: 
  it simply means that it is no longer called by the scheduler. 
 
  TASK_INDEX - The task index.  Provided by SCH_Add_Task(). 

  RETURN VALUE:  RETURN_ERROR or RETURN_NORMAL

-*------------------------------------------------------------------*/

unsigned char SCH_Delete_Task(const unsigned char TASK_INDEX)
{
   // Return_code can be used for error reporting, NOT USED HERE THOUGH!
   unsigned char Return_code = 0;

   SCH_tasks_G[TASK_INDEX].pTask = 0;
   SCH_tasks_G[TASK_INDEX].Delay = 0;
   SCH_tasks_G[TASK_INDEX].Period = 0;
   SCH_tasks_G[TASK_INDEX].RunMe = 0;

   return Return_code;
}

/*------------------------------------------------------------------*-

  SCH_Init_T1()

  Scheduler initialisation function.  Prepares scheduler
  data structures and sets up timer interrupts at required rate.
  You must call this function before using the scheduler.  

-*------------------------------------------------------------------*/

void SCH_Init_T1(void)
{
   unsigned char i;

   for(i = 0; i < SCH_MAX_TASKS; i++)
   {
      SCH_Delete_Task(i);
   }

   // Set up Timer 1
   // Values for 1ms and 10ms ticks are provided for various crystals

   // Hier moet de timer periode worden aangepast ....!
   OCR1A = (uint16_t)625;   		     // 10ms = (256/16.000.000) * 625
   TCCR1B = (1 << CS12) | (1 << WGM12);  // prescale op 64, top counter = value OCR1A (CTC mode)
   TIMSK1 = 1 << OCIE1A;   		     // Timer 1 Output Compare A Match Interrupt Enable
}

/*------------------------------------------------------------------*-

  SCH_Start()

  Starts the scheduler, by enabling interrupts.

  NOTE: Usually called after all regular tasks are added,
  to keep the tasks synchronised.

  NOTE: ONLY THE SCHEDULER INTERRUPT SHOULD BE ENABLED!!! 
 
-*------------------------------------------------------------------*/

void SCH_Start(void)
{
      sei();
}

/*------------------------------------------------------------------*-

  SCH_Update

  This is the scheduler ISR.  It is called at a rate 
  determined by the timer settings in SCH_Init_T1().

-*------------------------------------------------------------------*/

ISR(TIMER1_COMPA_vect)
{
   unsigned char Index;
   for(Index = 0; Index < SCH_MAX_TASKS; Index++)
   {
      // Check if there is a task at this location
      if(SCH_tasks_G[Index].pTask)
      {
         if(SCH_tasks_G[Index].Delay == 0)
         {
            // The task is due to run, Inc. the 'RunMe' flag
            SCH_tasks_G[Index].RunMe += 1;

            if(SCH_tasks_G[Index].Period)
            {
               // Schedule periodic tasks to run again
               SCH_tasks_G[Index].Delay = SCH_tasks_G[Index].Period;
               SCH_tasks_G[Index].Delay -= 1;
            }
         }
         else
         {
            // Not yet ready to run: just decrement the delay
            SCH_tasks_G[Index].Delay -= 1;
         }
      }
   }
}

// ---------------------//
//End copy pasta Scheduler.c
// ---------------------//
// Eigen code			//
//----------------------//

/*
	ADCsingleREAD leest waardes van een poort

*/
int ADCsingleREAD(uint8_t adctouse)
{
	int ADCval;

	ADMUX = adctouse;        // use #1 ADC
	ADMUX |= (1 << REFS0);   // use AVcc as the reference
	ADMUX &= ~(1 << ADLAR);  // clear for 10 bit resolution

	// 128 prescale for 8Mhz
	ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);

	ADCSRA |= (1 << ADEN);    // Enable the ADC
	ADCSRA |= (1 << ADSC);    // Start the ADC conversion

	while(ADCSRA & (1 << ADSC)); // waits for the ADC to finish

	ADCval = ADCL;
	ADCval = (ADCH << 8) + ADCval; // ADCH is read so ADC can be updated again

	return ADCval;
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


void on(char pin){
	DDRB |= (1 << pin);
	PINB |= (1 << pin);
}

/*
	Simuleert de LED lampjes om de rolluik uit te rollen
*/
void simulateOUT(){
	on(PB3);
	_delay_ms(5000);
	on(PB2);
	_delay_ms(1000);
}

void off(char pin){
	DDRB |= (0 << pin);
	PINB |= (0 << pin);
}

/*
	Simuleert de LED lampjes om de rolluik op te rollen
*/
void simulateIN(){
	on(PB3);
	_delay_ms(5000);
	on(PB4);
	_delay_ms(1000);
}


//------------------------------------------//
//				 SensorLogic				//

//----------HeatSensor----------//
int hitteSensor(){
	double number1 = 0;
	int number2 = 0;
	number1 = ADCsingleREAD(1);
	number1 = number1 / 1024;   //find percentage of input reading
	number1 = number1 * 5;                     //multiply by 5V to get voltage
	number1 = number1 - 0.5;                   //Subtract the offset
	number1 = number1 * 100;                   //Convert to degrees
	//number2 = (int) number1; -> voor display 
	//transmit(number1);
	number1 = (int)number1;
	return number1;
}

// add current value to total heat value and count++
void countHS(){
	Htemp += hitteSensor();
	HtempCount ++;
}

/*
	Transmit hitte sensor
*/
void transmitHS(){
	int gem = Htemp / HtempCount; // Set gemiddelde naar htemp / htempcount (totaal getal gedeeld door opgetelde hoeveelheid)
	transmit(gem);
	if(gem > HTH && status == 0){
		simulateOUT();
		status = 1;
	}
	if(gem < HTL && status == 1){
		simulateIN();
		status = 0;
	}
}

//----------LichtSensor----------//
int lichtSensor(){
	return(ADCsingleREAD(0));
}

// add current value to total light value and count++
void countLS(){
	Lstand += lichtSensor();
	LstandCount ++;
}

/*
	Transmit licht sensor
*/
void transmitLS(){
	int gem = Lstand / LstandCount; // Set gemiddelde naar Lstand / LstandCount (totaal getal gedeeld door opgetelde hoeveelheid)
	transmit(gem);
	if(gem > LTH && status == 0){
		simulateOUT();
		status = 1;
	}
	if(gem < LTL && status == 1){
		simulateIN();
		status = 0;
	}
}

//----------DistanceSensor----------//

int distanceSensor(){
	on(PD7);
	_delay_ms(10);
	int duration = ADCsingleREAD(2);
	off(PD7);
	
	int distance= duration*0.034/2;
	
	return distance;
}

void transmitDS(){
	transmit(distanceSensor());
}


//				End SensorLogic				//
//------------------------------------------//



void simulate(){
	int hs = hitteSensor();
	int ls = lichtSensor();
	
//----------------------------//
//Uncomment for instant result//

// 	Licht sensor logic
// 	if(ls > LTH && status == 0){
// 		simulateOUT();
// 		status = 1;
// 	}
// 	if(ls < LTL && status == 1){
// 		simulateIN();
// 		status = 0;
// 	}
// 	
// 	// Hitte sensor logic
// 	if(hs > HTH && status == 0){
// 		simulateOUT();
// 		status = 1;
// 	}
// 	if(hs < HTL && status == 1){
// 		simulateIN();
// 		status = 0;
// 	}
//----------------------------//
}
void start_init(){
	on(PB4);	
}
int main()
{
	//inits
	start_init();
	uart_init();
	SCH_Init_T1(); // zet timer op 0
	
	// counts
	SCH_Add_Task(countHS,0,100);
	SCH_Add_Task(countLS,0,100);
	
	// transmits
	SCH_Add_Task(transmitHS,0,1000); // -> transmit to terminal
	SCH_Add_Task(transmitLS,0,1000); 
	SCH_Add_Task(transmitDS,0,1000); 
	
	
	// simulate
	SCH_Add_Task(simulate,0,100); 
	
	//start de scheduler
	SCH_Start(); 
	
	_delay_ms(1000);
	
	while(1) {	
		SCH_Dispatch_Tasks(); // zet een infinite loop voor de taken.
	}
	return 0;
}