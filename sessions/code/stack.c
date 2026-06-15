#include <stdio.h>
int fun(int i){
    printf("inside fun(%d)\n", i);
    return fun(i+1);
}


int main(){
    int x = fun(1);
    
}