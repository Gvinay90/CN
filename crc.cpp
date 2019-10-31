#include<iostream>
using namespace std;
int main(){
        int i,j,k,fs,gs;
        int f[20],g[20];
        cout<<"Enter the frame size\n";
        cin>>fs;
        cout<<"Enter frame\n";
        for(i=0;i<fs;i++){
                cin>>f[i];
        }
        cout<<"Enter the generator size\n";
        cin>>gs;
        cout<<"Enter generator\n";
        for(i=0;i<gs;i++)
                cin>>g[i];
        for(i=fs;i<fs+gs-1;i++)
                f[i]=0;
        int temp[20];        
        for(i=0;i<fs+gs-1;i++)
                cout<<f[i];
        cout<<"\n";
        for(i=0;i<fs+gs-1;i++)
                temp[i]=f[i];       
        for(i=0;i<fs;i++){
                j=0;
                k=i;
                if(temp[k]>=g[j]){
                        for(j=0,k=i;j<gs;k++,j++){
                                if((temp[k]==1 && g[j]==1) || (temp[k]==0 && g[j]==0))
                                        temp[k]=0;
                                else
                                        temp[k]=1;
                         }
                }
         }
        // for(i=0;i<fs+gs-1;i++)
          //      cout<<temp[i];
          int crc[5];
        for(i=fs,j=0;i<fs+gs-1;i++,j++)
                crc[j]=temp[i];
       //  for(i=0;i<3;i++)
        // cout<<crc[i];
        for(i=fs,j=0;i<fs+gs-1;i++,j++)
                f[i]=crc[j];
        // for(i=0;i<fs+gs-1;i++)
          //      cout<<f[i];
        for(i=0;i<fs;i++){
                j=0;
                k=i;
                if(f[k]>=g[j]){
                        for(j=0,k=i;j<gs;j++,k++){
                                if((f[k]==1 && g[j]==1) || (f[k]==0 && g[j]==0))
                                        f[k]=0;
                                else
                                        f[k]=1;
                         }
                }
         }
         int flag=0;
          for(i=0;i<fs+gs-1;i++){
                if(f[i]==0)
                        flag=1;
                else{
                        flag=0;
                        break;
                    }
           }
           
           if(flag=1)
                cout<<"\nNo error found";
           else
                cout<<"\nError found";
                
                
                
                
}
