# cajablanca.py - Versión Refactorizada y Segura (MTC_011 / CP-02)
def calcular_copago_mediconnect():
    print("--- MÓDULO DE CÁLCULO DE COPAGOS MEDICONNECT (REFACTORIZADO) ---")
    s = 0  # Inicialización defensiva de variable para evitar UnboundLocalError
    
    try:
        entrada = input("Ingrese número de atenciones (N): ")
        N = int(entrada)
        
        if N > 0:
            for i in range(1, N + 1):
                s += i * 15000
            print(f"Monto total de copago calculado: ${s}")
        else:
            print(f"Cantidad de atenciones inválida ({N}). Copago asignado: ${s}")
            
    except ValueError:
        print("Error: Debe ingresar únicamente números enteros.")

if __name__ == "__main__":
    calcular_copago_mediconnect()