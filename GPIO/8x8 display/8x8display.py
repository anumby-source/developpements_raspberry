# working
import RPi.GPIO as GPIO
import time  # calling for time to provide delays in program

GPIO.setwarnings(False)  # do not show any warnings
x = 1
y = 1

GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers. (like PIN29 as'GPIO5')

# pins of the 8x8 display
LED_column_pin = [13, 3, 4, 10, 6, 11, 15, 16]
LED_row_pin = [9, 14, 8, 12, 1, 7, 2, 5]

# GPIO connections
LED_column_gpio = [12, 22, 27, 25, 17, 24, 23, 18]
LED_row_gpio = [21, 20, 26, 16, 19, 13, 6, 5]

SETUP = False

def get_row_column(led):
    row = int((led - 1) / 8)
    positive = LED_row_gpio[row]
    row_pin = LED_row_pin[row]

    column = (led - 1) % 8
    negative = LED_column_gpio[column]
    column_pin = LED_column_pin[column]

    return row+1, column+1, positive, negative, row_pin, column_pin


def setup_gpio():
    for negative in LED_column_gpio:
        IO.setup(negative, GPIO.OUT)
    for positive in LED_row_gpio:
        IO.setup(positive, GPIO.OUT)
    SETUP = True
        
        
def led_on(led):
    row = int((led - 1) / 8)
    positive = LED_row_gpio[row]
    column = (led - 1) % 8
    negative = LED_column_gpio[column]
    if SETUP:
       GPIO.output(negative, 0)  # if bit0 of 8bit 'pin' is true pull PIN21 low
       GPIO.output(positive, 1)  # if bit0 of 8bit 'pin' is true pull PIN21 low
    return positive, negative


def leds_on(leds):
    for led in leds:
        led_on(led)
        time.sleep(0.0005)


PORTVALUE = [128, 64, 32, 16, 8, 4, 2, 1]


