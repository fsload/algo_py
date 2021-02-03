#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int count = 0;
int red_x, red_y, blue_x, blue_y, out_x, out_y;
char **arr;

void moving(int move, int ball){
    if(ball == 1){
        switch (move)
        {
        case 1:
            for(int i = red_y ; arr[i][red_x] != '#' ; i--)
                red_y = i;
            break;
        
        case 2:
            for(int i = red_y ; arr[i][red_x] != '#' ; i++)
                red_y = i;
            break;
        case 3:
            for(int i = red_x ; arr[red_y][i] != '#' ; i--)
                red_x = i;
            break;
        case 4:
            for(int i = red_x ; arr[red_y][i] != '#' ; i++)
                red_x = i;
            break;

        }
    }
        if(ball == 2){
        switch (move)
        {
        case 1:
            for(int i = blue_y ; arr[i][blue_x] != '#' ; i--)
                blue_y = i;
            break;
        
        case 2:
            for(int i = blue_y ; arr[i][blue_x] != '#' ; i++)
                blue_y = i;
            break;
        case 3:
            for(int i = blue_x ; arr[blue_y][i] != '#' ; i--)
                blue_x = i;
            break;
        case 4:
            for(int i = blue_x ; arr[blue_y][i] != '#' ; i++)
                blue_x = i;
            break;

        }
    }
}

int main(){


    int row, col;
    int ball = 0; // 1 red, 2 blue;
    scanf("%d %d", &row, &col);
    arr = (char**)malloc(sizeof(char*) * row);
    for(int i = 0; i < col ; i++){
        arr[i] = (char*)malloc(sizeof(char) * col);
    }
    for(int i = 0 ; i < row ; i ++){
        for(int j = 0 ; j < col ; j ++){
            scanf("%c", arr[i][j]);
        }
    }
    for(int i = 0 ; i < row; i ++){
        for(int j = 0 ; j < col; j ++){
            if(arr[i][j] == 'R'){
                red_x = j;
                red_y = i;
            }
            if(arr[i][j] == 'B'){
                blue_x = j;
                blue_y = i;
            }
            if(arr[i][j] == 'O'){
                out_x = j;
                out_y = i;
            }
        }
    }
    int move; // 1 up, 2 down, 3 left, 4 right
   
    while(1){
        if(arr[])






    }

    return 0;
}