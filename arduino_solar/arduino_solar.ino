void Measure()
{
  int Vi;
  int Im;
  int v[300];
  int i[300];
  int x;
  for(x = 1; x <= 300; x++)
  {
    delay(50);
    Vi = analogRead(A1);
    v[x] = Vi;
    Im = analogRead(A5);
    i[x] = Im;
  }
  delay(5000);
  for(x = 1; x <= 300; x++)
  {
    Serial.print(v[x]);
    Serial.print(',');
    Serial.println(i[x]);
    delay(40);
  }
}

void setup()
{
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}


void loop()
{
  char a;
  if (Serial.available() > 0)
  {
    a = Serial.read();
    if (a == 'z')
    {
      delay(40);
      digitalWrite(8,LOW);
      delay(100);
      Measure();
    }
    if (a == 'y')
    {
      digitalWrite(8,HIGH);
    }
  }
}


