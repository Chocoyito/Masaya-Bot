#define ENTER 13
#define ESPACIO 32
#define User "admin"
#define Pass "12345"
#define Longitud 10

int intento = 3;

void credenciales()
{
    char Username[Longitud+1];
    char Password[Longitud+1];
    char caracter;
    int i = 0, p;
    int long1;
    int ingreso = 0;

    do
    {
        i = 0;
        system("cls");
        fflush(stdin);

		interfaz();

        gotoxy(34,4);textcolor(YELLOW);
        cprintf("CREDENCIALES");
		gotoxy(28,5);textcolor(WHITE);
        cprintf("Ingrese sus credenciales");
		gotoxy(29,6);
		cprintf("Intentos permitidos: %i", intento);
		gotoxy(19,8);
        cprintf("Usuario: ");

        switch (getch())
        {
            case ENTER:
                goto intento;
            case ESPACIO:
                goto intento;
            default:

                gets(Username);
            break;
        }

        long1 = strlen(Username);
        if (long1 > 10){
            textcolor(RED);gotoxy(28,10);
            cprintf("(!) El usuario es incorrecto.\n");
			gotoxy(31,11);
			cprintf("(!) Exceso de caracteres.");
            getch();
            goto intento;
        }

        gotoxy(19,10);
        cprintf("Ingrese la clave: ");
	
        switch (getch())
            {
             case ENTER:
                 goto intento;
             case ESPACIO:
                 goto intento;
             default:
                 while(caracter = getch())
                 if(caracter == 13){
                     Password[i] = '\0';
                     break;
                 }else if(caracter == 8){
                    if(i > 0){
                         i--;
                         printf("\b \b");
                    }
                 }else{
                    if(i < Longitud){
                     printf("*");
                     Password[i] = caracter;
                     i++;
                    }
                 }
             break;
            }

		for (p = 0; p < 3 ; p++){
			textcolor(YELLOW);
			gotoxy(34,13);
			cprintf("Verificando");
			gotoxy(45+p,13);
			cprintf(".");
			delay(800);
		}

        if (strcmp(Username,User) == 0 && strcmp(Password,Pass) == 0){
            ingreso = 1;
        }else{

            if(strcmp(Username,User) != 0){
                textcolor(RED);
				gotoxy(25,15);
                cprintf("(!) El usuario es incorrecto.\n");
                getch();
            }
            if(strcmp(Password,Pass) != 0){
                textcolor(RED);
				gotoxy(26,16);
				cprintf("(!) La clave es incorrecta.\n");
				getch();
            }

            intento:
            intento--;

            if (intento == 0){
				textcolor(RED+BLINK);gotoxy(21,17);
                cprintf("(!) Fallaste: Credenciales incorrectas.");
				gotoxy(28,18);
                cprintf("(!) Bloqueando acceso.");
				getch();
				pantallasalida();
            }
        }

    } while (intento > 0 && ingreso != 1);

	textcolor(GREEN+BLINK);
	gotoxy(32,15);
	cprintf("ACCESO PERMITIDO");
	delay(1000);
}