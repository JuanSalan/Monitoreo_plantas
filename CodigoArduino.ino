#include <dht.h>
#include <SoftwareSerial.h>
#include <ArduinoJson.h>
dht DHT;
#define DHT11_PIN 2
const int ligthpin =0;
const int Sensorhumidity=A0;
SoftwareSerial nodemcu(5, 6);

void setup() {
  Serial.begin(9600);
  pinMode(ligthpin,INPUT);
  nodemcu.begin(9600);
}

void loop() {
    StaticJsonBuffer<1000> jsonBuffer;
    JsonObject& data = jsonBuffer.createObject();
    DHT.read11(DHT11_PIN);
    int ligth=digitalRead(ligthpin);
    int humidity = analogRead(Sensorhumidity);
    int temperatura=(DHT.temperature);
    temperatura=map(temperatura,0,1023,0,50);
    int humedadaire=(DHT.humidity);
    data["Ligth"] = ligth;
    data["Humidity"] = humidity;
    data["Temperatura"] = temperatura;
    data["Humedadaire"] = humedadaire;
    data.printTo(nodemcu);
    jsonBuffer.clear();
    delay(1000);
}
