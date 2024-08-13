//Code for arduino ide
//Originaly made for esp32c6-devkit-c1 and MPU6050 module

//TODO: make printing out code more neat

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

int button1 = 10; //Left button input
int button2 = 11; //Right button input
int button3 = 19; //Middle button input
int button4 = 18; //Movement button, Mouse only moves when this button is pressed

void setup() {//--------------------Setup

  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);

  Serial.begin(115200);
  while (!Serial) { delay(50); } // Pauses, until serial opens
  
  // Checks for MPU6050 presence
  if (!mpu.begin()) {
    Serial.println("ERROR. Failed to find the accelerometer chip");
    while (1) { delay(1000); }
  }
  // Configs the mpu6050
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {//--------------------Loop
  
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  // Prints out everything to the serial for "Glove_mouse_script.py" to read
  Serial.print("S");
  Serial.print(String(digitalRead(button1)));
  Serial.print(",");
  Serial.print(String(digitalRead(button2)));
  Serial.print(",");
  Serial.print(String(digitalRead(button3)));
  Serial.print(",");
  Serial.print(String(digitalRead(button4)));
  Serial.print(",");
  Serial.print(int(a.acceleration.x));
  Serial.print(",");
  Serial.println(int(a.acceleration.y));
  delay(10);
}