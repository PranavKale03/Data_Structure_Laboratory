#include<iostream>
using namespace std;

class hp
{
   int heap[20],heap1[20],x,n1,i;
   public:
   hp()
   {
    heap[0]=0;  heap1[0]=0;
   }
   void getdata();
   void insert1(int heap[],int);
   void upadjust1(int heap[],int);
   void insert2(int heap1[],int);
   void upadjust2(int heap1[],int);
   void minmax();
};
void hp::getdata()
{
   cout<<"\nEnter the no. of students : ";
   cin>>n1;
   cout<<"\nEnter the marks : ";
   for(i=0;i<n1;i++)
   {   cin>>x;
       insert1(heap,x);
       insert2(heap1,x);
   }
}
void hp::insert1(int heap[20],int x)
{
   int n;
   n=heap[0];
   heap[n+1]=x;
   heap[0]=n+1;

   upadjust1(heap,n+1);
}
void hp::upadjust1(int heap[20],int i)
{
    int temp;
    while(i>1&&heap[i]>heap[i/2])
    {
       temp=heap[i];
       heap[i]=heap[i/2];
       heap[i/2]=temp;
       i=i/2;
    }
}
void hp::insert2(int heap1[20],int x)
{
   int n;
   n=heap1[0];
   heap1[n+1]=x;
   heap1[0]=n+1;

   upadjust2(heap1,n+1);
}
void hp::upadjust2(int heap1[20],int i)
{
    int temp1;
    while(i>1&&heap1[i]<heap1[i/2])
    {
       temp1=heap1[i];
       heap1[i]=heap1[i/2];
       heap1[i/2]=temp1;
       i=i/2;
    }
}
void hp::minmax()
{
   cout<<"\nMaximum marks obtained : "<<heap[1];
   cout<<"\nMinimum marks obtained : "<<heap1[1];
}
int main()
{
  hp h;
  h.getdata();
  h.minmax();
  return 0;
}
