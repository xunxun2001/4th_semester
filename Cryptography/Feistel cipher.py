import binascii
import numpy as np
def reverse(s):
    return ''.join(str(1^int(c)) for c in s)

def rand_key(p):
    import random
    key1 = ""
    p = int(p)

    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key1 = key1 + temp

    return (key1)

def exor(a, b):
    temp = ""
    for i in range(n):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"

    return temp

def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

def Feistel(R1, K1,L1):
    K = reverse(K1)
    f1 = exor(R1, K)
    R2 = exor(f1, L1)
    L2 = R1
    return L2 , R2

# Feistel Cipher
def main():
    PT = input("Please Input Your Plain Text In ENGLISH:")
    PT_Ascii = [ord(x) for x in PT]

    PT_Bin = [format(y, '08b') for y in PT_Ascii]
    PT_Bin = "".join(PT_Bin)

    global n
    n = int(len(PT_Bin) // 2)
    L1 = PT_Bin[0:n]
    R1 = PT_Bin[n::]
    m = len(R1)

    K1 = rand_key(m)

    L2, R2 = Feistel(R1, K1, L1)

    # Cipher text
    bin_data = L2 + R2
    str_data = ' '

    for i in range(0, len(bin_data), 7):
        temp_data = bin_data[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)

    print("Cipher Text:", str_data)

    # Decryption
    DeL1 = L2
    DeR1 = R2

    DeR2, DeL2 = Feistel(DeL1, K1, DeR1)

    PT1 = DeL2 + DeR2

    PT1 = int(PT1, 2)
    RPT = binascii.unhexlify('%x' % PT1)
    print("Retrieved Plain Text is: ", RPT)
    print(f"The key code is {K1}.")

if __name__ == '__main__':
    main()
