#include<iostream>
using namespace std;
int main(){
        int data[10];
        cout<<"Enter the data bits"<<endl;
        cin>>data[0];
        cin>>data[1];
        cin>>data[2];
        cin>>data[4];
        data[3]=data[0]^data[1]^data[2];
        data[5]=data[0]^data[1]^data[4];
        data[6]=data[0]^data[2]^data[4];
        for(int i=0;i<7;i++)
                cout<<data[i];
        int datar[10];
        cout<<endl;
        for(int i=0;i<7;i++)
                cin>>datar[i];
        int c1,c2,c3;
        c1=datar[6]^datar[4]^datar[2]^datar[0];
        c2=datar[5]^datar[4]^datar[1]^datar[0];
        c3=datar[3]^datar[2]^datar[1]^datar[0];
        int c;
        c=c3*4+c2*2+c1;
        if(c==0)
                cout<<"No error"<<endl;
        else
                cout<<"Error at pos"<<c<<endl;
        
        if(datar[7-c]==0)
                datar[7-c]=1;
        else
                datar[7-c]=0;
        cout<<"corrected bits are: ";
        for(int i=0;i<7;i++)
                cout<<datar[i];
}
