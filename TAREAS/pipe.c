#include <tupapa.h>
#include <TERM.H>                                                                               c
void preijos (void);
#define ARRIBA 72 
#define ABAJO 80
char tecla;
int x,i=2;
void main () 
{
   prefijos (); 
   system("cls");
    textcolor(RED);
    cprintf("\nAgregar Trabajador");
    printf("\nEliminar Trabajador\n");
    printf("Salir");
    menuprincipal:
    tecla = getch();
    if (tecla==80 | tecla==72)
    {
        switch (tecla)
            {
            case ABAJO:
                 system("cls");
                 textcolor(RED);
                 printf("\nAgregar Trabajador\n");
                 cprintf("Eliminar Trabajador");
                 printf("\nSalir");
                 getch();
                 system("cls");
                 goto menuprincipal;
                break;
            case ARRIBA:
                 system("cls");
                 textcolor(RED);
                 printf("\nAgregar Trabajador\n");
                 printf("Eliminar Trabajador\n");
                 cprintf("Salir");
                 getch();
                 system("cls");
                 goto menuprincipal;
                break;
            default:
                break;
            }
    }    
    else
    {
        goto menuprincipal;
    }

}
    



