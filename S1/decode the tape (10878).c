#include<stdio.h>

#define TAPE_WIDTH 11

static char s[TAPE_WIDTH];

int main(){
    int sum, i;
 
    while(gets(s)){
        unsigned int bit = 128;
        sum = 0;

        if(s[0] != '|')
            continue;
 
        for(i = 0; i < TAPE_WIDTH; ++i){
            if(s[i] == ' '){
                bit = (bit >> 1);
            }
            else if(s[i] == 'o'){
                sum += bit;
                bit = (bit >> 1);
            }
        }
 
        printf("%c", sum);
    }

    return 0;
}