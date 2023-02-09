from rich import print
from sys import argv
import modules.gen as gen

newline = "\n"

def showhelp():    
    print(f"""[bold white]Help [reset][green]menù

[bold green]Usage[reset][white]:
[bold white]- [green]python3 [reset][white]{argv[0]} [green]([white]cardtype/bin[green]) ([white]count[green]) ([white]month/random[green]) ([white]year/random[green]) ([white]cvv/random[green]) ([white]savefile/none[green])

[bold green]Card types[reset][white]:
{str(gen.card_types).replace("[","[bold green]["+newline+"  [reset]").replace(",","[bold green],"+newline+" [reset]").replace("']","'"+newline+"[bold green]]").replace("'","[bold green]'[reset]")}

[bold green]Example[reset][white]:
[bold white]- [green]python3 [reset][white]{argv[0]} mastercard 10 06 random 456 save.txt
    
    """)