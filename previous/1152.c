#include <stdio.h>

int main(){
    char input[1000000];
    scanf("%[^\n]s", input);
    int cnt = 1;
    int i;
    for(i = 0 ; input[i] ; i++){
        if(input[i] == ' ')
            cnt++;
        else if(input[i] == '\0'){
            break;
        }
    }
    if(input[0] == ' ')
        cnt -= 1;
    if (input[i-1] == ' ')
        cnt -= 1;
    printf("%d \n", cnt);
    return 0;
}