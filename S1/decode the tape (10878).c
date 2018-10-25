#include<stdio.h>

#define TAPE_WIDTH 11

/*
* The encoding used in the tapes are ASCII (7-bit), where o:s represent a 1 and blank 0.
* 
* 1. Read the current line.
* 2. Convert the blank spaces and o:s to binary while ignoring first blank and border of tape.
* 3. Print the ASCII-representation and repeat (1) until at end of tape.
*/

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