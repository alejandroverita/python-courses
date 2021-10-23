# SETS
set_ala_fija = {"Anfibio", "Hidroavion", "Avion", "Ornitoptero"}
set_ala_giratoria = {
    "Convertible",
    "Ornitoptero",
    "Autogiro",
    "Girodino",
    "Helicoptero",
}
set_sin_propulsor = {"Velero", "Planeador", "Parapente", "Ala delta"}

# Union
set_con_propulsor = set_ala_fija | set_ala_giratoria

# Solo la intercepcion
set_interseption_propulsor = set_ala_fija & set_ala_giratoria

# Diferencia del set1 - set2
set_difference = set_ala_fija.difference(set_ala_giratoria)

# resultado de la diferencia de los set sin las intercepciones
assymetric_set = set_ala_fija ^ set_ala_giratoria

print(set_con_propulsor)
print(set_interseption_propulsor)
print(set_difference)
print(assymetric_set)
