import random
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def generar_array(tamano):
    return [random.randint(1, 1000) for _ in range(tamano)]

def medir_tiempo(funcion, arr):
    inicio = time.time()
    funcion(arr.copy())
    fin = time.time()
    return (fin - inicio) * 1000

def ejecutar_pruebas_y_graficar(tamanos, num_pruebas=10):
    tiempos_bubble = []
    tiempos_quick = []
    
    # Para cada tamaño, ejecutamos las pruebas
    for tamano in tamanos:
        print(f"\nPruebas con array de tamaño {tamano}:")
        print("-" * 50)
        
        # Ejecutamos varias pruebas y tomamos el promedio
        tiempos_bubble_tamano = []
        tiempos_quick_tamano = []
        
        for i in range(num_pruebas):
            arr_original = generar_array(tamano)
            
            tiempo_bubble = medir_tiempo(bubble_sort, arr_original)
            tiempo_quick = medir_tiempo(quicksort, arr_original)
            
            tiempos_bubble_tamano.append(tiempo_bubble)
            tiempos_quick_tamano.append(tiempo_quick)
            
            print(f"Prueba {i+1}:")
            print(f"Bubble Sort: {tiempo_bubble:.2f} ms")
            print(f"Quicksort:   {tiempo_quick:.2f} ms")
        
        # Guardamos los promedios
        promedio_bubble = statistics.mean(tiempos_bubble_tamano)
        promedio_quick = statistics.mean(tiempos_quick_tamano)
        
        tiempos_bubble.append(promedio_bubble)
        tiempos_quick.append(promedio_quick)
        
        print(f"\nPromedio para tamaño {tamano}:")
        print(f"Bubble Sort: {promedio_bubble:.2f} ms")
        print(f"Quicksort:   {promedio_quick:.2f} ms")
    
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_bubble, 'o-', label='Bubble Sort', color='red')
    plt.plot(tamanos, tiempos_quick, 'o-', label='Quicksort', color='blue')
    
    plt.xlabel('Tamaño del array')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Comparación de tiempos de ejecución')
    plt.legend()
    plt.grid(True)
    
    # Añadir escala logarítmica si hay grandes diferencias
    if max(tiempos_bubble) / min(tiempos_quick) > 100:
        plt.yscale('log')
    
    # Mostrar valores en los puntos
    for i, (tamano, tiempo) in enumerate(zip(tamanos, tiempos_bubble)):
        plt.annotate(f'{tiempo:.1f}ms', 
                    (tamano, tiempo),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center')
    
    for i, (tamano, tiempo) in enumerate(zip(tamanos, tiempos_quick)):
        plt.annotate(f'{tiempo:.1f}ms', 
                    (tamano, tiempo),
                    textcoords="offset points",
                    xytext=(0,-15),
                    ha='center')
    
    plt.tight_layout()
    plt.show()

# Ejecutar el programa con diferentes tamaños
tamanos = [100, 1000, 2000, 5000, 10000]
ejecutar_pruebas_y_graficar(tamanos)