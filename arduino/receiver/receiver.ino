#include <Servo.h>
//#define SERIAL_BUFFER_SIZE 2

Servo servo;   
int servoPin = 9;
int pos;     
int dly;

void setup() {
  servo.attach(servoPin);
  Serial.begin(3200);
//  Serial.setTimeout(100);
//  Serial.print(SERIAL_BUFFER_SIZE);
}

void loop() {
  if (Serial.available()>0){
    int inChar = Serial.read();
    if (inChar == '<'){
        delay(80);
        int param0 = Serial.readStringUntil(',').toInt()/100;
        int param1 = Serial.readStringUntil('>').toInt()/100;

        pos = map(param0, 0, 10, 0, 180);
        dly = map(param1, 0, 10, 5, 40);

        Serial.print("P:");
        Serial.print(pos);
        Serial.print("D:");
        Serial.println(dly);        
//        servo.write(pos);
//        delay(dly);      
    }
    else{
      delay(1);
    }
  }
}
