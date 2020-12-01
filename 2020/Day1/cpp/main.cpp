#include "iostream"
#include "fstream"

using namespace std;

int main() {
  fstream file("../input.txt");

  int nums[200];

  for (int i = 0; i < 200; i++) {
    file >> nums[i];
  }

  for (int i = 0; i < 200; i++) {
    for (int j = 0; j< 200; j++) {
      if (nums[i] + nums[j] == 2020) cout << "Two: " << nums[i] * nums[j] << endl;

      for (int l = 0; l< 200; l++) {
        if (nums[i] + nums[j] + nums[l] == 2020) cout << "Three: " << nums[i] * nums[j] * nums[l] << endl;
      }
    }
  }
  return 0;
}
