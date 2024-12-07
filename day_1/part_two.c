#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../common/file.c"
#include "../common/algo.c"

#define ABS(x) ((x) > 0 ? x : -x)
typedef struct {

    int* first_list;
    int* second_list;

    int n;

} input_t;



input_t read_pairs(const char* input){
    int n = 1; 
    int input_len = strlen(input);
    for (int i = 0; i < input_len; i++){
        if (input[i] == '\n') n++;
    }

    int* first = malloc(sizeof(int) *n);
    int* second = malloc(sizeof(int) *n);

    int line_n = 0;

    for (char *p = strtok((char*)input,"\n"); p != NULL; p = strtok(NULL, "\n")){
        
        int first_number = 0;
        int second_number = 0;

        int index = 0; 
        while(p[index] <= '9' && p[index] >= '0'){
            first_number *= 10;
            first_number += (p[index] - '0');
            index++;
        }

        while(p[index] == ' ') index++;

        while(p[index] <= '9' && p[index] >= '0'){
            second_number *= 10;
            second_number += (p[index] - '0');
            index++;
        }

        first[line_n] = first_number;
        second[line_n] = second_number;

        line_n++;
    }

    return (input_t){.first_list = first, .second_list=second, .n =n};
}

int solve(input_t input){

    int sum = 0;
    for (int i = 0; i < input.n; i++){
        int first = input.first_list[i];

        int similarity_n = 0;
        for (int i = 0; i < input.n; i++){
            int second = input.second_list[i];
            if (first == second) similarity_n++;
        }

        sum += (first*similarity_n);
    }
    return sum;
}


int main(void){ 
    size_t buffer_size = 0;
    char* input_buffer = read_file_to_buffer("input.txt", &buffer_size);
    input_t pairs = read_pairs(input_buffer);
    int result = solve(pairs);
    printf("%d\n",result);

    free(input_buffer);
    free(pairs.first_list);
    free(pairs.second_list);
    return 0;
}