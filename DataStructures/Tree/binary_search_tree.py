
from DataStructures.Tree import bst_node as bst_node

def new_map():
    """
    
    Crea una tabla de simbolos ordenada basada en un árbol binario de búsqueda (BST) vacía

    Se crea una tabla de símbolos ordenada con los siguientes atributos:
    
    """
    
    bst = {"root": None, "type": "BST"}
    
    return bst 


def insert_node(root, key, value):
    
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    """
    root["key"] = key
    root["value"] = value
    root["size"] += 1   




def put(my_bst, key, value):
    raiz = my_bst["root"]
    if raiz["value"] is None:
        insert_node(key, value) 
    if key < raiz["key"]:
        put(raiz["izquierda"])
    if key > raiz["key"]:
        put(raiz["derecha"])        
        
    return my_bst   



def remove_node(root, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Es usada en la función remove()
    """
    root["key"] = "__EMPTY__"
    root["value"] = None   
    
    
    


def remove(my_bst, key):
    
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Usa la función remove_node() para eliminar la pareja
    """
    raiz = my_bst["root"]
    if raiz["key"] == key: 
        remove_node(raiz)
    if raiz["key"] < key:
        remove(raiz["derecha"],key)
    if raiz["key"] > key:
        remove(raiz["izquierda"],key)
    
    

