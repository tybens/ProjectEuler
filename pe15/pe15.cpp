#include <iostream>
#include <list>
#include <string>
#include "BigInteger.h"

using namespace std;

int main()
{
    const int gridSize = 20;
    BigInteger grid[gridSize+1][gridSize+1];


    for(int i = 0; i < 21; i++) {
        BigInteger one("1");
        grid[i][gridSize] = one;
        grid[gridSize][i] = one;
    }

    for(int i = gridSize; i >= 0; i--) {
        for(int j = gridSize; i >= 0; j--) {
            grid[i][j] = grid[i+1][j].add(grid[i][j+1]);
            cout << grid[i][j].toString() << endl;
        }
    }
    cout << grid[0][0].toString(); // gets too large for C++

    return 0;
}
