#include <stdio.h>
#include <stdlib.h>
int main(){ 
    int test_case;
    int T;
    scanf("%d", &test_case);

    int grade[10000] = {0};
    int cnt[1000] = {0};
    int label;
    int num = 0;
    int fa = 0;

    for(T = 1; T <= test_case; T++){
        int grade[10000] = {0};
        int cnt[1000] = {0};
        fa = 0;
        int num = 0;

        
        scanf("%d", &label);
        for (int i = 0 ; i < 1000 ; i++){
            scanf("%d", &grade[i]);
        }
        for (int i = 0 ; i < 1000 ; i++){
        //    printf("%d     ",grade[i]);
            for(int j = 1 ; j < 101 ; j++){
                if (j == grade[i])
                    cnt[j]++;
            }
        }
        for (int j = 1 ; j < 101 ; j++){
            //printf("cnt%d = %d\n",j,cnt[j]);
            if(cnt[j] > num){
                num = cnt[j];
                fa = j;
            }
            else if (cnt[j] == num){
                if (fa < j){
                    fa = j;
                }
            }
        }
        printf("#%d %d\n",T, fa);
    }
    return 0;
}