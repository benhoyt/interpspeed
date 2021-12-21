// gcc sum.c -O2 && time ./a.out

#include <stdio.h>

void main() {
    long s = 0;
    for (long i = 0; i < 100000000; i++) {
        s += i;
        asm(""); // avoid gcc optimizing away the entire loop
    }
    printf("%ld\n", s);
}