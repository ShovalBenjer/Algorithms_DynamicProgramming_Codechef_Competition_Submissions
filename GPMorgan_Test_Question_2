#include <bits/stdc++.h>
using namespace std;

void closestNumbers(vector<int> numbers) {
    // Step 1: Sort the array
    sort(numbers.begin(), numbers.end());

    // Step 2: Find the minimum absolute difference
    int min_diff = INT_MAX;
    for (size_t i = 1; i < numbers.size(); i++) {
        int diff = abs(numbers[i] - numbers[i - 1]);
        min_diff = min(min_diff, diff);
    }

    // Step 3: Collect and print all pairs with the minimum difference
    for (size_t i = 1; i < numbers.size(); i++) {
        int diff = abs(numbers[i] - numbers[i - 1]);
        if (diff == min_diff) {
            cout << numbers[i - 1] << " " << numbers[i] << endl;
        }
    }
}
