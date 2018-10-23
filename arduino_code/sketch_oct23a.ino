/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/
// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;
const int lightPin = A0;
const int tempPin = A1;

// defines variables
long duration;
int distance;
int lightValue; // variable to store the value coming from the sensor
int tempValue; // variable to store the value coming from the sensor
double temp;

void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
}

void loop() {
// Clears the trigPin
digitalWrite(trigPin, LOW);
delay(1000);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;

// Read light value
lightValue = analogRead(lightPin); // read the value from the sensor

// Read temp value
tempValue = analogRead(tempPin); // read the value from the sensor
temp = (double)tempValue / 1024;   //find percentage of input reading
temp = temp * 5;                     //multiply by 5V to get voltage
temp = temp - 0.5;                   //Subtract the offset 
temp = temp * 100;                   //Convert to degrees 

// Prints the distance on the Serial Monitor
String StrDos = String(distance) + "," + String(lightValue) + "," + String(temp);
Serial.println(StrDos);
}
