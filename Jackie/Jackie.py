
class Adatok(object):
    def __init__(self, sor):
        split = sor.split('\t')
        self.year = int(split[0])
        self.races = int(split[1])
        self.wins = int(split[2])
        self.podiums = int(split[3])
        self.poles = int(split[4])
        self.fastest = int(split[5])

beolvas = open('jackie.txt',"r", encoding="utf-8")
lista = []
fejlec = beolvas.readline().strip()
for x in beolvas:
    lista.append(Adatok(x.strip()))
print("3. feladat: %d" %len(lista))
max = lista[0].races
maxev =lista[0].year
for x in lista:
    if(x.races>max):
        max = x.races
        maxev = x.year
print("4. feladat: %d" %maxev)
print("5. feladat: ")



nyert =0
szoveg =str(lista[0].year)[2]
for x in lista:
    if str(x.year)[2]!=szoveg:
        print("\t{}0-s évek: {} megnyert verseny".format(szoveg,nyert))
        szoveg=str(x.year)[2]
        nyert=0
        nyert+=x.wins
    else: 
        nyert+=x.wins
     
print("\t{}0-s évek: {} megnyert verseny".format(szoveg,nyert))


print("6. feladat: jackie.html")
kiir = open("jackie.html","w", encoding="utf-8")
kiir.write(""" 
    <!DOCTYPE html>
<html lang="hu">
<head>
    <style>
        td{
            border: 1px solid black;
        }
        
    </style>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jackie Stewart</title>
</head>
<body>
    <h1>Jackie Steward</h1>
 <tr>
    """)
for x in lista:
    kiir.write("""
    <table>
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    </table>""".format(x.year,x.races,x.wins))
kiir.write(""" 
</body>
</html>

""")
kiir.close()
 