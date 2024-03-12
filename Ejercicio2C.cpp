	/* EJERCICIO DE LABORATORIO 2 */
	
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int* generate_list_random(int n) {
    int* lista = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        lista[i] = rand() % 201 - 100; // Genera números aleatorios entre -100 y 100
    }
    return lista;
}

int minv2(int* lista, int n) {
    int mini = lista[0];
    for (int i = 1; i < n; i++) {
        if (lista[i] < mini) {
            mini = lista[i];
        }
    }
    return mini;
}

int maxv2(int* lista, int n) {
    int maxi = lista[0];
    for (int i = 1; i < n; i++) {
        if (lista[i] > maxi) {
            maxi = lista[i];
        }
    }
    return maxi;
}

int* sumar_listas(int* lista1, int* lista2, int n) {
    int* suma_listas = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        suma_listas[i] = lista1[i] + lista2[i];
    }
    return suma_listas;
}

void print_list(int* lista, int n) {
    printf("[ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", lista[i]);
    }
    printf("]\n");
}

int main() {
    srand(time(NULL)); // Inicializa la semilla para generar números aleatorios

    int* lista1 = generate_list_random(10);
    int* lista2 = generate_list_random(10);

    printf("Lista 1: ");
    print_list(lista1, 10);
    printf("Lista 2: ");
    print_list(lista2, 10);

    printf("El minimo de lista 1 es %d\n", minv2(lista1, 10));
    printf("El minimo de lista 2 es %d\n", minv2(lista2, 10));
    printf("El maximo de lista 1 es %d\n", maxv2(lista1, 10));
    printf("El maximo de lista 2 es %d\n", maxv2(lista2, 10));

    int* suma = sumar_listas(lista1, lista2, 10);
    printf("Listas sumadas: ");
    print_list(suma, 10);

    free(lista1);
    free(lista2);
    free(suma);

    return 0;
}
