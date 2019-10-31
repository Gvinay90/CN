#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
using namespace std;
int main(){
        string sr,protocol,time,source,destination,info,len;
        int ch;
        int=0
        do{     
                 i=0;
                ifstream file("data.csv");
                cout<<"Enter your choice"<<endl;
                cout<<"1.IP"<<endl;
                cout<<"2.UDP"<<endl;
                cout<<"3.TCP"<<endl;
                cout<<"4.Ethernet"<<endl;
                cout<<"5.Exit"<<endl;
                cin>>ch;
                string pch;
                switch(ch){
                        case 1:
                                pch="ICMPv6";
                                break;
                        case 2:
                                pch="UDP";
                                break;
                        case 3:
                                pch="TCP";
                                break;
                        case 4:
                                pch="ARP";
                                break;
                 }
                 while(file.good()){
                        getline(file,sr,',');
                        getline(file,time,',');
                        getline(file,source,',');
                        getline(file,destination,',');
                        getline(file,protocol,',');
                        getline(file,len,',');
                        getline(file,info,'\n');
                        protocol=string(protocol,1,protocol.length()-2);
                        if(protocol=="Protocol" || protocol==pch){
                                cout<<left<<i++;
                                cout<<setw(12)<<left<<string(time,1,time.length()-2);
                                cout<<setw(30)<<left<<string(source,1,source.length()-2);
                                cout<<setw(30)<<left<<string(destination,1,destination.length()-2);
                                cout<<setw(8)<<left<<protocol;
                                cout<<setw(8)<<left<<string(len,1,len.length()-2);
                                cout<<string(info,1,info.length()-2)<<endl;
                        }
                  }
            file.close();
            }while(ch!=5);
}                    
