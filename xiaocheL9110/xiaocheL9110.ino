#include<ESP8266WiFi.h>
#include<Servo.h>
#define zhuan1 D6
#define zhuan2 D7
#define dong1 D4
#define dong2 D5

#define Echo D2
#define Trig D8

char* ssid = "小杨的灯灯";
char* passwd = "745619yxh";

int port = 8888;
WiFiServer server(port);

long getTime()
{
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

  return pulseIn(Echo, HIGH);
}
void initCS()
{
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);

}
void initWifisSta() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, passwd);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println(WiFi.localIP());
}
void initL9110s() {
  pinMode(dong1, OUTPUT);
  pinMode(dong2, OUTPUT);
  pinMode(zhuan1, OUTPUT);
  pinMode(zhuan2, OUTPUT);
}
void  qian() {
  digitalWrite(dong1, LOW);
  digitalWrite(dong2, HIGH);
}

void hou() {
  digitalWrite(dong1, HIGH);
  digitalWrite(dong2, LOW);
}
void zuo() {
  digitalWrite(zhuan1, LOW);
  digitalWrite(zhuan2, HIGH);
}
void ting() {
  digitalWrite(dong1, LOW);
  digitalWrite(dong2, LOW);
}
void zheng() {
  digitalWrite(zhuan1, LOW);
  digitalWrite(zhuan2, LOW);
}
void you() {
  digitalWrite(zhuan1, HIGH);
  digitalWrite(zhuan2, LOW);
}
void setup() {
  initCS();
  initL9110s();
  Serial.begin(115200);
  initWifisSta();
  server.begin();
}

void loop() {
  char cmd;
  int mark = 0;
  long dis;

  WiFiClient client = server.available();
  while (client.connected()) {
    while (client.available() > 0) {
      cmd = client.read();
      Serial.println(cmd);
      dis = getTime() / 58;
        delay(100);
      
      if (dis < 10) {
        hou();
        delay(200);
        ting();
        mark = 1;

      } else {
        mark = 0;
      }
      //if(Serial.available() > 0){
      //cmd = Serial.read();
      if(mark == 0){
       switch (cmd) {
        case'q':
          qian();
          break;
        case'h':
          hou();
          break;
        case'z':
          zuo();
          break;
        case'y':
          you();
          break;
        case'd':
          zheng();
          break;
        case's':
          ting();
          break;
        }
      }
    }
  }
}
