_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen","PASS"]

def validate_discount_code(discount_code):
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V',
    'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e',
    'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n',
    'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """

    final_diff=10000
    for code_word in _AVAILABLE_DISCOUNT_CODES:
        #Create and Reset buffer word list
        word_diff=[]
        #One way
        for char in discount_code:        
            if code_word.find(char) == -1:
                word_diff.append(char)
        #Reverse lookup
        for char in code_word:
            if discount_code.find(char) == -1:
                word_diff.append(char)            
        #Deduplicate characters that are different
        word_diff=list(set(word_diff))
        #Get quantity of characters that are different
        actual_difference = len(word_diff)
        #Checks if at least one code is OK
        if actual_difference < final_diff:
            final_diff = actual_difference
        else:
            actual_difference = final_diff  
    #If the discount code mismatch is less than three, it's OK  
    if final_diff < 3:
        #print(f"La diferencia final {final_diff}, es menor a 3")
        print("Codigo Válido")
        return True
    else:
        #print(f"La diferencia final {final_diff}, es mayor o igual a 3")
        print("Codigo Inválido")
        return False
