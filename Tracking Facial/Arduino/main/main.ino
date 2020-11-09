#include <Servo.h>
 
Servo myservo;  // crea el objeto servo
 
int pos = 90;    // posicion del servo

int pin = 9;
int servoPosition = 0;

int gradosDesplazamiento = 15;
 
void setup() {
   myservo.attach(pin);  // vincula el servo al pin digital 9
   Serial.begin(9600);
}
 
void loop() { 

  

  if (Serial.available() > 0) {
    // read the incoming byte:
    servoPosition = Serial.parseInt();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(servoPosition);
  }

  //Si es 1 giramos a la rizquierda
  if (servoPosition == 1){
    pos += gradosDesplazamiento;
    if (pos >180){
      pos = 180;
    }
    Serial.println(pos);
    myservo.write(pos);              
    delay(15);
    servoPosition = 0;
  }

  //Si es 2 giramos derecha
  if (servoPosition == 2){
     pos -= gradosDesplazamiento;
     if (pos < 0){
      pos = 0;
    }
     Serial.println(pos);
     myservo.write(pos);              
     delay(15);
     servoPosition = 0;
  }
  
}
