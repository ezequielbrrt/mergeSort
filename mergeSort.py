#! /bin/python
# -*- coding: utf-8 -*-


def mergeSort(arreglo):
    if len(arreglo) > 1:
        mitad = len(arreglo)
        parte_izquierda = arreglo[:mitad]
        parte_derecha = arreglo[mitad:]
        mergeSort(parte_izquierda)
        mergeSort(parte_derecha)
        i=0
        j=0
        k=0
        while i < len(parte_izquierda) and j < len(parte_derecha):
            if parte_izquierda[i] < parte_derecha[j]:
                arreglo[k]=parte_izquierda[i]
                i=i+1
            else:
                arreglo[k]=parte_derecha[j]
                j=j+1
            k=k+1
        while i < len(parte_izquierda):
            arreglo[k]=parte_izquierda[i]
            i=i+1
            k=k+1
        while j < len(parte_derecha):
            arreglo[k]=parte_derecha[j]
            j=j+1
            k=k+1
    return arreglo

def main():
	salir = True
	valores = []
	print "Merge Sort"
	while salir:
		try: 
			numeros = int(raw_input("Escribe los números a ordenar: "))
			valores.append(numeros)
		except:
			print "Iniciando el Algoritmo"
			salir = False
	print mergeSort(valores)

main()

