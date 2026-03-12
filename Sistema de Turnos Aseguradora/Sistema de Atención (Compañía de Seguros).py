# 1. Primero definimos la estructura de la Cola
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

# 2. Ahora definimos el Sistema que usa la clase Cola
class SistemaSeguros:
    def __init__(self, cantidad_servicios):
        # Aquí es donde fallaba: ahora 'Cola()' ya existe arriba
        self.servicios = {str(i): Cola() for i in range(1, cantidad_servicios + 1)}
        self.contadores = {str(i): 1 for i in range(1, cantidad_servicios + 1)}

    def registrar_cliente(self, id_servicio):
        if id_servicio in self.servicios:
            turno = self.contadores[id_servicio]
            self.servicios[id_servicio].enqueue(turno)
            print(f"-> Cliente registrado en Servicio {id_servicio}. Turno asignado: {turno}")
            self.contadores[id_servicio] += 1
        else:
            print(f"Error: El servicio {id_servicio} no existe.")

    def atender_cliente(self, id_servicio):
        if id_servicio in self.servicios:
            turno = self.servicios[id_servicio].dequeue()
            if turno:
                print(f"[/] Atendiendo al turno {turno} en el Servicio {id_servicio}")
            else:
                print(f"x No hay clientes en espera para el Servicio {id_servicio}")
        else:
            print(f"Error: El servicio {id_servicio} no existe.")

def menu():
    sistema = SistemaSeguros(3) # Definimos 3 servicios
    print("--- SISTEMA DE ATENCIÓN ASEGURADORA ---")
    print("Comandos: C1, C2 (Registrar) | A1, A2 (Atender) | S (Salir)")
    
    while True:
        entrada = input("\nIngrese comando: ").upper().strip()
        if entrada == 'S': break
        
        if len(entrada) >= 2:
            accion = entrada[0]
            num_serv = entrada[1:]
            if accion == 'C': sistema.registrar_cliente(num_serv)
            elif accion == 'A': sistema.atender_cliente(num_serv)
        else:
            print("Formato inválido. Use C o A seguido del número.")

if __name__ == "__main__":
    menu()