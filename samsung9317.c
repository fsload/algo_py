#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char input_[100000];
char seokchan_[100000];
int *error;

void check(int n, int num);

int main(){
    int TC;
    scanf("%d", &TC);
    int count = 0;
    int len;
    error = (int*)calloc(TC,sizeof(int));
    while(TC != 0){
        TC--;
        count++;
        scanf("%d", &len);
        for(int i = 0 ; i <= len ; i++){
            scanf("%c", &input_[i]);   
        }
        for(int i = 0 ; i <= len ; i++){
            scanf("%c", &seokchan_[i]);
        }
        check(len,count);
    }
    for(int i = 0; i < count; i++){
        printf("#%d %d\n", i + 1, error[i]);
    }

    return 0;
}

void check(int n, int num){
    int cnt = 0;
    for(int i = 0 ; i <= n ; i++){
        if((int)input_[i] != (int)seokchan_[i]){
        }
        else{
            cnt++;
            //printf("%c %c", input_[i], seokchan_[i]);
        }
        
    }
    error[num - 1] = cnt - 1;
}