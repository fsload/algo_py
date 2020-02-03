#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int partition(){
            //처음에서 나눌수 있는 경우의 수 row-1 + col-1
        //row 기준
        for(int i = 0 ; i < row-1 ; i++){

            for(int j = 0 ; j < col ; j++){
                for(int k = i + 1 ; k < row ; k++){
                    tmp_part[0] += arr[i][j];
                    tmp_part[1] += arr[k][j];
                }
            }
            if(tmp_part[0] - tmp_part[1] < part[0] - part[1]){
                part[0] = tmp_part[0];
                part[1] = tmp_part[1];
                row_cut = i + 1;
            }
            tmp_part[0] = 0;
            tmp_part[1] = 0;
        }
        //col 기준
        for(int i = 0 ; i < col-1 ; i++){
            for(int j = 0 ; j < row ; j++){
                for(int k = i + 1 ; k < col ; k++){
                    tmp_part[0] += arr[j][i];
                    tmp_part[1] += arr[j][k];
                }
            }
            if(tmp_part[0] - tmp_part[1] < part[0] - part[1]){
                part[0] = tmp_part[0];
                part[1] = tmp_part[1];
                col_cut = i + 1;
            }
            tmp_part[0] = 0;
            tmp_part[1] = 0;
        }
        if(col_cut == -1)

}

int main(){
    int TC;
    scanf("%d", &TC);
    int **arr;
    int number = 0;
    int row, col;
    int part[2] = {INT_MAX, 0};
    int tmp_part[2] = {0,};
    int row_cut = -1;
    int col_cut = -1;
    while(TC != 0){
        TC--;
        scanf("%d %d", &row, &col);
        arr = (int**)malloc(sizeof(int*) * row);
        for(int i = 0 ; i < row ; i++)
            arr[i] = (int*)malloc(sizeof(int)*col);
        for(int i = 0 ; i < row; i++){
            for(int j = 0; i < col; i ++){
                scanf("%d", &arr[i][j]);
            }
        }

    }

    return 0;
}