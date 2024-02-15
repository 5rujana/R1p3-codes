#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char *data;
    int length;
} MyString;

void initializeString(MyString *str, const char *source) {
    str->length = 0;

    while (source[str->length] != '\0') {
        str->length++;
    }

    str->data = (char *)malloc((str->length + 1) * sizeof(char));

    for (int i = 0; i < str->length; i++) {
        str->data[i] = source[i];
    }

    str->data[str->length] = '\0';
}

void printString(const MyString *str) {
    for (int i = 0; i < str->length; i++) {
        printf("%c", (str->data[i])-1);
    }
    printf("\n");
}


void freeString(MyString *str) {
    free(str->data);
    str->length = 0;
}

int main() {
    
    MyString myString;
    initializeString(&myString, "NEVZMW");
    printString(&myString);
    freeString(&myString);

    return 0;
}
