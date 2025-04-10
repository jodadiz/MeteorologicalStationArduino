const int analogInPin1 = A0;  // Analog input pin 1
const int analogInPin2 = A1;  // Analog input pin 2
int sensorValue[2];        // value read from the pot
float voltageValue[2];        // voltage output 
unsigned long lastTime = 0 , sampleTime = 200; // time value

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  if(millis()-lastTime>sampleTime){
  lastTime = millis();
  // read the analog in value:
  sensorValue[0] = analogRead(analogInPin1);
  sensorValue[1] = analogRead(analogInPin2);
  // map it to the range of the analog out:
  voltageValue[0] = scaling(sensorValue[0], 0, 1023, 0, 5);
  voltageValue[1] = scaling(sensorValue[1], 0, 1023, 0, 5);
  // Send data to Python:
  Serial.println(voltageValue[0]); 
  Serial.println(voltageValue[1]);  
  Serial.println(random(-50,50));  
  Serial.println(random(0,100));   
  }
}

float scaling(float x, float in_min, float in_max, float out_min, float out_max) 
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
