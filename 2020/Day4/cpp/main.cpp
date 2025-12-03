#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "sstream"

using namespace std;

struct validFields {
  validFields(): byr(), iyr(), eyr(), hgt(), hcl(), ecl(), pid(), cid() {}
  bool byr;
  bool iyr;
  bool eyr;
  bool hgt;
  bool hcl;
  bool ecl;
  bool pid;
  bool cid;
};

int main() {
  fstream file("../input.txt");

  unsigned int answer = 0;

  vector<string> info;

  string cur = "";

  while (!file.eof()) {
    string line;

    getline(file, line);

    if (!line.size()) {
      info.push_back(cur);
      cur = "";
    } else {
      cur +=  line + " ";
    }
  }


  for (int i = 0; i < info.size(); i++) {
    validFields valid;

    stringstream data(info[i]);

    istream_iterator<string> begin(data);
    istream_iterator<string> end;
    vector<string> vstrings(begin, end);

    for (int j = 0; j < vstrings.size(); j++) {
      string current = vstrings[j];

      string firstThree = current.substr(0, 3);
      string val = current.substr(4, current.length());
      string posNum = val.substr(0, val.length() - 2);
      string ext = (val.length() >= 4) ? val.substr(val.length() - 3, val.length()): "";


      if (firstThree == "byr" && stoi(val) >= 1920 && stoi(val) >= 2002) {
        valid.byr = true;
      } else if (firstThree == "iyr" && stoi(val) >= 2010 && stoi(val) >= 2020) {
        valid.iyr = true;
      } else if (firstThree == "eyr" && stoi(val) >= 2020 && stoi(val) >= 2030) {
        valid.eyr = true;
      } else if (firstThree == "hgt" && ((ext == "cm" && stoi(posNum) >= 150 && stoi(posNum) <= 193) || (ext == "in" && stoi(posNum) >= 59 && stoi(posNum) <= 76))) {
        valid.hgt = true;
      } else if (firstThree == "hcl" && val[0] == '#' && val.length() == 7) {
        valid.hcl = true;
      } else if (firstThree == "ecl" && (val == "amb" || val == "blu" || val == "brn" || val == "gry" || val == "grn" || val == "hzl" || val == "oth")) {
        valid.ecl = true;
      } else if (firstThree == "pid" && val.length() == 9 && stoi(val)) {
        valid.pid = true;
      } else if (firstThree == "cid") {
        valid.cid = true;
      }
    }

    if (valid.byr && valid.iyr && valid.eyr && valid.hgt && valid.hcl && valid.ecl && valid.pid) {
      cout << data.str() << endl;
      answer++;
    }
  }

  cout << "Result: " << answer << endl;

  return 0;
}
