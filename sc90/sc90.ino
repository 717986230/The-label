#include<Servo.h>
#define Echo D2
#define Trig D8
#define DPIN D5
Servo myDPIN;
 long getTime() 
 {
  digitalWrite(Trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig,LOW);
  
  return pulseIn(Echo,HIGH);
  }
  
void initCS()
{
   pinMode(Echo,INPUT);
   pinMode(Trig,OUTPUT); 
  
 }

void setup() {
    initCS();
    myDPIN.attach(DPIN);
    Serial.begin(115200);
}

void loop() {
  long dis;
  dis = getTime() / 58;
  delay(100);
  Serial.print(dis);
  Serial.println("cm");
  if(dis < 10){
    myDPIN.write(90);
    
    }else{
      myDPIN.write(180);
      }
     delay(100);
}
  /*int cmd;
  if(Serial.available() > 0){
    cmd = Serial.read();
    if(cmd == 1){
      myDuoJi.write(90);
      }
      if(cmd == 0){
        myDuoJi.write(180);
        }*/
  
  /*myDuoJi.write(0);
  delay(1000);
  myDuoJi.write(180);
  delay(1000);*/
