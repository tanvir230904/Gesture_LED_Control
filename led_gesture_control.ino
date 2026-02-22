int led1 = 3;
int led2 = 4;
int led3 = 5;
int led4 = 6;
int led5 = 7;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == '1') digitalWrite(led1, HIGH);
    else if (cmd == 'A') digitalWrite(led1, LOW);

    if (cmd == '2') digitalWrite(led2, HIGH);
    else if (cmd == 'B') digitalWrite(led2, LOW);

    if (cmd == '3') digitalWrite(led3, HIGH);
    else if (cmd == 'C') digitalWrite(led3, LOW);

    if (cmd == '4') digitalWrite(led4, HIGH);
    else if (cmd == 'D') digitalWrite(led4, LOW);

    if (cmd == '5') digitalWrite(led5, HIGH);
    else if (cmd == 'E') digitalWrite(led5, LOW);
  }
}


