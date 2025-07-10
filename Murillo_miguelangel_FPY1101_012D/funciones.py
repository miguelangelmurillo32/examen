

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}


def stock_marca(marca):
    total_stock = 0
    marca = marca.lower()  
    for model, details in productos.items():
        if details[0].lower() == marca:  
            total_stock += stock[model][1]
    print(f"el stock es: {total_stock}")


def busqueda_precio(p_min, p_max):
    modelos_en_rango = []
    for model, details in productos.items():
        precio = stock[model][0]
        if p_min <= precio <= p_max and stock[model][1] > 0:  
            modelos_en_rango.append(f"{details[0]}--{model}")
    
    modelos_en_rango.sort()  
    if modelos_en_rango:
        print("los notebooks entre los precios consultados son:", modelos_en_rango)
    else:
        print("no hay notebooks en ese rango de precios.")


def actualizar_precio(modelo, precio_nuevo):
    if modelo in stock:
        stock[modelo][0] = precio_nuevo
        return True
    else:
        return False


def pedir_precio(mensaje):
    while True:
        try:
            precio = int(input(mensaje))
            return precio
        except ValueError:
            print("debe ingresar valores enteros!!")


def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        
        elif opcion == "2":
            p_min = pedir_precio("Ingrese precio mínimo: ")
            p_max = pedir_precio("Ingrese precio máximo: ")
            busqueda_precio(p_min, p_max)
        
        elif opcion == "3":
            modelo = input("Ingrese modelo a actualizar: ")
            nuevo_precio = pedir_precio("Ingrese precio nuevo: ")
            if actualizar_precio(modelo, nuevo_precio):
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
            
            actualizar_otro = input("Desea actualizar otro precio (s/n)?: ")
            if actualizar_otro.lower() != 's':
                continue
        
        elif opcion == "4":
            print("Programa finalizado.")
            break
        
        else:
            print("Debe seleccionar una opción válida!!")

main()











