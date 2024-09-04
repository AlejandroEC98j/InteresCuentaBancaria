import tkinter as tk
from tkinter import messagebox

class CuentaBancaria:
    def __init__(self, saldo_inicial: float, tasa_interes_anual: float):
        self.saldo = saldo_inicial
        self.tasa_interes_anual = tasa_interes_anual

    def calcular_interes(self, meses: int) -> float:
        tasa_interes_mensual = self.tasa_interes_anual / 12 / 100
        interes_generado = self.saldo * tasa_interes_mensual * meses
        return interes_generado

    def actualizar_saldo(self, interes: float):
        self.saldo += interes

    def mostrar_saldo(self) -> float:
        return self.saldo

# Función para manejar la lógica de la interfaz
def calcular_interes():
    try:
        saldo_inicial = float(entry_saldo_inicial.get())
        tasa_interes_anual = float(entry_tasa_interes_anual.get())
        meses = int(entry_meses.get())

        cuenta = CuentaBancaria(saldo_inicial, tasa_interes_anual)
        interes = cuenta.calcular_interes(meses)
        cuenta.actualizar_saldo(interes)

        saldo_final = cuenta.mostrar_saldo()
        label_resultado.config(text=f"Saldo final: {saldo_final:.2f} nuevos soles")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de Intereses de Cuenta Bancaria")

# Crear y colocar los widgets
label_saldo_inicial = tk.Label(root, text="Saldo inicial:")
label_saldo_inicial.grid(row=0, column=0, padx=10, pady=10)

entry_saldo_inicial = tk.Entry(root)
entry_saldo_inicial.grid(row=0, column=1, padx=10, pady=10)

label_tasa_interes_anual = tk.Label(root, text="Tasa de interés anual (%):")
label_tasa_interes_anual.grid(row=1, column=0, padx=10, pady=10)

entry_tasa_interes_anual = tk.Entry(root)
entry_tasa_interes_anual.grid(row=1, column=1, padx=10, pady=10)

label_meses = tk.Label(root, text="Número de meses:")
label_meses.grid(row=2, column=0, padx=10, pady=10)

entry_meses = tk.Entry(root)
entry_meses.grid(row=2, column=1, padx=10, pady=10)

button_calcular = tk.Button(root, text="Calcular Interés", command=calcular_interes)
button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="Saldo final: ")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
