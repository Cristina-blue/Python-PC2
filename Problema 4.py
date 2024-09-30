alumnos = []

n = int(input("¿Cuántos alumnos desea ingresar?:"))

for _ in range(n):
    nombre = input("Ingrese el nombre del alumno:")

    notas = []
    for i in range(1, 4):
        nota = float(input(f"Ingrese la calificación {i} de {nombre}:"))
        notas.append(nota)

    alumno = {
        'Alumno': nombre,
        'Notas': notas}
    alumnos.append(alumno)

print("\nListado completo de alumnos y calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
