import math

def mcc():
    """
    Morse Code Converter
    >> converts a single character
    >> converts a 6 characters inputted singly, prints string

    """
    morse = {"A": ".-",
             "B": "-...",
             "C": "-.-.",
             "D": "-..",
             "E": ".",
             "F": "..-.",
             "G": "--.",
             "H": "....",
             "I": "..",
             "J": ".---",
             "K": "-.-",
             "L": ".-..",
             "M": "--",
             "N": "-.",
             "O": "---",
             "P": ".--.",
             "Q": "--.-",
             "R": ".-.",
             "S": "...",
             "T": "-",
             "U": "..-",
             "V": "...-",
             "W": ".--",
             "X": "-..-",
             "Y": "-.--",
             "Z": "--..",
             "0": "-----",
             "1": ".----",
             "2": "..---",
             "3": "...--",
             "4": "....-",
             "5": ".....",
             "6": "-....",
             "7": '--...',
             "8": "---..",
             "9": "----.",
             ".": ".-.-.-",
             ',': "--..--"}

    print(morse[input('enter character to be converted').upper()])

    print(
        f'{morse[input("1:").upper()]} '
        f'{morse[input("2:").upper()]} '
        f'{morse[input("3:").upper()]} '
        f'{morse[input("4:").upper()]} '
        f'{morse[input("5:").upper()]} '
        f'{morse[input("6:").upper()]}')

def distance_and_slope():
    print('|========================|')
    print("|=Enter your coordinates=|")
    print("|====(x1,y1),(x2,y2)=====|")

    x1 = int(input("X1 cord: "))
    y1 = int(input("Y1 cord: "))
    x2 = int(input("X2 cord: "))
    y2 = int(input("Y2 cord: "))

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    slope = (y2 - y1) / (x2 - x1)
    tanvar = (x2 - x1)/(y2 - y1)
    ang = math.atan(tanvar)
    deg = math.degrees(ang)

    print("=======Solutions========")
    print("====(x1,y1),(x2,y2)=====")
    print("distance:", dist)
    print("slope:", slope)
    print("angle in radians:", ang)
    print("angle in degrees:", deg)

    print('|========================|')
    print("|=Enter your coordinates=|")
    print("|====(x3,y3),(x4,y4)=====|")

    x3 = int(input("X3 cord: "))
    y3 = int(input("Y3 cord: "))
    x4 = int(input("X4 cord: "))
    y4 = int(input("Y4 cord: "))

    dist1 = math.sqrt((x4 - x3) * 2 + (y4 - y3) ** 2)
    slope1 = (y4 - y3) / (x4 - x3)

    tanvar1 = (x4 - x3)/(y4 - y3)
    ang1 = math.atan(tanvar1)
    deg1 = math.degrees(ang1)

    print("=======Solutions========")
    print("====(x3,y3),(x4,y4)=====")
    print("distance:", dist1)
    print("slope:", slope1)
    print("angle in radians:", ang1)
    print("angle in degrees:", deg1)

    print("=======Solutions========")
    print("====(x1,y1),(x2,y2)=====")
    print("====(x3,y3),(x4,y4)=====")
    print("========================")
    print("total degrees: ", deg + deg1)


func_dict = {'dns': distance_and_slope,
             'mcc': mcc}

if __name__ == "__main__":
    print('Enter a Command')
    print('dns: distamce and slope\nmcc: morse code converter')
    command = input('>>>')
    func_dict[command]()


