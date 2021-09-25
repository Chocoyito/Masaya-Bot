#include <conio.h>
#include <stdlib.h>
#include <dos.h>
#include <tupapa.h>
void muneco1(void);
void muneco2(void);
void muneco3(void);
void main(void) /*Programa principal*/
{
  initgraph(&driver, &modo, "c:\\TC20\\BIN"); /*Inicio del modo grafico*/
  cleardevice();                              

  setbkcolor(BLUE);

  setcolor(LIGHTCYAN);
  setfillstyle(1, WHITE);
  /*Caja Exterior */
  rectangle(11, 10, 626, 459);
  floodfill(21, 71,LIGHTCYAN);

  setcolor(LIGHTCYAN);
  setfillstyle(1, LIGHTGRAY);
  /*Caja De los muñecos */
  rectangle(34, 35, 603, 357);
  floodfill(281, 187, LIGHTCYAN);

  setcolor(BLUE);
  outtextxy(200, 20, "Universidad Nacional De Ingenieria");

  setcolor(LIGHTCYAN);
  /*MUÑECO 1*/
  rectangle(112, 387, 228, 432);

  setcolor(LIGHTBLUE);
  outtextxy(145, 407, "JOSE");
  setcolor(LIGHTCYAN);
  outtextxy(145, 407, "J");

  setcolor(LIGHTCYAN);
  /*MUÑECO 3*/
  rectangle(412, 387, 528, 432);

  setcolor(LIGHTBLUE);
  outtextxy(435, 406, "LEONEL");
  setcolor(GREEN);
  outtextxy(435, 406, "L");
  setcolor(LIGHTBLUE);


  /*Muñeco 2*/
  setfillstyle(1, WHITE);
  bar(261, 387, 375, 432);

  setcolor(LIGHTBLUE);
  outtextxy(295, 407, "EDUARDO");
  setcolor(RED);
  outtextxy(295, 407, "E");

  setcolor(LIGHTCYAN);
  line(253, 379, 381, 379);
  line(253, 379, 253, 438);
  setcolor(BLUE);
  line(253, 438, 381, 438);
  line(381, 379, 381, 438);
  getch();
  sleep(1);

  muneco1();
  muneco2();
  muneco3();
}

void muneco2(void)
{

  /* Muñeco del centro */
  setcolor(BROWN);
  setfillstyle(SOLID_FILL, BROWN);
  rectangle(290, 111, 355, 169);
  floodfill(291, 112, BROWN);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  rectangle(283, 85, 363, 109);
  floodfill(284, 86, WHITE);

  setcolor(BLUE);
  setfillstyle(SOLID_FILL, BLUE);
  fillpoly(5, cuerpo);

  setcolor(BROWN);
  setfillstyle(SOLID_FILL, BROWN);
  fillpoly(5, cuello);

  setcolor(BROWN);
  setfillstyle(SOLID_FILL, BROWN);
  fillpoly(5, cuello1);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, ojo1);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, ojo);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, bocacentro);

  setcolor(LIGHTCYAN);
  setfillstyle(SOLID_FILL, LIGHTCYAN);
  fillpoly(5, pupila);

  setcolor(LIGHTCYAN);
  setfillstyle(SOLID_FILL, LIGHTCYAN);
  fillpoly(5, pupila2);
}
void muneco1(void)
{
  /* Muñeco izquierda */
  setcolor(BROWN);
  setfillstyle(SOLID_FILL, BROWN);
  fillpoly(12, cabezaizq);

  setfillstyle(SOLID_FILL, 8);
  setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
  fillpoly(5, ojoiqz1);

  setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
  fillpoly(5, ojo2);

  setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, boca);

  setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
  circle(93, 108, 3);
  setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
  circle(132, 109, 3);

  setcolor(BLUE);
  rectangle(82, 176, 98, 191);
  setfillstyle(SOLID_FILL, BLUE);
  floodfill(90, 180, BLUE);

  setcolor(BLUE);
  rectangle(146, 176, 131, 192);
  setfillstyle(SOLID_FILL, BLUE);
  floodfill(134, 180, BLUE);
  /* flood fill funcional */
  setcolor(YELLOW);
  rectangle(50, 192, 178, 239);
  setfillstyle(SOLID_FILL, YELLOW);
  floodfill(70, 210, YELLOW);

  setcolor(LIGHTMAGENTA);
  rectangle(50, 67, 177, 79);
  setfillstyle(SOLID_FILL, LIGHTMAGENTA);
  floodfill(51, 68, LIGHTMAGENTA);

  setcolor(LIGHTMAGENTA);
  rectangle(65, 48, 162, 67);
  setfillstyle(SOLID_FILL, LIGHTMAGENTA);
  floodfill(66, 49, LIGHTMAGENTA);
}

void muneco3(void)
{
  /* Dibujo derecho */
  setcolor(BROWN);
  setfillstyle(SOLID_FILL, BROWN);
  fillpoly(5, mechal1);
  fillpoly(5, mechal2);
  fillpoly(5, mechal3);
  fillpoly(5, mechal4);
  fillpoly(5, mechal5);
  fillpoly(5, mechal6);
  fillpoly(5, mechal7);
  fillpoly(5, mechal8);

  setcolor(YELLOW);
  setfillstyle(SOLID_FILL, YELLOW);
  fillpoly(5, gorra1);
  fillpoly(5, gorra2);
  fillpoly(5, gorra3);
  fillpoly(5, gorra4);
  fillpoly(5, gorra5);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, jicara);
  fillpoly(5, jicara2);

  setcolor(LIGHTRED);
  setfillstyle(SOLID_FILL, LIGHTRED);
  fillpoly(5, tapas);

  setcolor(BLUE);
  setfillstyle(SOLID_FILL, BLUE);
  fillpoly(5, ojoder);

  setcolor(BLUE);
  setfillstyle(SOLID_FILL, BLUE);
  fillpoly(5, ojoder2);

  setcolor(WHITE);
  setfillstyle(SOLID_FILL, WHITE);
  fillpoly(5, cuelloizq);
  fillpoly(5, cuelloizq2);

  setcolor(CYAN);
  setfillstyle(SOLID_FILL, CYAN);
  fillpoly(5, camisafrente);
  fillpoly(5, camisafrente2);

  setcolor(LIGHTBLUE);
  setfillstyle(SOLID_FILL, LIGHTBLUE);
  fillpoly(5, brazo1);
  fillpoly(5, brazo2);

  setcolor(LIGHTCYAN);
  setfillstyle(SOLID_FILL, LIGHTCYAN);
  fillpoly(5, pechito);
  fillpoly(5, pechito2);

  getch();
  closegraph();
}