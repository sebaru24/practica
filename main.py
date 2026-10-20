import tkinter as tk
from tkinter import ttk, messagebox


def calcular_imc():
    nombre = entrada_nombre.get().strip()

    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        if not nombre:
            messagebox.showwarning(
                "Atención", "Ingresa tu nombre."
            )
            return

        if peso <= 0 or altura <= 0:
            messagebox.showwarning(
                "Atención",
                "El peso y la altura deben ser mayores que cero."
            )
            return

        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = "Peso bajo"
        elif imc < 25:
            categoria = "Peso normal"
        elif imc < 30:
            categoria = "Sobrepeso"
        elif imc < 35:
            categoria = "Obesidad grado 1"
        elif imc < 40:
            categoria = "Obesidad grado 2"
        else:
            categoria = "Obesidad grado 3"

        resultado.config(
            text=f"Hola, {nombre}\n\n"
                 f"Tu IMC es: {imc:.2f}\n"
                 f"Categoría: {categoria}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingresa valores numéricos válidos para peso y altura."
        )


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("420x520")
ventana.resizable(False, False)

# Contenedor principal
marco = ttk.Frame(ventana, padding=25)
marco.pack(fill="both", expand=True)

# Título
ttk.Label(
    marco,
    text="Calculadora de IMC",
    font=("Arial", 18, "bold")
).pack(pady=(0, 8))

ttk.Label(
    marco,
    text="Ingresa tus datos para calcular tu IMC"
).pack(pady=(0, 20))

# Campo de nombre
ttk.Label(marco, text="Nombre").pack(anchor="w")
entrada_nombre = ttk.Entry(marco, width=35)
entrada_nombre.pack(fill="x", pady=(4, 12))

# Campo de peso
ttk.Label(marco, text="Peso en kilogramos (kg)").pack(anchor="w")
entrada_peso = ttk.Entry(marco, width=35)
entrada_peso.pack(fill="x", pady=(4, 12))

# Campo de altura
ttk.Label(marco, text="Altura en metros (m)").pack(anchor="w")
entrada_altura = ttk.Entry(marco, width=35)
entrada_altura.pack(fill="x", pady=(4, 20))

# Botón para calcular
boton = ttk.Button(
    marco,
    text="Calcular IMC",
    command=calcular_imc
)
boton.pack(fill="x", ipady=5)

# Área para mostrar el resultado
resultado = ttk.Label(
    marco,
    text="Tu resultado aparecerá aquí",
    justify="center",
    font=("Arial", 11)
)
resultado.pack(pady=20)

# Mantener la ventana abierta
ventana.mainloop()