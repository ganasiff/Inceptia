import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})


def is_product_available(product_name, quantity):
    """Function that checks the availability of choice of a product"""
    
    #Catches incorrect product name
    try:
        req_prod = _PRODUCT_DF.loc[_PRODUCT_DF.product_name == product_name,'quantity'].values[0]
    except:
        req_prod = -1
    #Checks for correct quantity input type
    try:
        quantity_clean = int(quantity)
        #Checks for product request vs stock
        if (req_prod-quantity_clean)>=0:
            return True
        else:
            return False
    except ValueError:
        #Input not convertible to int
        False


def list_products():
    """Function that returns an alphabetically ordered product list"""
    #Flavors in alphabetic order
    df = _PRODUCT_DF.sort_values(by=['product_name'])

    #Filter if there is no stock for selection
    df = df.query('quantity > 0')

    #Human readable names for columns, index strip
    df = df.rename(columns={"product_name":"Sabor","quantity":"Cantidad en Stock"})
    
    return df.to_string(index=False)
