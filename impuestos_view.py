from impuestos_controller import parsear_tipos, calcular_total

MENU = """
================= CALCULADORA DE IMPUESTOS =================
Precio base: número >= 0
Impuestos permitidos:
  exento | iva19 | iva5 | inc8 | licor25 | bolsa (suma 50 COP)

Ejemplos:
  precio: 10000
  impuestos: iva19
  impuestos: inc8, bolsa

Comandos: 'q' para salir
============================================================
"""

def run():
    print(MENU)
    while True:
        precio_str = input("💲 Precio base (o 'q' para salir): ").strip()
        if precio_str.lower() == "q":
            print("👋 Gracias por usar la calculadora.")
            break

        try:
            precio = float(precio_str)
            if precio < 0:
                print("⚠️  El precio debe ser mayor o igual a 0.\n")
                continue
        except ValueError:
            print("❌ El precio debe ser numérico.\n")
            continue

        tipos_str = input("🧾 Ingrese impuesto(s): ").strip()
        if tipos_str.lower() == "q":
            print("👋 Gracias por usar la calculadora.")
            break

        tipos = parsear_tipos(tipos_str)

        try:
            total = calcular_total(precio, tipos)
            print(f"✅ Total calculado:\n   • Precio base: {precio}\n   • Impuesto(s): {tipos}\n   • Total a pagar: {total}\n")
        except (ValueError, TypeError) as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    run()
