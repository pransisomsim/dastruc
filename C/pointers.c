
#include <stdio.h>

void change(int *age, int new) {
  *age = new;
  printf("%d\n", *age);
}

int sum(int *x, int *y){
  return *x + *y;
}


int main(int argc, char *argv[]){
  int x = 10;
  int *px = &x;

  int y = 20;
  int *py = &y;
  change(px, 20);

  printf("%d\n", sum(&x, &y));

  return 0;
}
