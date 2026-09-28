#include <iostream>
using namespace std;

int* getValue() {
    int x = 10;

    return &x;
}

struct Widget {
    Widget() {
    std::cout << "Default ";
    }

    Widget(const Widget&) {
        std::cout << "Copy ";
    }

    Widget(Widget&&) noexcept {
        std::cout << "Move ";
    }
};

Widget make() {
    return Widget();
}

class Data{
    public:
        int* value;
        Data(int v){
            value = new int(v);
        }
        ~Data(){
            delete value;
        }
};

void change(int a, int& b) {
    a = 50;
    b = 100;
}   

struct Tracker {
    int id;

    Tracker(int i) : id(i) {
        std::cout << "Ctor" << id << " ";
    }

    Tracker(const Tracker& other) : id(other.id) {
        std::cout << "Copy" << id << " ";
    }

    ~Tracker() {
        std::cout << "Dtor" << id << " ";
    }
};

void byValue(Tracker t) {
    std::cout << "In" << t.id << " ";
}

int main(){
    //CPP05
    Data a(10);
    Data b = a;
    std::cout << *a.value << " " << *b.value << std::endl;

    //CPP06
    int arr[3] = {10, 20, 30};
    std::cout << arr[3] << std::endl;

    //CPP07
    int x = 10;
    int y = 20;
    change(x, y);
    std::cout << x << " " << y << std::endl;

    //CPP08
    Tracker a2(1);
    byValue(a2);
    std::cout << "End ";

    //CPP09
    Widget w = make();
    return 0;

    //CPP10
    int* ptr = getValue();

    std::cout << *ptr << std::endl;
}   