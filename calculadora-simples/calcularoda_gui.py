import tkinter as tk


def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacao = choice_var.get()
    
    if operacao == "Adição":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Divisão":
        if num2 == 0:
            resultado = "Erro! Divisão por zero."
        else:
            resultado = num1 / num2
    
    label_resultado.config(text="Resultado: " + str(resultado))

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="black")  

font_style = ("Arial", 12)

label_num1 = tk.Label(root, text="Número 1:", bg="black", fg="white", font=font_style)
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root, bg="white", fg="black", font=font_style)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Número 2:", bg="black", fg="white", font=font_style)
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, bg="white", fg="black", font=font_style)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operacao = tk.Label(root, text="Operação:", bg="black", fg="white", font=font_style)
label_operacao.grid(row=2, column=0, padx=10, pady=10)

choice_var = tk.StringVar()
choices = ["Adição", "Subtração", "Multiplicação", "Divisão"]
choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.config(bg="gray", fg="white", font=font_style)
choice_menu.grid(row=2, column=1, padx=10, pady=10)

button_calcular = tk.Button(root, text="Calcular", command=calcular, bg="black", fg="#2196F3", padx=10, pady=5, font=font_style, relief="groove")
button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="", bg="black", fg="white", font=font_style)
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
