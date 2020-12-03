#include "iostream"
#include "fstream"
#include "string"

using namespace std;

int main() {
  fstream file("../input.txt");

  unsigned int total[5] = {0};

  string temp;
  file >> temp;

  unsigned int i = 0;

  while (!file.eof()) {
    i++;
    string data;
    file >> data;

    if (data[(i) % data.length()] == '#') total[0]++;
    if (data[(i*3)%data.length()] == '#') total[1]++;
    if (data[(i*5)%data.length()] == '#') total[2]++;
    if (data[(i*7)%data.length()] == '#') total[3]++;

    if (i%2 == 0) if (data[((i/2))%data.length()] == '#') total[4]++;
  }

  cout << "1x1: " << total[0] << endl;
  cout << "3x1: " << total[1] << endl;
  cout << "5x1: " << total[2] << endl;
  cout << "7x1: " << total[3] << endl;
  cout << "1x2: " << total[4] << endl;

  cout << endl;

  unsigned int product = total[0] * total[1] * total[2] * total[3] * total[4];

  cout << "Total product: " << product << endl;

  return 0;
}
