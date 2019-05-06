
#include <iostream>
#include "complex.h"

complex::complex(double r, double j) : r(r), j(j) {}

complex complex::operator+(const complex &o) const 
{
    return complex(o.r + r, o.j + j);
}

complex complex::operator+(double n) const 
{
    return complex(n + r, j);
}

complex complex::operator-(const complex &o) const 
{
    return complex(r - o.r, j - o.j);
}

complex complex::operator-(double n) const 
{
    return complex(r - n, j);
}

complex complex::operator*(const complex &o) const 
{
    return complex(((o.r * r) - (o.j * j)), ((o.j * r) + (o.r * j)));
}

complex complex::operator*(double n) const 
{
    return complex(n * r, n * j);
}

complex complex::operator/(const complex &o) const 
{
    return complex((o.r * r + o.j * j) / (o.r*o.r + o.j*o.j), (o.r * j - o.j * r ) / (o.r*o.r + o.j*o.j));
}

complex complex::operator/(double n) const 
{
    return complex(r / n, j / n);
}

complex operator+(double n, const complex &o) 
{
    return o + n;
}

complex operator-(double n, const complex &o) 
{
    return complex(n - o.r, 0 - o.j);
}

complex operator*(double n, const complex &o) 
{
    return o * n;
}

complex operator/(double n, const complex &o) 
{
    return complex(n / o.r, 0 / o.j);
}

ostream &operator<<(ostream &out, const complex &o) 
{
    out << '(' << o.r << ") + (" << o.j << ")i";
    return out;
}
