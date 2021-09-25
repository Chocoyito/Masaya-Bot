#include<graphics.h>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<dos.h>
void main(void)
{
int driver=DETECT,modo;
initgraph(&driver,&modo,"c:\\tc20\\bin");
cleardevice();
                    setfillstyle (SOLID_FILL ,9);
					bar3d(220,20,170,200,25,1);
					delay(100);
					setfillstyle (SOLID_FILL ,9);
					bar3d(220,200,340,160,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(290,160,340,80,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(230,19,350,65,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(280,145,230,65,0,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(350,20,400,200,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(400,160,420,200,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(420,70,460,200,25,1);
					delay(100);
					setfillstyle(SOLID_FILL,9);
					bar3d(420,20,460,60,25,1);
getch();
closegraph();
}