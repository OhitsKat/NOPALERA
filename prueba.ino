#include <Servo.h>

Servo servoMotor;
int x;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 servoMotor.attach(9);
 servoMotor.write(0);
}

void loop() {
 while (Serial.available());
 if(Serial.readString() == "1"){
  delay(5000);
  for (int i = 0; i <= 180; i++)
  {
    // Desplazamos al ángulo correspondiente
    servoMotor.write(i);
    // Hacemos una pausa de 25ms
    delay(25);
  }
  delay(5000);
  // Para el sentido negativo
  for (int i = 179; i > 0; i--)
  {
    // Desplazamos al ángulo correspondiente
    servoMotor.write(i);
    // Hacemos una pausa de 25ms
    delay(25);
  }
 }
}
