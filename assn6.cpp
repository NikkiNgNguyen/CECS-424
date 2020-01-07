/*
Nikki Nguyen
09/16/2019
CECS 424 - 01
Assn 6 - Evolving a Language in and for the Real World C++
*/
#include <iostream>
#include <regex>
using namespace std;

template <class T>
T calculator (T in1, T in2, char* st1)
{
  T out;
  if(strcmp(st1,"+") == 0)
    out = in1 + in2;
  else if(strcmp(st1,"-") == 0)
    out = in1 - in2;
  else if(strcmp(st1,"*") == 0)
    out = in1 * in2;
  else
    out = in1 / in2;
  cout << in1 << " " << st1 << " " << in2 << " = " << out << endl;
  return out;
}

bool regexmatch(string s)
{
    regex e ("\\d*(\\.\\d|\\d\\.)\\d*");
    if (regex_match (s,e))
        return true;
    return false;
}

int main (int argc, char* argv[]) {
  char* point;
  char* input[3];
  int i = 0;
  point = strtok(argv[1]," ");
  while(point != NULL)
  {
    input[i++] = point;
    point = strtok(NULL, " ");
  }
  string st0 = input[0];
  char* st1 = input[1];
  string st2 = input[2];

  if((regexmatch(st0)) || (regexmatch(st2)))
  {
    double in1, in2 = 0.0;
    in1 = stod(input[0]);
    in2 = stod(input[2]);
    calculator(in1, in2, st1);
  }
  else
  {
    int in1, in2, = 0;
    in1 = stoi(input[0]);
    in2 = stoi(input[2]);
    calculator(in1, in2, st1);
  }
  return 0;
}
