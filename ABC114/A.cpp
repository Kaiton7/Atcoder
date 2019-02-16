#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
using namespace std;
 
int n, k;
typedef  long long ll;
int main(){

    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    string s;
    cin >> s;
    //printf("%s", s.c_str());
    if(s[0] == s[2]){
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;

}