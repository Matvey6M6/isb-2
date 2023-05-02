#include <iostream>
#include <random>
#include <bitset>
using namespace std;


vector<string> get_ranom_num_128bit() {
    random_device rd;
    mt19937_64 generator(rd());
    vector<string> result;
    bitset<128>  bits;
    bitset<128> bits2;
    for (int i = 0; i < 128; i++) {
        bits[i] = generator() & 1;
        bits2[i] = rand()%2;
    }
    result.push_back(bits.to_string());
    result.push_back(bits2.to_string());

    return  result;
}

void mission() {
    auto result = get_ranom_num_128bit();
    for (auto i = 0; i < result.size(); i++) {
        cout << "Random number "<< i<< " :" << result[i] << endl;
    }
    cout << "\n\n";
}
//Random number 0 : 11101101011110111001110000100110101101100000100100011110010111100100010101111101000001001101110101110011001100000000001101110110
//Random number 1 : 10001100111101001010010111001100011111100101011111101100000110011111110101001111101000110001010101000111010101100111001010101000

int main()
{
    auto counter = 1;
    for (auto i = 0; i < counter; i++) {
        mission();
    }
}