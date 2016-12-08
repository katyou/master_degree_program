#include "Wire.h"
#include "INA226.h"
#include "TimerOne.h"

#define period 50    //initialize timer1, and m seconds period (microseconds)

INA226 ina;
INA226 ina2;

int dutymeasure;

void sepicmeasure()
{

  int j;

  for(j=0; j<300; j++)
  {
    Serial.print(dutymeasure);
    Serial.print(", ");

    Serial.print(ina.readBusVoltage(), 5); //5 is significant digits in serial.
    Serial.print(", ");

    Serial.print(ina.readShuntCurrent(), 5);
    Serial.print(",     ");


    Serial.print(ina2.readBusVoltage(), 5);
    Serial.print(", ");

    Serial.print(ina2.readShuntCurrent(), 5);
    Serial.println("");
    delay(100);
  }
  Serial.println("-----------------------------------------------");
}

void setup()
{
  Serial.begin(115200);
  Serial.println("IV-measurement");
  Serial.println("-----------------------------------------------");

  ina.begin(0x45);              //solar cell                                       //INA226のアドレス値変更箇所
  ina2.begin(0x48);             //fuel cell

  ina.configure(INA226_AVERAGES_1, INA226_BUS_CONV_TIME_1100US, INA226_SHUNT_CONV_TIME_1100US, INA226_MODE_SHUNT_BUS_CONT);
  ina.calibrate(0.002, 5);
  ina2.configure(INA226_AVERAGES_1, INA226_BUS_CONV_TIME_1100US, INA226_SHUNT_CONV_TIME_1100US, INA226_MODE_SHUNT_BUS_CONT);
  ina2.calibrate(0.002, 5);

  Timer1.initialize(period);

  Serial.print("       ");
  Serial.print("INPUT");
  Serial.print("                      ");
  Serial.println("OUTPUT");

  Serial.print("Duty   ");
  Serial.print("Voltage ");
  Serial.print("Current ");

  Serial.print("      ");

  Serial.print("Voltage ");
  Serial.println("Current ");



  Serial.println("-----------------------------------------------");
}


void loop()
{
  int duty;
  Timer1.pwm(9, 0);
  if (Serial.available() > 0)
  {
    duty = Serial.read();
    dutymeasure = (duty * 1023)/100;
    Timer1.pwm(9, dutymeasure);
    sepicmeasure();
  }
}
