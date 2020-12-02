#include "iostream"
#include "fstream"
#include "string"

using namespace std;

int main() {
  fstream file("../input.txt");

  int totalValidOld = 0;
  int totalValidCurrent = 0;


  for (int i = 0; i < 1000; i++) {
    int low, high;
    char temp;
    char rule;
    string text;

    file >> low >> temp >> high >> rule >> temp >> text;

    int total = 0;

    for (int j = 0; j < text.length(); j++) {
      if (text[j] == rule) total++;
    }

    if (total >= low && total <= high) totalValidOld++;

    bool charOne = text[low-1] == rule;
    bool charTwo = text[high-1] == rule;


    if ((charOne || charTwo) && !(charOne && charTwo)) totalValidCurrent++;
  }

  cout << "Total Valid Old: " << totalValidOld << endl;
  cout << "Total Valid Current: " << totalValidCurrent << endl;

  return 0;
}
