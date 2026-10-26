# Working With Sets
from pyscript import display, document

# Members from G7-10
G7Club = {"Ryan Foster", "Olivia Hayes", "Sarah Morgan", "Megan Cooper"}
G8Club = {"Daniel Brooks", "Hannah Mitchell", "Ethan Parker", "Chloe Bennett"}
G9Club = {"Mateo Gozun", "Qualaen Mate", "Zadie Zagala", "Emily Carter"}
G10Club = {"Jaena Ambata", "Guia Dahap", "Chelsea Nortiga"}

AllMembers = G7Club | G8Club | G9Club | G10Club   # joins members from g7-10

# Adds users to the club list
def submit_name(e):
     document.getElementById('result').innerHTML = ' '

     # Name input
     firstname_input = " ".join(document.getElementById('firstname').value.strip().split())    # removes extra spaces
     lastname_input = " ".join(document.getElementById('lastname').value.strip().split())
     fullname = ((firstname_input + " " + lastname_input).title())

     AllMembers.add(fullname)      # adds typed name to set
     SortedMembers = "\n".join(sorted(AllMembers))     # sorts members alphabetically and puts each name on separate lines

     display(f"{SortedMembers}\n\nTotal Members: {len(AllMembers)}", target='result')     # displays all members and total number of members