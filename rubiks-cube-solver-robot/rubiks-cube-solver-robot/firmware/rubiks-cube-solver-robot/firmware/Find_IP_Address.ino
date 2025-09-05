#include <CubeCentral.h>
WebServer CubeCentral(192, 168, 8, 167);  //change this IP address when you find your IP adress

void setup() {
  Serial.begin(115200);
  CubeCentral.begin();
  CubeCentral.printIP(); //prints IP address
}

void loop() {
  CubeCentral.display();  //displays web server
}
