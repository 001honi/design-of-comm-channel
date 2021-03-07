void setup() {
  Serial.begin(2400);
}

void loop() {
  Serial.print('<');
  Serial.print(analogRead(A0));
  Serial.print(',');
  Serial.print(analogRead(A1));
  Serial.print('>');
  Serial.flush();
}