# value of pin in each port
A = [0, 0b01111111, 0b11111111, 0b11001100, 0b11001100, 0b11001100, 0b11111111, 0b01111111]
B = [0, 0b00111100, 0b01111110, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
C = [0, 0b11000011, 0b11000011, 0b11000011, 0b11000011, 0b11100111, 0b01111110, 0b00111100]
D = [0, 0b01111110, 0b10111101, 0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b11111111]
E = [0, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
F = [0, 0b11011000, 0b11011000, 0b11011000, 0b11011000, 0b11011000, 0b11111111, 0b11111111]
G = [0b00011111, 0b11011111, 0b11011000, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
H = [0, 0b11111111, 0b11111111, 0b00011000, 0b00011000, 0b00011000, 0b11111111, 0b11111111]
I = [0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b11111111, 0b11000011, 0b11000011, 0b11000011]
J = [0b11000000, 0b11000000, 0b11000000, 0b11111111, 0b11111111, 0b11000011, 0b11001111, 0b11001111]
K = [0, 0b11000011, 0b11100111, 0b01111110, 0b00111100, 0b00011000, 0b11111111, 0b11111111]
L = [0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b11111111, 0b11111111]
M = [0b11111111, 0b11111111, 0b01100000, 0b01110000, 0b01110000, 0b01100000, 0b11111111, 0b11111111]
N = [0b11111111, 0b11111111, 0b00011100, 0b00111000, 0b01110000, 0b11100000, 0b11111111, 0b11111111]
O = [0b01111110, 0b11111111, 0b11000011, 0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b01111110]
P = [0, 0b01110000, 0b11111000, 0b11001100, 0b11001100, 0b11001100, 0b11111111, 0b11111111]
Q = [0b01111110, 0b11111111, 0b11001111, 0b11011111, 0b11011011, 0b11000011, 0b11111111, 0b01111110]
R = [0b01111001, 0b11111011, 0b11011111, 0b11011110, 0b11011100, 0b11011000, 0b11111111, 0b11111111]
S = [0b11001110, 0b11011111, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11111011, 0b01110011]
T = [0b11000000, 0b11000000, 0b11000000, 0b11111111, 0b11111111, 0b11000000, 0b11000000, 0b11000000]
U = [0b11111110, 0b11111111, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b11111111, 0b11111110]
V = [0b11100000, 0b11111100, 0b00011110, 0b00000011, 0b00000011, 0b00011110, 0b11111100, 0b11100000]
W = [0b11111110, 0b11111111, 0b00000011, 0b11111111, 0b11111111, 0b00000011, 0b11111111, 0b11111110]
X = [0b01000010, 0b11100111, 0b01111110, 0b00111100, 0b00111100, 0b01111110, 0b11100111, 0b01000010]
Y = [0b01000000, 0b11100000, 0b01110000, 0b00111111, 0b00111111, 0b01110000, 0b11100000, 0b01000000]
Z = [0b11000011, 0b11100011, 0b11110011, 0b11111011, 0b11011111, 0b11001111, 0b11000111, 0b11000011]


def leds_letter(letter):
    leds = []
    # print("letter={} ".format(letter))
    r = 0
    for row in letter:
        p2 = 1
        for col in range(8):
            b = row & p2
            led = r*8 + col + 1
            # print("p2={:8b} row={:8b} b={:8b} led={}".format(p2, col, b, led))
            if b != 0:
                leds.append(led)
            p2 *= 2
        r += 1
    return leds
            
            
def setup_letter_leds():
    letter_array = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    letter_leds = []
    for letter in letter_array:
        leds = leds_letter(letter)
        letter_leds.append(leds)
        
    return letter_leds


def PORT(pin):  # assigning GPIO state by taking 'pin' value
    if (pin & 0x01 == 0x01):
        IO.output(21, 0)  # if bit0 of 8bit 'pin' is true pull PIN21 low
    else:
        IO.output(21, 1)  # if bit0 of 8bit 'pin' is false pull PIN21 high
    if (pin & 0x02 == 0x02):
        IO.output(20, 0)  # if bit1 of 8bit 'pin' is true pull PIN20 low
    else:
        IO.output(20, 1)  # if bit1 of 8bit 'pin' is false pull PIN20 high
    if (pin & 0x04 == 0x04):
        IO.output(26, 0)  # if bit2 of 8bit 'pin' is true pull PIN26 low
    else:
        IO.output(26, 1)  # if bit2 of 8bit 'pin' is false pull PIN26 high
    if (pin & 0x08 == 0x08):
        IO.output(16, 0)
    else:
        IO.output(16, 1)


    if (pin & 0x10 == 0x10):
        IO.output(19, 0)
    else:
        IO.output(19, 1)
    if (pin & 0x20 == 0x20):
        IO.output(13, 0)
    else:
        IO.output(13, 1)
    if (pin & 0x40 == 0x40):
        IO.output(6, 0)
    else:
        IO.output(6, 1)
    if (pin & 0x80 == 0x80):
        IO.output(5, 0)
    else:
        IO.output(5, 1)


def PORTP(pinp):  # assigning GPIO logic for positive terminals by taking 'pinp' value
    if (pinp & 0x01 == 0x01):
        IO.output(12, 1)  # if bit0 of 8bit 'pinp' is true pull PIN12 high
    else:
        IO.output(12, 0)  # if bit0 of 8bit 'pinp' is false pull PIN12 low
    if (pinp & 0x02 == 0x02):
        IO.output(22, 1)  # if bit1 of 8bit 'pinp' is true pull PIN22 high
    else:
        IO.output(22, 0)  # if bit1 of 8bit 'pinp' is false pull PIN22 low
    if (pinp & 0x04 == 0x04):
        IO.output(27, 1)  # if bit2 of 8bit 'pinp' is true pull PIN27 high
    else:
        IO.output(27, 0)  # if bit2 of 8bit 'pinp' is false pull PIN27 low
    if (pinp & 0x08 == 0x08):
        IO.output(25, 1)
    else:
        IO.output(25, 0)
    if (pinp & 0x10 == 0x10):
        IO.output(17, 1)
    else:
        IO.output(17, 0)
    if (pinp & 0x20 == 0x20):
        IO.output(24, 1)
    else:
        IO.output(24, 0)
    if (pinp & 0x40 == 0x40):
        IO.output(23, 1)
    else:
        IO.output(23, 0)
    if (pinp & 0x80 == 0x80):
        IO.output(18, 1)  # if bit7 of 8bit 'pinp' is true pull PIN18 high
    else:
        IO.output(18, 0)  # if bit7 of 8bit 'pinp' is false pull PIN18 low

def scroll():
    while 1:
        for y in range(100):  # execute loop 100 times
            for x in range(8):  # execute the loop 8 times incrementing x value from zero to seven
                pin = PORTVALUE[x]  # assigning value to 'pin' for each digit
                PORT(pin);  # mapping appropriate GPIO
                pinp = C[x]  # assigning character 'C' value to 'pinp'
                PORTP(pinp);  # turning the GPIO to show character 'C'
                time.sleep(0.0005)  # wait for 0.5msec
        for y in range(100):
            for x in range(8):
                pin = PORTVALUE[x]
                PORT(pin);
                pinp = I[x]
                PORTP(pinp);
                time.sleep(0.0005)

    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = R[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = C[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = U[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = I[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = T[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = D[x]
            PORTP(pinp);
            time.sleep(0.0005)

    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = I[x]
            PORTP(pinp);
            time.sleep(0.0005)
    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = G[x]
            PORTP(pinp);
            time.sleep(0.0005)

    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = E[x]
            PORTP(pinp);
            time.sleep(0.0005)

    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = S[x]
            PORTP(pinp);
            time.sleep(0.0005)

    for y in range(100):
        for x in range(8):
            pin = PORTVALUE[x]
            PORT(pin);
            pinp = T[x]
            PORTP(pinp);
            time.sleep(0.0005)
    pinp = 0
    PORTP(pinp);
    time.sleep(1)


if __name__ == '__main__':
    for led in [1, 8, 9, 64]:
       # rc = get_row_column(led)
       rc = led_on(led)
       print(led, rc)

    leds = leds_letter(A)
    # print(leds)
    
    leds = setup_letter_leds()
    # print(leds)
    
    for letter_leds in leds:
        print(letter_leds)
        for y in range(100):
            leds_on(letter_leds)
    
