# calculadora_mejorada.py
# Script mejorado para operaciones matemáticas con manejo de errores

def obtener_numero(mensaje):
    """Solicita un número al usuario con manejo de errores"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

def mostrar_resultado(num1, num2, operacion, resultado):
    """Muestra el resultado formateado"""
    print(f"\n{num1} {operacion} {num2} = {resultado}")

def realizar_operacion(num1, num2, operacion):
    """Realiza la operación matemática solicitada"""
    operaciones = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else None,
        '//': num1 // num2 if num2 != 0 else None,  # División entera
        '%': num1 % num2 if num2 != 0 else None,    # Módulo
        '**': num1 ** num2                          # Potencia
    }
    
    if operacion in operaciones:
        resultado = operaciones[operacion]
        if resultado is None:
            return "Error: No se puede dividir por cero."
        return resultado
    else:
        return "Operación no válida."

def main():
    """Función principal de la calculadora"""
    print("=== CALCULADORA MEJORADA ===")
    print("Operaciones disponibles: +, -, *, /, // (división entera), % (módulo), ** (potencia)")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        try:
            # Obtener primer número
            entrada = input("Primer número (o 'salir'): ").strip().lower()
            if entrada == 'salir':
                print("¡Hasta luego!")
                break
            
            numero_1 = float(entrada)
            
            # Obtener segundo número
            entrada = input("Segundo número: ").strip().lower()
            if entrada == 'salir':
                print("¡Hasta luego!")
                break
                
            numero_2 = float(entrada)
            
            # Obtener operación
            operacion = input("Operación (+, -, *, /, //, %, **): ").strip().lower()
            if operacion == 'salir':
                print("¡Hasta luego!")
                break
            
            # Realizar cálculo y mostrar resultado
            resultado = realizar_operacion(numero_1, numero_2, operacion)
            
            if isinstance(resultado, str) and resultado.startswith("Error"):
                print(f"\n{resultado}")
            else:
                mostrar_resultado(numero_1, numero_2, operacion, resultado)
                
        except ValueError:
            print("Error: Por favor ingresa números válidos.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        print("-" * 40)

if __name__ == "__main__":
    main()
    