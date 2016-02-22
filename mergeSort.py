#! /bin/python
# -*- coding: utf-8 -*-


def mergeSort(arreglo):
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

