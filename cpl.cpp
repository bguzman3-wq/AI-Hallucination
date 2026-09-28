#include <iostream>
using namespace std;


// CPP10
int* getValue() {
    int x = 10;
    return &x;
}


// CPP09
struct Widget {
    Widget() {
        cout << "Default ";
    }

    Widget(const Widget&) {
        cout << "Copy ";
    }

    Widget(Widget&&) noexcept {
        cout << "Move ";
    }
};

Widget make() {
    return Widget();
}


// CPP05
class Data {
public:
    int* value;

    Data(int v) {
        value = new int(v);
    }

    ~Data() {
        delete value;
    }
};


// CPP07
void change(int a, int& b) {
    a = 50;
    b = 100;
}


// CPP08
struct Tracker {
    int id;

    Tracker(int i) : id(i) {
        cout << "Ctor" << id << " ";
    }

    Tracker(const Tracker& other) : id(other.id) {
        cout << "Copy" << id << " ";
    }

    ~Tracker() {
        cout << "Dtor" << id << " ";
    }
};

void byValue(Tracker t) {
    cout << "In" << t.id << " ";
}


int main() {


    // CPP05
    cout << "\n[CPP05] Shallow Copy / Double Delete" << endl;
    cout << "----------------------------------------" << endl;

    Data a(10);
    Data b = a;

    cout << *a.value << " " << *b.value << endl;


    // CPP06
    cout << "\n[CPP06] Out of Bounds Array Access" << endl;
    cout << "----------------------------------------" << endl;

    int arr[3] = {10, 20, 30};

    cout << arr[3] << endl;


    // CPP07
    cout << "\n[CPP07] Pass by Value / Reference" << endl;
    cout << "----------------------------------------" << endl;

    int x = 10;
    int y = 20;

    change(x, y);

    cout << x << " " << y << endl;


    // CPP08
    cout << "\n[CPP08] Constructor / Destructor Trace" << endl;
    cout << "----------------------------------------" << endl;

    Tracker a2(1);

    byValue(a2);

    cout << "End" << endl;


    // CPP09
    cout << "\n[CPP09] C++17 Copy Elision" << endl;
    cout << "----------------------------------------" << endl;

    Widget w = make();

    cout << endl;


    // CPP10
    cout << "\n[CPP10] Dangling Pointer" << endl;
    cout << "----------------------------------------" << endl;

    int* ptr = getValue();

    cout << *ptr << endl;


    cout << "\n========================================" << endl;
    cout << "VERIFICATION COMPLETE" << endl;
    cout << "========================================" << endl;

    return 0;
}