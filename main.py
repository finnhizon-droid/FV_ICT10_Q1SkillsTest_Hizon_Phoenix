#Reciept Generator #Skills Test
from pyscript import display, document


def generate(e):
    document.getElementById("order").innerHTML = ""


    prod1 = document.getElementById("sweet1")
    
    prod2 = document.getElementById("sweet2")
    
    prod3 = document.getElementById("sweet3")
    
    prod4 = document.getElementById("sweet4")
    
    prod5 = document.getElementById("sweet5")
   
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked
   
    vat = subtotal * 0.12

    grand_total = subtotal + vat
    
    display(f"Subtotal: {subtotal}", target="food")
    display(f"VAT: {vat}", target="food")
    display(f"Grand Total: {grand_total}", target="food")
