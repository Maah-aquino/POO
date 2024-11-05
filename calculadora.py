from interface import Interface

class Calculadora:
    def __init__(self, interface):
        self.interface = interface
        self.todos_valores = ''
       
    def entrar_valores(self, valor):

        self.todos_valores += str(valor)
        self.interface.update_display(self.todos_valores)

    def calcular(self):
      
            resultado = eval(self.todos_valores)
            self.interface.update_display(str(resultado))
        

    def clear(self):
        self.todos_valores = ''
        self.interface.clear_display()
