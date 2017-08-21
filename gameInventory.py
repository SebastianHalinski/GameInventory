# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Displays the inventory.
def display_inventory(inventory):
    print('Inventory:')
    for i in inventory:
        print(str(inventory[i]) + " " + str(i))
    total = list(inventory.values())
    print("Total number of items: " + str(sum(total)))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
            if i in inventory:
                inventory[i] += 1
            else:
                inventory[i] = 1
    return inventory

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    total = list(inventory.values())
    table = list(inventory)
    space = []
    for k in range(len(table)):
        space.append(len(table[k]))
    space.sort()
    print('Inventory:')
    print("count" + " "*(max(space) - 5) + 'item name')
    print("---------" + "-" * max(space))
    if order == None:
        for i in inventory:
            print((str(inventory[i])).rjust(2) + " "*(max(space)-2) + (str(i)).rjust((max(space))))
    elif order == "count,asc":
        for key , value in sorted(inventory.iteritems(), key=lambda (k, v): (v, k), reverse = False):
            sep = ''
            obj = [str(value), str(key)]
            print(sep.join(str(value)).rjust(2) + " "*(max(space)-2) + sep.join(str(key)).rjust(max(space)))
    elif order == "count,desc":
        for key , value in sorted(inventory.iteritems(), key=lambda (k, v): (v, k), reverse = True):
            sep = ''
            obj = [str(value), str(key)]
            print(sep.join(str(value)).rjust(2) + " "*(max(space)-2) + sep.join(str(key)).rjust(max(space)))
    print("---------" + "-" * max(space))
    print("Total number of items: " + str(sum(total)))
    pass


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import csv
    path =r'/home/sebastian/Dokumenty/Si week3/python-game-inventory-SebastianHalinski-master/import_inventory.csv'
    with open(path, 'rb') as filecsv:
        goblin_loot = csv.reader(filecsv)
        for row in goblin_loot:
            for i in row:
                    if i in inventory:
                        inventory[i] += 1
                    else:
                        inventory[i] = 1
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    import csv
    path =r'/home/sebastian/Dokumenty/Si week3/python-game-inventory-SebastianHalinski-master/export_inventory.csv'
    with open(path, 'w') as filecsv:
        w = csv.writer(filecsv)
        w.writerow([inventory])
    pass


# Main function sets initial variables and stores rest of the functions
def main(inventory):
    inventory = inv
    print_table(inventory, order="count,asc")
    print_table(inventory, order="count,desc")
    print_table(inventory, order=None)
    import_inventory(inventory, filename="import_inventory.csv")
    print_table(inventory, order="count,desc")
    export_inventory(inventory, filename="export_inventory.csv")
    pass

main(inv)
