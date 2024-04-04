#include <iostream>

using namespace std;

int main(){
    int odleglosc;
    int osoby;
    int srspalanie=8;
    int spalanie;
    int tankowanie;
    int paliwo;
    float cena=5;
    float cenaspalanie;

    cout<<"podaj odleglosc"<<endl;
    cin>>odleglosc;
    cout<<"podaj liczbe osob"<<endl;
    cin>>osoby;
    cout<<"podaj ilosc paliwa"<<endl;
    cin>>paliwo;

    spalanie=(srspalanie*odleglosc)/100;
    tankowanie=(paliwo/40)+1;
    cenaspalanie=cena*srspalanie;

    cout<<"odleglosc "<<odleglosc<<"km"<<endl;
    cout<<"osoby "<<osoby<<endl;
    cout<<"spalanie "<<spalanie<<"l"<<endl;
    cout<<"ilosc tankowan "<<tankowanie<<"l"<<endl;
    cout<<"cena "<<cena<<"zl"<<endl;


	return 0;
}
