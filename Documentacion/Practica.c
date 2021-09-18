#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

#define FILA 4
#define COLU 5


void main()
{
	int array[FILA][COLU];
	int i,k,num,new,cont=0;
	clrscr();
	
	for(i=0;i<FILA;i++)
	{
		clrscr();
		
		for(k=0;k<COLU;k++)
		{
		
			printf("Elemento [%d][%d]: ",i,k);
			scanf("%d",&array[i][k]);
			
		}
		
		printf("\n");
	}
	
	
	
	do
	{
		clrscr();
		for(i=0;i<FILA;i++)
		{
			
			for(k=0;k<COLU;k++)
			{
			
				printf(" %d ",array[i][k]);
				
			}
			
			printf("\n");
		}
		
		printf("\nIngrese Dato a Buscar: ");
		scanf("%d",&num);
		
		clrscr();
		
		printf("Resultados de Busqueda\n\n");
		
		for(i=0;i<FILA;i++)
		{
			
			for(k=0;k<COLU;k++)
			{
				if(array[i][k]==num)
				{
					textcolor(GREEN);
					cprintf(" %d ",array[i][k]);
					cont++;
				}else{
					printf(" %d ",array[i][k]);
				}
			}
			
			printf("\n");
		}
		if(cont>0)
		{
			printf("\nIngrese el numero nuevo a sustituir: ");
			scanf("%d",&new);
			for(i=0;i<FILA;i++)
			{
				
				for(k=0;k<COLU;k++)
				{
					if(array[i][k]==num)
					{
						textcolor(BLUE);
						cprintf(" %d ",new);
						cont++;
					}else{
						printf(" %d ",array[i][k]);
					}
				}
				
				printf("\n");
			}
			
		}else{
			printf("\nNumero No Encontrado\n\n");
		}
		
		gotoxy(50,23);
		printf("Designed By Rafael Poveda");
		
		getch();
	}while(cont==0);
	

}