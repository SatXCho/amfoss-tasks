#include <stdio.h>
#include <cs50.h>

int t = 1;
int height(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

int main(void)
{
    int p = height();
    for (int i = 0; i < p; i++)
        {
              for (int k=p-i;;k--){
                                      printf(" ");
                                      if (k==1)
                                      break;
                                     }
            for (int j = 0; j < i; j++)
                {
                  
                    printf("#");

                }
        printf("\n");
        }
}
