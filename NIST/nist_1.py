import random
import math
#Random number 0 : 11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110
#Random number 1 : 10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000
def bit_frequency_test(bit_sequence: str):

    num_bits = len(bit_sequence)
    num_ones = bit_sequence.count('1')
    num_zeros = num_bits - num_ones
    S = abs(num_zeros - num_ones) / math.sqrt(num_bits)

    P_value = math.erfc(S / math.sqrt(2))

    print(P_value)
    return P_value > 0.01


def main():
    print(bit_frequency_test("11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110"),"\n\n")
    #0.8596837951986662
    #True 
    print(bit_frequency_test("10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000"))
    #0.37675911781158217
    #True
if __name__ =="__main__":
    main()

