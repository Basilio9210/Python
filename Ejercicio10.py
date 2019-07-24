#! /usr/bin/env python
# -*- coding: utf-8 -*-
def es_bisiesto():
    print "Comprueba años bisiestos"
    a = input ("Escriba un años y le dire si es bisiesto: ")
    if a % 4 == 0 and (not(a % 100 == 0)):
        print "El año", a, "es un año bisiesto porque es multiplo de 4"
    elif a % 400 == 0:
        print "El año", a, "es un año bisiesto porque es multiplo de 400"
    else:
        print "El año", a, "no es bisiesto"
