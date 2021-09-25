#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <dos.h>
#include <math.h>
#include <time.h>
#include <ctype.h>
#include<GRAPHICS.H>
#include<MARIOBROS.H>
int u[]={77,100,148,100,148,262,244,262,244,165,305,165,305,315,77,315,77,101};
int ni[]={163,100,385,100,385,263,410,263,410,165,481,165,481,316,321,316,321,148,233,148,233,245,163,245,163,100};
int punto[]={410,102,482,102,482,150,410,150,410,102};
int driver = DETECT,modo,codigo;
int poligono [] = {502, 311,120, 311,120, 151,502, 151,502, 311};
int raya [] = {122,279.1, 500,279.1};
int rayaroja [] = {122, 287, 500, 287};
int rayaroja2[] = {120,190,120,190};
int raya2 [] = {120,176, 500, 176};
int tc20 [] = {0,0,1,479,639,479,639,1};
int triangulo [] = {120,233, 184,279, 120,279,120,233};
int cuadrado [] = {119,396,119,448,500,448, 500,396,119,396};
int tri[] = {0,100, 100,100, 50,0};
#define BLINK 128 /* blink */
int maxcolor = 14;
void carga(void);
void logografico(void);
void logo(void)
{
    int figura1=13;
    int figura2=22;
    int figura3=17;
    int figura4=13;
    int figura5=13;
    int figura6=13;
    int figura7=17;
    int figura8=22;
    int figura9=13;

        textcolor(BLUE);
        while(figura1<=24)
        {
            gotoxy(17,figura1);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura1++;
        }

        while(figura2<=24)
        {
            gotoxy(18,figura2);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura2++;
        }

        while(figura3<=24)
        {
            gotoxy(35,figura3);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura3++;
        }

        while(figura4<=20)
        {
            gotoxy(26,figura4);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura4++;
        }

        while(figura5<=24)
        {
            gotoxy(44,figura5);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura5++;
        }

        while(figura6<=15)
        {
            gotoxy(54,figura6);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura6++;
        }

        while(figura7<=24)
        {
            gotoxy(54,figura7);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura7++;
        }

        while(figura8<=24)
        {
            gotoxy(44,figura8);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            figura8++;
        }

        while(figura9<=15)
        {
            gotoxy(28,figura9);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);
            cprintf("%c",219);        
            figura9++;
        }
}

void carga(void)
{

  int a=20,b=0,porcentaje=2;
  system("cls");
  textbackground(BLACK);
  while(b<=49)
    {
    gotoxy(30,15);
    textcolor(CYAN + BLINK);
    cprintf("Cargando, por favor espere");
	gotoxy(a,20);printf("%c",219);delay(200);
	b++;
	a++;
    porcentaje+=2;
    gotoxy(40,23);
    printf("%d %s",porcentaje,"%");
    }
}

void presentacion(void)
{
    FILE *p;
    char ch;
    system("cls");
    p=fopen("AAA.txt","r");

    if(p==NULL)
    {
        printf("Archivo no encontrado");
    }
	else ch=fgetc(p);

    while(ch!=EOF)
    {
		delay(50);
		printf("%c",ch);
		ch=fgetc(p);

    }

    fclose(p);
}

void logogrande(void)
{
    int i=0;
    textbackground(LIGHTGRAY);
    while(i<=3)
    {
    int figura1=3;
    int figura2=12;
    int figura3=7;
    int figura4=3;
    int figura5=3;
    int figura6=3;
    int figura7=7;
    int figura8=12;
    int figura9=3;

       
        clrscr();
        textcolor(BLUE);
            while(figura1<=14)
            {
                delay(5);
                gotoxy(17,figura1);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura1++;
            }
            delay(100);
            while(figura2<=14)
            {
                delay(5);
                gotoxy(18,figura2);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura2++;
            }
            delay(100);
            while(figura3<=14)
            {
                delay(5);
                gotoxy(35,figura3);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura3++;
            }
            delay(100);
            while(figura4<=10)
            {
                delay(5);
                gotoxy(26,figura4);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura4++;
            }
            delay(100);
            while(figura5<=14)
            {
                delay(5);
                gotoxy(44,figura5);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura5++;
            }
            delay(100);
            while(figura6<=5)
            {
                delay(5);
                gotoxy(54,figura6);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura6++;
            }
            delay(100);
            while(figura7<=14)
            {
                delay(5);
                gotoxy(54,figura7);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura7++;
            }
            delay(100);
            while(figura8<=14)
            {
                delay(5);
                gotoxy(44,figura8);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                figura8++;
            }
            delay(100);
            while(figura9<=5)
            {
                delay(5);
                gotoxy(28,figura9);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);
                cprintf("%c",219);        
                figura9++;
            }
        i++;
        delay(300);    
    }






}
void logografico(void)
{
    initgraph(&driver,&modo, "c:\\tc20\\BIN");
    setfillstyle(SOLID_FILL,BLUE);
    fillpoly(9,u);
    fillpoly(13,ni);
    fillpoly(4,punto);



 
}
void prefijos(void)
{
    

    initgraph(&driver,&modo, "c:\\tc20\\BIN");
    cleardevice();

    /* Dibujo */



    setbkcolor(4);
    setcolor(1);

        /* Texto Uni */
    setcolor(8);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(80,77,"Universidad Nacional de Ingenieria");
    delay(120);

    setcolor(WHITE);
	settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(70,70,"Universidad Nacional de Ingenieria");
    delay(120);

  

    /* Bandera Maxi Pali */
    setcolor(14);

    setlinestyle(SOLID_LINE,14,THICK_WIDTH);
    setfillstyle(SOLID_FILL,2);

    drawpoly(5,poligono);
    fillpoly(5,poligono);

    drawpoly(2,raya);
    fillpoly(2,raya);

    drawpoly(2,raya2);
    fillpoly(2,raya2);

    setcolor(14);
    
    setfillstyle(SOLID_FILL,2);
    drawpoly(4,triangulo);
    fillpoly(4,triangulo);

    setcolor(4);

    setlinestyle(SOLID_LINE,4,THICK_WIDTH);
    fillpoly(2,rayaroja);
   

    /* Texto dentro de la bandera */
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 3);
    outtextxy(225,225,"MAXIPALI");

    /* Texto Debajo de la bandera */
    setcolor(WHITE);
    settextstyle (TRIPLEX_FONT  , HORIZ_DIR, 2);
	outtextxy(160,319,"PRECIO BAJO SIEMPRE");

    /* Recuadro TC20 */
    setcolor(WHITE);
    setlinestyle(SOLID_LINE,WHITE,THICK_WIDTH);
    drawpoly(4,tc20);
  
    /* Rectangulo */
  /*  setcolor(WHITE);
    fillpoly(5,cuadrado); */

    /* Texto Enter */
    /* Verde */
    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    /*AZUL */
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");

    
    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");

    
    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");

    
    sleep(1.5);

    setcolor(4);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(90,384,"Presione Enter para Continuar");
    setcolor(WHITE);
    settextstyle (DEFAULT_FONT  , HORIZ_DIR, 2);
	outtextxy(100,389,"Presione Enter para Continuar");

    getch();
    closegraph(); 
    logografico();
    sleep(2);
    closegraph();
    carga();
}