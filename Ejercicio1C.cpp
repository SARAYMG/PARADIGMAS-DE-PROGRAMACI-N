	/* EJERCICIO DE LABORATORIO 1 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define ARRAY_SIZE 1000

	//Función para generar el arreglo e imprimirlo...
	void ga(int arreglo[], int size) {
		for(int i=0; i<size; i++){
			arreglo[i] = rand() % 1000;
		}
	}
		
	void ia(int arreglo[], int size){
		for(int i=0; i<size; i++){
			printf("%d", arreglo[i]);
		}
		printf("\n");
	}
	//Función de busqueda secuencial...
	int bs(int arreglo[], int size, int ele){
		for(int i=0; i<size; i++){
			if(arreglo[i] == ele){
				return i;
			}
		}
		return -1;
	}

	//Función de ordenamiento: Metodo Burbuja
	void mb(int arreglo[], int size){
		for(int i=0; i<size -1; i++){
			for(int j=0; j<size-i-1; j++){
				if(arreglo[j] > arreglo[j + 1]){
					
	//Intercambiamos elementos si estan en el orden incorrecto
					int temp = arreglo[j];
					arreglo[j] = arreglo[j + 1];
					arreglo[j + 1] = temp;
                }
			}
		}
	}

	//Comienza main
	int main() {
		
		srand(time(NULL));
		int arreglo[ARRAY_SIZE];
		clock_t inicio,fin;
		double tiempo;
	
	// Paso 1: Generar arreglo numeros aleatorios
		inicio = clock();
		ga(arreglo, ARRAY_SIZE);

	//Paso 2: Imprimir el arreglo generado
		printf("Arreglo Generado:\n");
		ia(arreglo,ARRAY_SIZE);
		
	// Paso 3: Solicitar al usuario el numero a buscar	
		int elebus;
		printf("\nIngrese el numero que desea buscar:");
		scanf("%d", &elebus);
		
	// Paso 4: Busqueda secuencial del elemento ingresado por el usuario
		inicio = clock();
		int indenc = bs(arreglo, ARRAY_SIZE, elebus);
		fin = clock();
		tiempo = ((double)(fin - inicio)) / CLOCKS_PER_SEC;
		if(indenc != -1){
			printf("\nARREGLO GENERADO");
			printf("\nEL ELEMENTO %d SE ENCUENTRA EN EL INDICE %d\n\n", elebus, indenc);
		}	else{
			printf("\nEL ELEMENTO %d NO SE ENCUENTRA EN EL ARREGLO\n\n", elebus);
		}

    // Paso 5: Ordenar el arreglo
    mb(arreglo, ARRAY_SIZE);
   
    // Paso 6: Imprimir el arreglo ordenado
    printf("Arreglo ordenado:\n");
    ia(arreglo, ARRAY_SIZE);


	// Paso 7: Buscar en el arreglo ordenado
    printf("\nARREGLO ORDENADO\n");
    inicio = clock();
    indenc = bs(arreglo, ARRAY_SIZE, elebus);
    fin = clock();
    tiempo = ((double)(fin - inicio)) / CLOCKS_PER_SEC;
    if (indenc != -1) {
        printf("EL ELEMENTO %d SE ENCUENTRA EN EL INDICE %d\n\n", elebus, indenc);
    } else {
        printf("EL ELEMENTO %d NO SE ENCUENTRA EN EL ARREGLO\n\n", elebus);
    }
    fin = clock();
    tiempo = ((double)(fin - inicio)) / CLOCKS_PER_SEC;
    printf("Tiempo de ordenacion del arreglo: %f segundos\n", tiempo);

    return 0;
}