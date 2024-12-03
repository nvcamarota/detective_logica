"""
DETECTIVE LÓGICA
Eres una detective resolviendo un caso. Tienes pistas sobre un robo y debes identificar si el sospechoso es culpable. El programa debe evaluar las condiciones lógicas basándose en estas pistas:
1) Si el sospechoso estuvo en el lugar del robo y no tiene coartada válida, es culpable.
2) Si el sospechoso no estuvo en el lugar del robo, pero tiene objetos robados, también es culpable.
3) Si ninguna de las condiciones anteriores se cumple, es inocente.

Usa and, or y not para determinar si el sospechoso es culpable o inocente.
"""

sospecha1 = input("¿Estuvo usted en el lugar del robo? ¿S/N?: ").capitalize()
sospecha2 = input("¿Tiene una coartada válida? ¿S/N?: ").capitalize()
sospecha3 = input("¿Tiene objetos robados? ¿S/N?: ").capitalize()

es_culpable1 = sospecha1 == "S" and sospecha2 == "N"
es_culpable2 = sospecha3 == "S"

mensaje_culpable = "¡Usted es declarado 'Culpable'!"
mensaje_inocente = "¡Usted es declarado 'Inocente'!"

if es_culpable1 or es_culpable2:
    print(mensaje_culpable)
else:
    print(mensaje_inocente)