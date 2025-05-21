#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int value;
  struct Node* next;
}Linked;

int is_even(int value) {
  int total;

  while(value) {
    total = value % 10;
    value = value / 10;
  }
  return total % 2 == 0;
}

Linked *even_list(Linked** head){
  Linked* tmp = *head;
  Linked* new = NULL;
  Linked* tail = NULL;

  while (tmp) {
    if(is_even(tmp->value)) {
      Linked* new_node = (Linked*)malloc(sizeof(Linked));
      new_node->value = tmp->value;
      new_node->next = NULL;

      if (new == NULL) {
        new = new_node;
        tail = new_node;
      }
      else {
        tail->next = new_node;
        tail = new_node;
      }
    }
  }
  return new;
}
void insert(Linked** head, int value) {
  Linked* new = (Linked*)malloc(sizeof(Linked));
  new->value = value;
  new->next = NULL;

  Linked *cur = *head;
  while (cur->next) {
    cur = cur->next;
  }
  cur->next = new;
}

int delete(Linked** head, int value){
  if ((*head) == NULL) {
    return -1;
  }
  Linked *cur = *head;
  Linked *prev = *head;
  return 1;
}

void display(Linked** head) {
  Linked* cur = *head;
  printf("Linked list:\n");

  while (cur) {
    printf(" %d ->", cur->value);
    cur = cur->next;
  }
}

int main(int argc, char *argv[]){
  Linked *head = (Linked*)malloc(sizeof(Linked));
  head->value = 1;

  for (int i = 2;i < 10 +1 ;i++) {
    insert(&head, i);
  }

  Linked* even = even_list(&head);

  display(&even);
  display(&head);
  return 0;
}
