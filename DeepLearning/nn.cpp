#include <iostream>

int main() {
    int input[] = {1, 2, 3, 4};
    float weight[] = {1.5, 2.5, 3.5, 4.5};
    int bias = 2;
    float output = 0;

    // Perform the weighted sum
    for (int i = 0; i < sizeof(input) / sizeof(input[0]); i++) {
        output += input[i] * weight[i];
    }

    // Add the bias
    output += bias;

    std::cout << output << std::endl;
    return 0;
}
