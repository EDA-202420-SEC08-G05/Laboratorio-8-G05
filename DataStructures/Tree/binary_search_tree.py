
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
    #if root is not None:
        
    #if root["key"] is not None:
    if root is None:
        root_new = bst_node.new_node(key, value)
           
                
        #root_new["key"] = key
        #root_new["value"] = value  
                
        return root_new      
    
    else:
              
            if root["key"] == key:
                    
                    #root["key"] = key
                    root["value"] = value
                
            else:
                    
                    root["key"] = key
                    root["value"] = value  
                
            return root            




def put(my_bst, key, value):
    
    if my_bst["root"] is None:
        my_bst["root"] = insert_node(my_bst["root"],key,value)  
        
    elif my_bst["root"]["key"] == key :
        my_bst["root"]["value"] = value
        
    elif my_bst["root"]["value"] > value and my_bst["root"]["left"]== None:
        root_new = bst_node.new_node(key, value)
        my_bst["root"]["left"] = insert_node(root_new,key,value)    
        
        
    elif my_bst["root"]["value"] < value  and my_bst["root"]["right"]== None:
        root_new = bst_node.new_node(key, value)
        my_bst["root"]["right"] = insert_node(root_new,key,value)
    
    return my_bst



def remove_node(root, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Es usada en la función remove()
    """
    
    
    
    


def remove(my_bst, key):
    
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Usa la función remove_node() para eliminar la pareja
    """
    
    
    
    

