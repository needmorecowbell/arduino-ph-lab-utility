

 /*
  * PH Serial Proof of Concept
  *   - randomly outputs data in a way that will be similar to the ph probe's data
  *   - created for use of the ph logging program in python, without the need for the probe --aka prototyping/debugging
  * 
  * Developed by: Adam Musciano   
  * 
 */



void setup() {
  Serial.begin(9600);
}

void loop() { // run over and over
  delayedInput(300);
  
}

void delayedInput(int delayTime){
  Serial.println(random(600,1000)/100.0);
  delay(delayTime);
}


