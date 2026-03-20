import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Datos Globales (Base de datos temporal) ---
precios = {1: 700, 2: 1200, 3: 1600}
sabores_disponibles = ["Chocolate", "Vainilla", "Frutilla", "Dulce de Leche", "Limón"]
PASSWORD_STAFF = "1234"  # Contraseña para el modo admin

def actualizar_interfaz():
    """Refresca la lista de sabores y precios en la pantalla principal"""
    lista_visual.delete(0, tk.END)
    for sabor in sabores_disponibles:
        lista_visual.insert(tk.END, f"• {sabor}")

    texto_precios = f"Precios: 1 Bocha ${precios[1]} | 2 Bochas ${precios[2]} | 3 Bochas ${precios[3]}"
    lbl_precios.config(text=texto_precios)

def realizar_pedido():
    try:
        cantidad = int(entrada_bochas.get())
        if cantidad < 1 or cantidad > 3:
            messagebox.showerror("Error", "Solo de 1 a 3 bochas.")
            return

        # Ahora el usuario escribe los sabores separados por coma para permitir repetir
        sabores_texto = entrada_sabores.get().strip()
        lista_sabores = [s.strip().capitalize() for s in sabores_texto.split(",") if s.strip()]

        if len(lista_sabores) != cantidad:
            messagebox.showwarning("Atención", f"Escribiste {len(lista_sabores)} sabores, pero pediste {cantidad} bochas.\nEjemplo: Chocolate, Chocolate, Vainilla")
            return

        total = precios[cantidad]
        resumen = f"🍦 TICKET DE VENTA 🍦\n\nBochas: {cantidad}\nSabores: {', '.join(lista_sabores)}\nTotal: ${total}"
        messagebox.showinfo("Pedido Exitoso", resumen)

    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido de bochas.")

# --- Funciones de Staff (Administración) ---
def abrir_panel_staff():
    password = simpledialog.askstring("Acceso Staff", "Ingrese la contraseña:", show='*')

    if password == PASSWORD_STAFF:
        ventana_admin = tk.Toplevel(ventana)
        ventana_admin.title("Panel de Control Staff")
        ventana_admin.geometry("300x400")
        ventana_admin.configure(bg="#f0f0f0")

        tk.Label(ventana_admin, text="ADMINISTRACIÓN", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

        # Agregar Sabor
        tk.Label(ventana_admin, text="Nuevo Sabor:").pack()
        nuevo_sabor_ent = tk.Entry(ventana_admin)
        nuevo_sabor_ent.pack()

        def add_sabor():
            s = nuevo_sabor_ent.get().strip()
            if s:
                sabores_disponibles.append(s)
                actualizar_interfaz()
                messagebox.showinfo("Éxito", f"{s} agregado.")

        tk.Button(ventana_admin, text="Agregar Sabor", command=add_sabor, bg="lightgreen").pack(pady=5)

        # Cambiar Precios
        tk.Label(ventana_admin, text="Actualizar Precios ($):").pack(pady=5)
        ent_p1 = tk.Entry(ventana_admin); ent_p1.insert(0, str(precios[1])); ent_p1.pack()
        ent_p2 = tk.Entry(ventana_admin); ent_p2.insert(0, str(precios[2])); ent_p2.pack()
        ent_p3 = tk.Entry(ventana_admin); ent_p3.insert(0, str(precios[3])); ent_p3.pack()

        def update_precios():
            try:
                precios[1] = int(ent_p1.get())
                precios[2] = int(ent_p2.get())
                precios[3] = int(ent_p3.get())
                actualizar_interfaz()
                messagebox.showinfo("Éxito", "Precios actualizados.")
            except:
                messagebox.showerror("Error", "Usa solo números.")

        tk.Button(ventana_admin, text="Guardar Precios", command=update_precios, bg="lightblue").pack(pady=10)

    else:
        messagebox.showerror("Error", "Contraseña incorrecta")

# --- Ventana Principal ---
ventana = tk.Tk()
ventana.title("Heladería Dulce Frío")
ventana.geometry("400x600")
ventana.configure(bg="#FFF5F5")

# Título y Precios
tk.Label(ventana, text="🍦 DULCE FRÍO 🍦", font=("Helvetica", 18, "bold"), bg="#FFF5F5", fg="#D63384").pack(pady=10)
lbl_precios = tk.Label(ventana, text="", font=("Helvetica", 9, "bold"), bg="#FFE0E0")
lbl_precios.pack(fill="x", pady=5)

# Entradas de pedido
tk.Label(ventana, text="1. ¿Cuántas bochas? (1-3):", bg="#FFF5F5").pack()
entrada_bochas = tk.Entry(ventana, justify="center"); entrada_bochas.pack(pady=5)

tk.Label(ventana, text="2. Sabores disponibles (mira la lista abajo):", bg="#FFF5F5").pack()
lista_visual = tk.Listbox(ventana, height=6); lista_visual.pack(pady=5)

tk.Label(ventana, text="3. Escribe los sabores (separados por coma):", bg="#FFF5F5").pack()
tk.Label(ventana, text="Ej: Chocolate, Chocolate, Limón", font=("Arial", 8, "italic"), bg="#FFF5F5").pack()
entrada_sabores = tk.Entry(ventana, width=40); entrada_sabores.pack(pady=5)

# Botones
tk.Button(ventana, text="REALIZAR PEDIDO", command=realizar_pedido, bg="#D63384", fg="white", font=("Arial", 10, "bold")).pack(pady=20)
tk.Button(ventana, text="Acceso Staff", command=abrir_panel_staff, relief="flat", bg="#FFF5F5", fg="gray", font=("Arial", 8)).pack(side="bottom")

actualizar_interfaz()
ventana.mainloop()