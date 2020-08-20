#include "hello.h"

void hello()
{
    std::cout << "Hello World!" << std::endl;
}

MyHello::MyHello(const std::string &name) : _name(name)
{
}

void MyHello::hello()
{
    std::cout << "Hello "
              << _name << std::endl;
}