#include <iostream>

void hello();

class MyHello
{
public:
    MyHello(const std::string &name);
    void hello();

private:
    std::string _name;
};