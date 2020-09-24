// Code Adder.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    int start = 0;
    int end = 0;
    int i = 0;
    string base;
    string indicator;

    cout << "Base name" << endl;
    cin >> base;
    cout << "Indicator" << endl;
    cin >> indicator;
    cout << "The beginning question number" << endl;
    cin >> start;
    cout << "The last question number" << endl;
    cin >> end;


    for (int x = start; x <= end; x++) {
        string fileName = base + to_string(x) + ".pg";
        ifstream inFile(fileName);

        string line;
        vector<string> vLines;
        bool flag = true;
        int count = 0;
        
        if (inFile) {
            while (getline(inFile, line)) {
                vLines.push_back(line);
                if (flag == true) {
                    count++;
                    if (line == indicator) {
                        flag = false;
                    }
                }
            }

            inFile.close();

            ofstream outFile(fileName);

            char buff[1024] = "TEXT(beginproblem());";

            for (i = 0; i < vLines.size(); i++) {
                if (i == count) {
                    outFile << "\n";
                    outFile << buff << endl;
                    outFile << "\n";
                    cout << "Text Added to " << fileName << endl;
                }
                else {
                    outFile << vLines[i] << endl;
                }
            }
            outFile.close();
        }
        else {
            cout << fileName << " could not be opened/found" << endl;
        }
    }


    return 0;
}



// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
