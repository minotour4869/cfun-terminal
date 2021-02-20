/*
    Author: Minotour o(≧▽≦)o
    Date and time: 15:43:03, 15/09/2020
    Note: My code has a lot of useless define, stupid sub-program, and sometimes has lost brain neutron, so if u don't want to get rid of this, pls skip to line 107
*/

/// general library - namespace
#include <bits/stdc++.h>
using namespace std;

/// customize for some special problem
//#define _MULTEST_
#define Mino "TEST"

/// Here is my define god. I recommended you should NOT read it, unless you need to do this.
#pragma region Define_God
/// shorten declare
#define elif else if
#define ll long long
#define pii pair <int, int>
#define pb push_back
#define mp make_pair
#define mii map <int, int>
#define mib map <int, bool>
#define vi vector <int>
#define qi queue <int>
#define fi first
#define se second

/// easier function
#define fvt(x) for (auto &i: x) cout << i << ' ';
#define rvt(x) for (auto &i: x) cin >> i;
#define gl(x) getline (cin, x)
#define resett(x, t) memset(x, t, sizeof(x))

/// constant number
const int maxa = 1e3 + 7;
const int maxb = 1e6 + 7;
const int oo = 1e9 + 7;
const int maxtime = 1000; //with ms

/// FIO - in dev
template <class T>
void fip(T &n)
{
    bool neg = 0;
    register T c = getchar(); 
    n = 0;
    if (c == '-')
    {
        neg = 1; c = getchar();
    }
    for (;(c < 48 || c > 57); c = getchar());
    for (;(c >= 48 && c <= 57); c = getchar()) 
    {
        n = (n << 1) + (n << 3) + c - '0';
    }
    if (neg) n *= -1;
    cin >> ws;
}

// void fop(int n)
// {
    
// }

// common void
void init();
void solve(int test);
void timer();

void init()
{
#ifndef ONLINE_JUDGE
    freopen(Mino".INP", "r", stdin);
    freopen(Mino".OUT", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
}

void timer()
{
    int timer = 1000*clock()/CLOCKS_PER_SEC;
    cout << endl << "Used: " << timer << "ms";
    if (timer > maxtime)
        cout << endl << "TLE";
}
#pragma endregion

int main()
{
    init();
#ifdef _MULTEST_
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) // so i used for because some problem need to print out your test count
        solve(T);
#else
    solve(1);
#endif
#ifndef ONLINE_JUDGE
    timer();
#endif
}

/// End of my fk useless define. Pls take a cup of milktea, and feel free to read my main code:

ll n;

void solve(int test)
{
    cin >> n;
    cout << ((n > 2)? "YES": "NO");
}