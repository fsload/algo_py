#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
int arr[100][100] = { 0 };

int main() {
    int k;
    int sum = 0;
    int TC = 11;


    for (int t = 1; t < TC; t++) {
        int rowmax = 0, colmax = 0, dimax = 0;
 	    int max = 0;


        scanf("%d", &k);
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                scanf("%d", &arr[i][j]);
            }
        }

        for (int i = 0; i < 100; i++) {
            sum = 0;
            for (int j = 0; j < 100; j++) {
                sum += arr[i][j];
            }
            if (rowmax < sum) {
                rowmax = sum;
            }
        }

        for (int i = 0; i < 100; i++) {
            sum = 0;
            for (int j = 0; j < 100; j++) {
                sum += arr[j][i];
            }
            if (colmax < sum) {
                colmax = sum;
            }

        }
        sum = 0;
        for (int i = 0; i < 100; i++) {
            sum += arr[i][i];
        }
        if (dimax < sum) {
            dimax = sum;
        }
        sum = 0;
        for (int i = 100; i >= 0; i--) {
            sum += arr[i][i];
        }
        if (dimax < sum) {
            dimax = sum;
        }

        max = MAX(MAX(rowmax, colmax), dimax);
        printf("#%d %d",t, max);
        printf("\n");
    }
    return 0;
}
