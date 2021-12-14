from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
# Agregue esta libreria que ayuda a tener id unicos y me parece interesante
# por la seguridad de la información
from uuid import uuid4 as uuid


app = FastAPI()

# aqui estara la "base de datos"
products = []

#clase para la creación de los datos a capturar
class Producto(BaseModel):
    id: str
    # ademas de una ide unica es bueno tener un codigo del producto por el cual tambien pueda ser buscado
    cod_Producto: int
    nombre: str
    precio: float
    cantidad: int
    dioponible: bool
    # de esta forma condiciono la variable para que pueda estar vacia
    description: Optional[Text]
    # De esta forma obtenemos la fecha de creación y/o actualización
    created_at: datetime = datetime.now()


# ruta raiz
@app.get('/')
def read_root():
    return {"Welcome to my api"}

# metodo para crear productos
@app.post('/products')
def create(product: Producto):
    product.id = str(uuid())
    products.append(product.dict())
    #return products[-1]
    return f"Se a guardado el siguiente producto {products[-1]}"

# metodo para obtener un producto
@app.get('/products/{id_producto}')
def read_producto(id_producto:str):
    for product in products:
        if product['id'] == id_producto:
            return product
    raise HTTPException(status_code=404, detail="Product Not Found")

# metodo para actualizar
@app.put('/products/{id_producto}')
def update_product(id_producto:str, updateProduct:Producto):
    for idx, p in enumerate(products):
        if p['id'] == id_producto:
            products[idx]["cod_Producto"] = updateProduct.cod_Producto
            products[idx]["nombre"] = updateProduct.nombre
            products[idx]["precio"] = updateProduct.precio
            products[idx]["cantidad"] = updateProduct.cantidad
            products[idx]["dioponible"] = updateProduct.dioponible
            products[idx]["description"] = updateProduct.description
            products[idx]["created_at"] = updateProduct.created_at
            return {"message": "El producto fue actualizado exitosamente"}

# listar productos
@app.get('/products')
def list_products():
    return products

# Metodo para eliminar un producto
@app.delete("/products/{id_producto}")
def delete_product(id_producto:str):
    for idx, p in enumerate(products):
        if p['id'] == id_producto:
            products.pop(idx)
            return {"message": "El producto fue eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Product Not Found")
