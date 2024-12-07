#include <stdio.h>
#include <stdlib.h>


char* read_file_to_buffer(const char *filename, size_t *buffer_size) {
    FILE *file = fopen(filename, "rb"); // Open the file in binary mode
    if (!file) {
        perror("Failed to open file");
        return NULL;
    }

    // Seek to the end of the file to determine its size
    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    fseek(file, 0, SEEK_SET); // Go back to the beginning of the file

    if (size < 0) {
        perror("Failed to determine file size");
        fclose(file);
        return NULL;
    }

    // Allocate memory for the buffer
    char *buffer = malloc(size + 1); // +1 for the null terminator
    if (!buffer) {
        perror("Failed to allocate memory");
        fclose(file);
        return NULL;
    }

    // Read the file content into the buffer
    size_t bytes_read = fread(buffer, 1, size, file);
    if (bytes_read != size) {
        perror("Failed to read file");
        free(buffer);
        fclose(file);
        return NULL;
    }

    buffer[size] = '\0'; // Null-terminate the buffer
    fclose(file);

    if (buffer_size) {
        *buffer_size = size; // Set the size of the buffer
    }

    return buffer;
}