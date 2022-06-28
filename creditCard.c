//6
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long cartao;
    do
    {    
        cartao = get_long("Digite o numero do cartao: ");
    }
    while (cartao < 0);
    
   
    int ult_2 = cartao % 100; // pega os 2 ultimos digitos do cartao
    int n15 = (ult_2 / 10) * 2; // pega o digito 15 do cartao e mult por 2
    int n13 = ((cartao % 10000) / 1000) * 2; // pega o digito 13 do cartao e mult por 2
    int n11 = ((cartao % 1000000) / 100000) * 2;
    int n09 = ((cartao % 100000000) / 10000000) * 2;
    int n07 = ((cartao % 10000000000) / 1000000000) * 2;
    int n05 = ((cartao % 1000000000000) / 100000000000) * 2;
    int n03 = ((cartao % 100000000000000) / 10000000000000) * 2;
    int n01 = ((cartao % 10000000000000000) / 1000000000000000) * 2;
    
    n15 = (n15 % 100) / 10 + (n15 % 10); // separa digitos e soma caso a mult seja um numero de dois digitos
    n13 = (n13 % 100) / 10 + (n13 % 10);
    n11 = (n11 % 100) / 10 + (n11 % 10);
    n09 = (n09 % 100) / 10 + (n09 % 10);
    n07 = (n07 % 100) / 10 + (n07 % 10);
    n05 = (n05 % 100) / 10 + (n05 % 10);
    n03 = (n03 % 100) / 10 + (n03 % 10);
    n01 = (n01 % 100) / 10 + (n01 % 10);
    
    int soma = n15 + n13 + n11 + n09 + n07 + n05 + n03 + n01;
   
    
    int n1_n2 = ((cartao % 1000000000000000) / 10000000000000);
    int x01 = ((cartao % 10000000000000000) / 1000000000000000);
    int x02 = ((cartao % 1000000000000000) / 100000000000000);
    int x04 = ((cartao % 10000000000000) / 1000000000000);
    int x06 = ((cartao % 100000000000) / 10000000000);
    int x08 = ((cartao % 1000000000) / 100000000);
    int x10 = ((cartao % 10000000) / 1000000);
    int x12 = ((cartao % 100000) / 10000);
    int x14 = ((cartao % 1000) / 100);
    int x16 = (cartao % 10);

    int soma2 = soma + x02 + x04 + x06 + x08 + x10 + x12 + x14 + x16;

    
    if (soma2 % 10 == 0)
        printf("Cartao valido.\n");
    else
        printf("Cartao invalido.\n");
    
    if (n1_n2 == 37)
        printf("American Express.\n");
    else if (n1_n2 == 34)
        printf("American Express.\n");
    else if (x01 == 4)
        printf("Visa.\n");
    else if (n1_n2 == 51)
        printf("MasterCard\n");
    else if (n1_n2 == 52)
        printf("MasterCard\n");
    else if (n1_n2 == 53)
        printf("MasterCard\n");
    else if (n1_n2 == 54)
        printf("MasterCard\n");
    else if (n1_n2 == 55)
        printf("MasterCard\n");
}
