from prettytable import PrettyTable


x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

table = PrettyTable()
table.align = "l"
table.border = True

table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)

