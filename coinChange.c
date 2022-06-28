//6
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float v;
    do
    {
        v = get_float("Digite o troco: ");
    }
    while(v<0);
    
    int centavos = round(v * 100);
    
    while (centavos >= 0)    
    {    
        {int moedas = 0;}
        while (centavos >= 50)
        {    
            centavos - 50;
            int moedas =+ 1;
        }
        while (centavos >= 25)
        {
            centavos - 25;
            int moedas=+ 1;
            
        }
        while (centavos >= 10)
        {    
            centavos - 10;
            int moedas =+ 1;
        }
        while (centavos >= 5)
        {
            centavos - 5;
            int moedas =+ 1;
        }
        while (centavos >= 1)
        {
            centavos - 1;
            int moedas =+ 1;
        }
        if (centavos == 0)
        printf("numero de moedas: %i", moedas)
    }
}
