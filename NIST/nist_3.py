import math
import scipy
from scipy.special import gammaincc

#Random number 0 : 11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110
#Random number 1 : 10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000
def longtest(bits):
    num_blocks = 128 // 8
    mas_count = []
    for i in range(16):
        block = bits[i * 8: (i + 1) * 8]
        one = 0
        max_one_in_block = 0
        max_run = 0
        for bit in block:
            if bit == '1':
                one += 1
                max_one_in_block = max(max_one_in_block, one)
            else:
                one = 0
        max_run = max(max_run, max_one_in_block)
        mas_count.append(max_run)

    v1 = sum(x <= 1 for x in mas_count)
    v2 = sum(x == 2 for x in mas_count)
    v3 = sum(x == 3 for x in mas_count)
    v4 = sum(x > 4 for x in mas_count)
    k0 = 0.2148
    k1 = 0.3672
    k2 = 0.2305
    k3 = 0.1875
    X = ((v1-16*k0)**2)/(16*k0)+((v2-16*k1)**2)/(16*k1) + ((v3-16*k2)**2)/(16*k2)+((v4-16*k3)**2)/(16*k3)
    P=gammaincc(3/2,X/2)
    print(P)
    return (P > 0.01)

def main():
    bits = '11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110'
    print(longtest(bits))
    #0.4836430435754958
    #True

    print("\n\n")
    bits = '10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000'
    print(longtest(bits))
    #0.9087610381824585
    #TRUE
    
    
if __name__ == "__main__":
    main()