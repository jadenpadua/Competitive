#include <iostream>
using namespace std;
int a[100],n=0;
 
int main() 
{
	while(cin>>a[n++]);
        cout << a[n];
	sort(a,a+n);
	cout<<a[1];

	for(int i=2;i<n;i++)
		cout<<'+'<<a[i];
}