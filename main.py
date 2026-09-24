#Reciept Generator #Skills Test
from pyscript import display, document



prices = {
    "sweet1": (110.00, "Banana Loaf Cakes (3 pcs)"), #assigning prices to each item on the menu
    "sweet2": (105.00, "Chocolate Chip Cookies (4 pcs)"),
    "sweet3": (115.00, "Cinnamon Rolls (3 pcs)"),
    "sweet4": (110.00, "Crinkle Cookies (4 pcs)"),
    "sweet5": (110.00, "Chocolate Muffins (2 pcs)"),
}


def generate(e):
    document.getElementById("subtotal").innerHTML = "" #clearing div outputs
    document.getElementById("tax").innerHTML = ""
    document.getElementById("total").innerHTML = ""

    subtotal = 0.0

    if document.getElementById("sweet1").checked: #checking to see if the checkbox is checked & adding their prices to subtotal
        subtotal = subtotal + prices["sweet1"][0]
        
    if document.getElementById("sweet2").checked:
        subtotal = subtotal + prices["sweet2"][0]

    if document.getElementById("sweet3").checked:
        subtotal = subtotal + prices["sweet3"][0]

    if document.getElementById("sweet4").checked:
        subtotal = subtotal + prices["sweet4"][0]

    if document.getElementById("sweet5").checked:
        subtotal = subtotal + prices["sweet5"][0]


    tax = subtotal * 0.12 #calculating the tax of 12%

    total = subtotal + tax #adding the subtotal and tax to get the total

    display(f"Subtotal: ₱{subtotal:.2f}", target="subtotal") #displaying the total to the divs in the html file
    display(f"Tax: ₱{tax:.2f}", target="tax")
    display(f"Total: ₱{total:.2f}", target="total")
