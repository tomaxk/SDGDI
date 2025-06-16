"""

Cambiar listas por diccionarios []
Cambair las funciones para que ocupen diccionarios []
Busqueda de diccionarios dentro de listas []
Agregar el procesamiento de codigos de productos []

"""


opcion=0

lista_productos=[]
#producto={'nombre':nombre,'cantidad':stock,'precio':precio}

def solicitarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return [nombreProd,precioProd,stockProd]
    except ValueError:
        print("Debe ingresar valores numericos positivos")


def buscarProducto(nombre):

    for producto in lista_productos:
        if producto['nombre'].lower()==nombre.lower():
            return producto
        
    return None

def guardarProducto(nombre,precio,stock):

    if buscarProducto(nombre)==None:
        producto={
            'nombre':nombre,
            'cantidad':stock,
            'precio':precio}
        lista_productos.append(producto)
        print('producto guardado con exito')
    else:
        print('Ya exite un producto con ese nombre')

def actualizarProducto(nombre,nuevoStock,nuevoPrecio):
    
    productoBuscado= buscarProducto(nombre)
    if productoBuscado!=None:
        indice= lista_productos.index(productoBuscado)
        productoBuscado['cantidad']=nuevoStock
        productoBuscado['precio']=nuevoPrecio
        #actualizar el producto en la lisa de productos
        lista_productos[indice]=productoBuscado
        print(f'El producto {nombre} actualizado con exito')
    else:
        print(f'El producto no existe')


def mostrarInventarioCompleto():
    for producto in lista_productos:
        print('-'*60)
        print(f'Nombre: {producto['nombre']} \t\tPrecio: ${producto['precio']} \t\tCantidad: {producto['cantidad']}')
        print('-'*60)



while opcion!="6":
    print("**************Menu de gestion de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opcion que desea(1-6): ")

    match opcion:
        case "1":
            infoProdcuto=solicitarProducto()
            if infoProdcuto!=None:
                guardarProducto(infoProdcuto[0],
                                infoProdcuto[1],
                                infoProdcuto[2])
        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print('-'*60)
                print(f"Nombre: {productoEncontrado['nombre']} \t\t Precio: ${productoEncontrado['precio']} \t\t Stock: {productoEncontrado['cantidad']}")
                print('-'*60)
        case '3':
            infoProdcuto=solicitarProducto()  
            if infoProdcuto!=None:
                actualizarProducto(nombre=infoProdcuto[0],nuevoStock=infoProdcuto[1],nuevoPrecio=infoProdcuto[2])
        case '4':
                mostrarInventarioCompleto()

