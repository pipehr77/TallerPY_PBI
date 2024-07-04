import random

def generarDatosProductos ():
    Productos=["Musica","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for Producto in Productos:
        ProductoP={}
        Categoria=random.choice(["Plus", "Mega", "Basic"])
        ProductoP=[Categoria,Producto]
        datos.append(ProductoP)
    return datos
print(generarDatosProductos())