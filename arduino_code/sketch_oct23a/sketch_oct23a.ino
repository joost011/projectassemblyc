/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/
// defines pins numbers

const int tempPin = A0;

// defines variables
long duration;
 // variable to store the value coming from the sensor
int tempValue; // variable to store the value coming from the sensor
double temp;

void setup() {

Serial.begin(9600); // Starts the serial communication
}

void loop() {


// Read temp value
tempValue = analogRead(tempPin); // read the value from the sensor
temp = (double)tempValue / 1024;   //find percentage of input reading
temp = temp * 5;                     //multiply by 5V to get voltage
temp = temp - 0.5;                   //Subtract the offset 
temp = temp * 100;                   //Convert to degrees 

// Prints the distance on the Serial Monitor
String StrDos = String(temp);
Serial.println(StrDos);
}
