inventario=[]

def menu_principal():
    """
    Muestra el menu princial
    """
    while True:
        print("Menu_princpal")
        print("0.Saludar")
        print("1.Agregar producto")
        print("2.Mostrar Inventario")
        print("3.Vender producto")
        print("4.Salir")
        
        opcion= input("seleccione una opcion")
        
        if opcion=="1":
            agregar_producto()
        elif opcion=="2":
            mostrar_inventario()
        elif opcion=="3":
            vender_producto()
        elif opcion=="4":
            break
        else:
            print("opcion no valida,Por favor intente otra vez")
            
def agregar_producto():
    """
    Agregar un nuevo producto al inventario
    """
    
    
 
    nombre= input("ingrese el nombre del producto")  
    precio= float(input("ingrese el precio del producto"))
    cantidad=int(input("ingrese la cantidad del producto"))    
    
    
    producto={"nombre":nombre,"precio":precio,"stock":cantidad}
              
    inventario.append(producto)
    print (f"producto{nombre} agregado al inventario") 
    print (inventario)  
    
def mostrar_inventario():
    """
    Muestra todos los productos del inventario
    """
    
    if inventario.count()==0:
        print ("el inventario esta vacio")
    else:
        print  ("presentando inventario")
        
        for  producto in inventario: 
            print (f"Nombre:{producto['nombre']},precio:{producto['precio']}, cantidad:{producto['stock']}")
            
            
def vender_producto():
    """
Vende un producto, actualiza el inventario y muestra el total de la venta
    """

nombre = input("Ingrese el nombre del producto que desea vender: ")
for producto in inventario:
    if producto["nombre"] == nombre:
        cantidad = int(input(f" ¿Cuantas unidades de {nombre} desea vender?: "))
        if cantidad <= producto["stock"]:
            producto ["stock"] -= cantidad
            total = cantidad * producto ["precio"]
            print(f"Venta realizada. Total: ${total: 2f}")
    
            if producto ["stock"] == 0:
                print(f"El producto {nombre} se ha agotado.")
                
            return
        else:
            print ("No hay suficiente Stock en Inventario")
            return


print("Producto no encontrado en el inventario")    

menu_principal()       
            
                           