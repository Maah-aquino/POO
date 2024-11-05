import tkinter as tk
class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Calculadora')
        self.janela.geometry("235x318")
        self.janela.config(bg="#ECEFF1")  # cor azul escuro
        
        self.frame_tela = tk.Frame(self.janela, width=235, height=50, bg="#ECEFF1")  # Divide a tela criando o visor da calculadora
        self.frame_tela.grid(row=0, column=0)
        self.frame_corpo = tk.Frame(self.janela, width=235, height=268)  # Divide a tela criando o corpo que vai os botões da calculadora
        self.frame_corpo.grid(row=1, column=0)
        
        self.valor_texto = tk.StringVar()
        self.app_label = tk.Label(self.frame_tela, textvariable=self.valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e", bd=0, justify=tk.RIGHT, font=('Ivy 18 '), bg="#ded4d4", fg="#feffff")
        self.app_label.place(x=0, y=0)

    def update_display(self, value):
        self.valor_texto.set(value)

    def get_display_value(self):
        return self.valor_texto.get()

    def clear_display(self):
        self.valor_texto.set('')

    def criar_botoes(self, calculadora): ##ECEFF1
        botoes = [
            ('C', calculadora.clear, 11, 2, 0, 0, '#EA4335', '#3b3b3b'),
            ('%', lambda: calculadora.entrar_valores('%'), 5, 2, 118, 0, '#C71585', '#38576b'),
            ('/', lambda: calculadora.entrar_valores('/'), 5, 2, 177, 0, '#C71585', '#38576b'),
            ('7', lambda: calculadora.entrar_valores('7'), 5, 2, 0, 52, '#ECEFF1', '#3b3b3b'),
            ('8', lambda: calculadora.entrar_valores('8'), 5, 2, 59, 52, '#ECEFF1', '#3b3b3b'),
            ('9', lambda: calculadora.entrar_valores('9'), 5, 2, 118, 52, '#ECEFF1', '#3b3b3b'),
            ('*', lambda: calculadora.entrar_valores('*'), 5, 2, 177, 52, '#C71585', '#38576b'),
            ('4', lambda: calculadora.entrar_valores('4'), 5, 2, 0, 104, '#ECEFF1', '#3b3b3b'),
            ('5', lambda: calculadora.entrar_valores('5'), 5, 2, 59, 104, '#ECEFF1', '#3b3b3b'),
            ('6', lambda: calculadora.entrar_valores('6'), 5, 2, 118, 104, '#ECEFF1', '#3b3b3b'),
            ('-', lambda: calculadora.entrar_valores('-'), 5, 2, 177, 104, '#C71585', '#38576b'),
            ('1', lambda: calculadora.entrar_valores('1'), 5, 2, 0, 156, '#ECEFF1', '#3b3b3b'),
            ('2', lambda: calculadora.entrar_valores('2'), 5, 2, 59, 156, '#ECEFF1', '#3b3b3b'),
            ('3', lambda: calculadora.entrar_valores('3'), 5, 2, 118, 156, '#ECEFF1', '#3b3b3b'),
            ('+', lambda: calculadora.entrar_valores('+'), 5, 2, 177, 156, '#C71585', '#38576b'),
            ('0', lambda: calculadora.entrar_valores('0'), 11, 2, 0, 208, '#ECEFF1', '#3b3b3b'),
            ('.', lambda: calculadora.entrar_valores('.'), 5, 2, 118, 208, '#ECEFF1', '#3b3b3b'),
            ('=', calculadora.calcular, 5, 2, 177, 208, '#C71585', '#38576b')
        ]
        
        for (text, command, width, height, x, y, bg, fg) in botoes:
            b = tk.Button(self.frame_corpo, command=command, text=text, width=width, height=height, bg=bg, fg=fg, font=('Ivy 13 bold'), relief=tk.RAISED, overrelief=tk.RIDGE)
            b.place(x=x, y=y)
