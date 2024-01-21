
class ListaDeTareas:
    def __init__(self):
        self.tareas = {}

    def agregar_tarea(self, tarea):
        self.tareas[len(self.tareas) + 1] = {'tarea': tarea, 'completada': False}
        print(f"Tarea agregada: {tarea}")

    def mostrar_tareas(self):
        print("Lista de Tareas:")
        for num, tarea in self.tareas.items():
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{num}. {tarea['tarea']} - {estado}")

    def marcar_completada(self, num_tarea):
        tarea = self.tareas.get(num_tarea)
        if tarea:
            tarea['completada'] = True
            print(f"Tarea marcada como completada: {tarea['tarea']}")
        else:
            print("Número de tarea no válido")

    def eliminar_tarea(self, num_tarea):
        tarea = self.tareas.pop(num_tarea, None)
        if tarea:
            print(f"Tarea eliminada: {tarea['tarea']}")
        else:
            print("Número de tarea no válido")

def main():
    lista_tareas = ListaDeTareas()

    while True:
        print("\n1. Agregar tarea\n2. Mostrar tareas\n3. Marcar como completada\n4. Eliminar tarea\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tarea = input("Ingrese la nueva tarea: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == '2':
            lista_tareas.mostrar_tareas()
        elif opcion == '3':
            num_tarea = int(input("Ingrese el número de la tarea completada: "))
            lista_tareas.marcar_completada(num_tarea)
        elif opcion == '4':
            num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(num_tarea)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor elija nuevamente.")


if __name__ == "__main__":
    main()