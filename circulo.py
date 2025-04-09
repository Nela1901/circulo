class Circulo:
    PI=3.1416
    def __init__(self,radio):
        self.radio=radio
    def circunfenrencia(self):
        return 2*self.PI*self.radio

if __name__ = "__main__":
    instancia_circulo=Circulo(10)
    print(f"la circunferencia es: {instancia_circulo.circunfenrencia()}")
