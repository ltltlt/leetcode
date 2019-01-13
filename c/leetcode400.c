#include <math.h>
#include <stdio.h>
#include <assert.h>

int findNthDigit(int n) {
    long lowBound = 0, highBound, p;
    int i=0;
    for (;;) {
        p = pow(10, i);
        highBound = lowBound + (i+1)*9*p;
        if (highBound >= n) break;
        lowBound = highBound;
        i++;
    }
    int offset = n - lowBound - 1;
    int v = offset/(i+1) + pow(10, i);
    int extra = (i+1) - (offset % (i + 1)) - 1;
    return (v / (int)pow(10, extra)) % 10;
}

int main(void) {
    assert(1 == findNthDigit(1000000000));
}