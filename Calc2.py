import tkinter as tk
from tkinter import ttk


def calculo():

    sl_liquido = float(0 if sal_liq.get() == '' else sal_liq.get())
    aluguel_value = float(0 if aluguel.get() == '' else aluguel.get())
    agua_value = float(0 if agua_entry.get() == '' else agua_entry.get())
    luz_value = float(0 if luz.get() == '' else luz.get())
    internet_value = float(0 if internet.get() == '' else internet.get())
    cartao1_value = float(0 if cartao1.get() == '' else cartao1.get())
    cartao2_value = float(0 if cartao2.get() == '' else cartao2.get())
    cartao3_value = float(0 if cartao3.get() == '' else cartao3.get())
    outros_value = float(0 if outros.get() == '' else outros.get())


      
    divid = sl_liquido - aluguel_value - agua_value - luz_value - internet_value - cartao1_value - cartao2_value - cartao3_value - outros_value
    rest = divid*(100/sl_liquido)
    
    resultado_geral['text'] = f"Irá te sobrar R${divid} que é um total de {rest:.2f}% após pagar todas as suas dividas"



janela = tk.Tk()
janela.title('Calculadora de Dividas')

opcoes_label = tk.Label(text='Informe, seu salario liquido')
opcoes_label.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

sal_liq = tk.Entry()
sal_liq.grid(row = 0, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

aluguel_label = tk.Label(text='Informe o valor do aluguel')
aluguel_label.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

aluguel = tk.Entry()
aluguel.grid(row = 1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

Agua_label = tk.Label(text='Valor da conta de água')
Agua_label.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

agua_entry = tk.Entry()
agua_entry.grid(row = 2, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

luz_label = tk.Label(text='Valor da conta de luz')
luz_label.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

luz = tk.Entry()
luz.grid(row = 3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

internet_label = tk.Label(text='valor do combo de internet')
internet_label.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

internet = tk.Entry()
internet.grid(row = 4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

cartao_label = tk.Label(text='Faturas dos cartões')
cartao_label.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

cartao1 = tk.Entry()
cartao1.grid(row = 7, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

cartao2 = tk.Entry()
cartao2.grid(row = 7, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

cartao3 = tk.Entry()
cartao3.grid(row = 7, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)

outros_label = tk.Label(text='Outros gastos')
outros_label.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

outros = tk.Entry()
outros.grid(row = 5, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

caucular_botao = tk.Button(text = "Calcular", command=calculo)
caucular_botao.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

resultado_geral = tk.Label(text="")
resultado_geral.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

tk.mainloop()