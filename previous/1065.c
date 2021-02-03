#include <stdio.h>
#include <string.h>
// tot len now len 구하기

int get_len(int num){
    int len = 0;
    while(1){
        num /= 10;
        len++;
        if (num < 1) break;
    }
    return len;

}

int main(){
    printf("input num = ");
    int input, tot_len, cur_len;
    scanf("%d", &input);
    int tmp = input;
    int arr[100];
    int count = 0;
    int chai, flag = 0;
    tot_len = get_len(input);

    if (tot_len >= 3){
        for(int j = 100; j <= input; j ++){
            cur_len = get_len(j);
            arr[0] = j % 10;
            tmp = j;

            for (int i = 1 ; i < cur_len ; i ++){
                    tmp = tmp / 10;
                    arr[i] = tmp % 10;
            }

            chai = arr[0] - arr[1];
            for(int i = 1 ; i < cur_len - 1 ; i++){
                int num = arr[i] - arr[i+1];
                if(num != chai)
                    flag ++;
            }
            if (flag == 0)
                count += 1;
            flag = 0;
        }
    }
    if (tot_len >= 3)
        count += 99;
    else
        count = input;

    printf("%d\n", count);
    return 0;
}