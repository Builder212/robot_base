#include <AFMotor.h>

AF_DCMotor motor_1(1, MOTOR12_64KHZ);
AF_DCMotor motor_2(2, MOTOR12_64KHZ);
AF_DCMotor motor_3(3, MOTOR12_64KHZ);
AF_DCMotor motor_4(4, MOTOR12_64KHZ);

void setup() {
  Serial.begin(115200);

  motor_1.setSpeed(200);
  motor_2.setSpeed(200);
  motor_3.setSpeed(200);
  motor_4.setSpeed(200);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readString();
    if (command == "F") {
      motor_1.run(FORWARD);
      motor_2.run(FORWARD);
      motor_3.run(FORWARD);
      motor_4.run(FORWARD);
    } else if (command == "B") {
      motor_1.run(BACKWARD);
      motor_2.run(BACKWARD);
      motor_3.run(BACKWARD);
      motor_4.run(BACKWARD);
    } else if (command == "S") {
      motor_1.run(RELEASE);
      motor_2.run(RELEASE);
      motor_3.run(RELEASE);
      motor_4.run(RELEASE);
    } else if (command == "R") {
      motor_1.run(FORWARD);
      motor_2.run(BACKWARD);
      motor_3.run(FORWARD);
      motor_4.run(BACKWARD);
    } else if (command == "L") {
      motor_1.run(BACKWARD);
      motor_2.run(FORWARD);
      motor_3.run(BACKWARD);
      motor_4.run(FORWARD);
    }
  }
  delay(10);
}
