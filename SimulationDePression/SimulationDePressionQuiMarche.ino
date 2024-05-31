#include <Adafruit_NeoPixel.h>

#define NEOPIXEL_PIN 6  
#define NUMPIXELS 1      

#define BOUTON_PIN 2       
#define DEBOUNCE_DELAY 5000   
#define AUTOMATIC_SHUTDOWN_DELAY 3000 

Adafruit_NeoPixel pixels(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);
bool ledAllumee = false;
bool boutonRelache = true;
bool tempsEcoule = false;
unsigned long tempsInitialAppui;

uint32_t couleurs[] = {pixels.Color(255, 0, 0), pixels.Color(0, 255, 0), pixels.Color(0, 0, 255)};
int indexCouleur = 0;

void setup() {
  pixels.begin();
  pinMode(BOUTON_PIN, INPUT); 
  pixels.setBrightness(50); 
  eteindreLED();
}

void loop() {
  int boutonEtat = digitalRead(BOUTON_PIN);

  if (boutonEtat == LOW && boutonRelache) {
    boutonRelache = false;
    tempsInitialAppui = millis(); 
    changerCouleur();
    allumerLED();
  }

  if (boutonEtat == HIGH) {
    boutonRelache = true;
  }

  if (millis() - tempsInitialAppui > AUTOMATIC_SHUTDOWN_DELAY) {
    if (ledAllumee) {
      tempsEcoule = true;
    }
  }

  if (tempsEcoule && ledAllumee) {
    eteindreLED();
    tempsEcoule = false;
  }
}

void changerCouleur() {
  indexCouleur = (indexCouleur + 1) % (sizeof(couleurs) / sizeof(couleurs[0]));
}

void allumerLED() {
  pixels.setPixelColor(0, couleurs[indexCouleur]);
  pixels.show();
  ledAllumee = true;
}

void eteindreLED() {
  pixels.setPixelColor(0, pixels.Color(0, 0, 0));
  pixels.show();
  ledAllumee = false;
}