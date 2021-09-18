#include<conio.h>
#include<stdlib.h>
#include<dos.h>
#include<graphics.h>


void main(void)
{
 int driver=DETECT,modo;
 int u[]={77,100,148,100,148,262,244,262,244,165,305,165,305,315,77,315,77,101};
 int ni[]={163,100,385,100,385,263,410,263,410,165,481,165,481,316,321,316,321,148,233,148,233,245,163,245,163,100};
 int punto[]={410,102,482,102,482,150,410,150,410,102};

 initgraph(&driver,&modo,"c:\\TC20\\BIN");
 cleardevice();
  setfillstyle(SOLID_FILL,BLUE);
  fillpoly(9,u);

  fillpoly(13,ni);


  fillpoly(4,punto);


 getch();
 closegraph();
}