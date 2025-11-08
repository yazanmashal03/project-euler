#include <iostream>

void printHelloWorld(const std::string& message = "Hello World") {
    std::cout << message << std::endl;
}

int main() {
    printHelloWorld();  // prints "Hello World"
    printHelloWorld("Hi there!");  // prints "Hi there!"
    return 0;
}