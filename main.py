import modules.utils as utils
import modules.logo as logo
import modules.gen as gen
import modules.help as help
from rich import print
from sys import argv

utils.clear()
logo.printlogo()

try:
    cardtype = argv[1]
    
    counter = int(argv[2])
    
    month = argv[3]
    if month.lower() == "random":
        month = gen.gendata("month")
    
    year = argv[4]
    if year.lower() == "random":
        year = gen.gendata("year")

    cvv = argv[5]
    if cvv.lower() == "random":
        cvv = gen.gendata("")
    
    savefile = argv[6]
except:
    help.showhelp()
    exit()

print(f"""[bold green]Stats[reset][white]:
[bold white]- [green]Card/Bin[white]: {cardtype}
[bold white]- [green]Count[white]: {str(counter)}
[bold white]- [green]Month[white]: {month}
[bold white]- [green]Year[white]: {year}
[bold white]- [green]Cvv[white]: {cvv}
[bold white]- [green]Savefile[white]: {savefile}
\n[reset][green][[bold white]+[reset][green]] [bold white] Generating...\n
""")

if savefile != "none":
    f = open(savefile,"a")
for x in range(counter):
    generated = gen.generate_card(cardtype,16)
    card = f"{generated}|{month}|{year}|{cvv}"
    print("[bold green]"+card)
    if savefile != "none":
        f.write(card+"\n")
print("\n[reset][green][[bold white]*[reset][green]] [bold white] Done!")
if savefile != "none":
    f.close()
utils.removedoublelines(savefile)
exit()