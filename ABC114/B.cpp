#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)


typedef  long long ll;
int main(){

    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    string ans = "IMPOSSIBLE";
    int N,M; cin >> N >> M;
    vector <bool> start_next(N,false);
    vector <bool> end_prev(N,false);
    REP(i,M){
        int a,b;
        cin >> a >> b;
        a--;b--;
        if(a==0){
            start_next[b]=true;
        }
        if(b==0){
            start_next[a]=true;
        }
        if(a==N-1){
            end_prev[b]=true;
        }
        if(b==N-1){
            end_prev[a]=true;
        }
    }
    REP(i,N){
        if(start_next[i]==true && end_prev[i]==true){
            ans = "POSSIBLE";
        }
    }
    cout << ans <<endl;
    
}