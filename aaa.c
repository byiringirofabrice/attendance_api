include<stdio.h>
include<stdlib.h>
include<string.h>

  struct person1{
    char name[30];
    int  age;


  }p1;
  int main(){

    strcpy(p1.name, "Ishimwe Ange"); 
    p1.age = 41;   
    printf("My name is: %s",p1.name);
    printf("My age is: %d",p1.age);

    return 0;
  }