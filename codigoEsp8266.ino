#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

// Set these to run example.
#define FIREBASE_HOST "https://esp8266-f7b58-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "KR1M3ooOlPNL0VF5rAR0E6kCbJT4y4EiRHDXxG7Q"
#define WIFI_SSID "HOME-56EE"
#define WIFI_PASSWORD "72346192FBB98FDF"

const int ligthpin =0;

FirebaseData firesbasedata;
SoftwareSerial nodemcu(D6, D5);
void setup() {
  Serial.begin(9600);
  nodemcu.begin(9600);
  pinMode(ligthpin,INPUT);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {
  
  Serial.println("JSON Object Recieved");
  StaticJsonBuffer<1000> jsonBuffer;
  JsonObject& data = jsonBuffer.parseObject(nodemcu);
  if (data == JsonObject::invalid()) {
    jsonBuffer.clear();
   return;}
  int ligth=digitalRead(ligthpin);
  //int ligth= data["Ligth"];
  //float humidity= data["Humidity"];
  //float temperatura= data["Temperatura"];
  //float humedadaire= data["Humedadaire"];
  Serial.print("Recieved ligth:  ");
  Serial.print(ligth);
  //Serial.print("Recieved Humidity:  ");
  //Serial.print(humidity);
  //Serial.print("Recieved Temperatura:  ");
  //Serial.print(temperatura);
  //Serial.print("Recieved huidity of the air:  ");
  //Serial.print(humedadaire);
  //if(Firebase.setFloat(firesbasedata,"ligth",32.8)){
    //Serial.print("ligth");}
  //else{
      //Serial.println(firesbasedata.errorReason());
  //}
  if(Firebase.setInt(firesbasedata,"ligth", ligth)){
    Serial.print("xd");}
  else{
      Serial.println(firesbasedata.errorReason());
  }
  delay(1000);
}
