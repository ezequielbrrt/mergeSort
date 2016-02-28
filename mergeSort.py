#! /bin/python
# -*- coding: utf-8 -*-

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda
    if izquierda[0] < derecha[0]:
        return [izquierda[0]] + merge(izquierda[1:], derecha)
    return [derecha[0]] + merge(izquierda, derecha[1:])

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
	print merge_sort(valores)
	print "Algoritmo terminado"
main()

