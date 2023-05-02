import math 

#Random number 0 : 11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110
#Random number 1 : 10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000

def identical_consecutive_bits_test(bits):
    f1 = bits.count('1') /128
    zeros = bits.count('0') 
    runs = [bits[0]]
    for i in range (1,128):
        if bits[i] != bits[i-1]:
            runs.append(bits[i])
    num = len(runs)
    # вычисляем Вероятность
    P = math.erfc( abs(num-2*128*f1*(1-f1))/(2*math.sqrt(2*128)*f1*(1-f1)) )
    # проверяем гипотезу на уровне значимости 0.01
    print(P)
    #0.8946367310768166 -> последовательность случайна 
    return P > 0.01

def main():
    print(identical_consecutive_bits_test('11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110'))
    #0.7256806886581656 следовательно последовательность случайна 
    #True
    
    print(identical_consecutive_bits_test('10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000'))
    #0.4348456807201941 следовательно последовательность случайна 
    #True
    

if __name__ == "__main__":
    main()