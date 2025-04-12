#include <stdio.h>
#define MAX 10

typedef struct s {
  int data[MAX];
  int cursor;
} Stack;

int init(Stack* s){
  return s->cursor = -1;
}

int isEmpty(Stack* s) {
  return s->cursor == -1;
}

int isFull(Stack* s) {
  return s->cursor == MAX - 1;
}

void push(Stack* s, int value) {
  if (isFull(s)) {
    printf("Stack overflow");
    return;
  }

  s->cursor++;
  s->data[s->cursor] = value;
}

void display(Stack* s){
  if (isEmpty(s)) {
    return;
  }

  for (int i = s->cursor; i >=0; i--) {
    printf("%d\n", s->data[i]);
  }
}
int main() {
  Stack mystack;
  init(&mystack);

  for (int i = 10; i<50 + 1;i= i+10) {
   push(&mystack, i);   
  }
  display(&mystack);
  return 0;
}
