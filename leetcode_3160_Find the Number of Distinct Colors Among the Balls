#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Final Approach: Count distinct colors correctly after each query.
// We use ballColor to record each ball's current color and colorCount to track the frequency of each color.
// For each query, if the ball was previously colored, we decrement the old color count and remove it if necessary.
// Then, we update the ball's color and increment the new color count, appending the current number of distinct colors.
class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int, int> ballColor;  // ball index -> current color
        unordered_map<int, int> colorCount;   // color -> frequency
        vector<int> result;
        
        for (auto &q : queries) {
            int ball = q[0], newColor = q[1];
            
            // If this ball was colored before, update the count for its old color.
            if (ballColor.find(ball) != ballColor.end()) {
                int oldColor = ballColor[ball];
                if (oldColor == newColor) {
                    result.push_back(colorCount.size());
                    continue;
                }
                colorCount[oldColor]--;
                if (colorCount[oldColor] == 0)
                    colorCount.erase(oldColor);
            }
            
            // Assign the new color to the ball.
            ballColor[ball] = newColor;
            colorCount[newColor]++;
            
            // The number of distinct colors is the size of the colorCount map.
            result.push_back(colorCount.size());
        }
        return result;
    }
};

// Use the following main() function only if your environment does not already provide one.
// To avoid conflicts, define the macro STANDALONE when compiling this file standalone.
// For example: g++ -DSTANDALONE solution.cpp
#ifdef STANDALONE
int main() {
    Solution sol;
    int limit = 4;
    vector<vector<int>> queries = { {1, 4}, {2, 5}, {1, 3}, {3, 4} };

    vector<int> output = sol.queryResults(limit, queries);
    cout << "Final Output: ";
    for (int num : output)
        cout << num << " ";
    cout << endl;
    
    return 0;
}
#endif
