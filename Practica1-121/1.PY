class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def tiene_solucion(self):
        return (self.a * self.d - self.b * self.c) != 0
    
    def get_x(self):
        if not self.tiene_solucion():
            raise ArithmeticError("La ecuación no tiene solución")
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
    
    def get_y(self):
        if not self.tiene_solucion():
            raise ArithmeticError("La ecuación no tiene solución")
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)

# Programa de prueba en Python
if __name__ == "__main__":
    print("Ingrese a, b, c, d, e, f separados por espacios:")
    valores = input().split()
    
    if len(valores) != 6:
        print("Debe ingresar exactamente 6 valores")
    else:
        try:
            a, b, c, d, e, f = map(float, valores)
            ecuacion = EcuacionLineal(a, b, c, d, e, f)
            
            if ecuacion.tiene_solucion():
                x = ecuacion.get_x()
                y = ecuacion.get_y()
                print(f"x = {x:.1f}, y = {y:.1f}")
            else:
                print("La ecuación no tiene solución")
                
        except ValueError:
            print("Todos los valores deben ser números")
        except ArithmeticError as e:
            print(e)