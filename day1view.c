#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int findMax(int a, int b, int c, int d){
    return MAX(MAX(a,b),MAX(c,d));
}

int main(){

    int tc = 10;

    for(int i = 1; i < 11; i++){
        int tot;
        int cnt = 0;
        int arr[1002] = {0};
        scanf("%d", &tot);
        for(int i = 0 ; i < tot ; i ++){
            scanf("%d", &arr[i]);
        }

        for(int i = 2 ; i < tot -2 ; i ++){
            if(arr[i] - findMax(arr[i+1], arr[i+2], arr[i-1],arr[i-2]) > 0){
                cnt += arr[i] - findMax(arr[i+1], arr[i+2], arr[i-1],arr[i-2]);
            }
        }

        printf("#%d %d\n", i, cnt);
    }
    return 0;
}

