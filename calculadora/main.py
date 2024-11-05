import tkinter as tk
from interface import Interface
from calculadora import Calculadora

if __name__ == "__main__":
    janela = tk.Tk()
    interface = Interface(janela)
    calculadora = Calculadora(interface)
    interface.criar_botoes(calculadora)
    janela.mainloop()
