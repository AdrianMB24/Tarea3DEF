from PIL import Image
from playsound import playsound
from tabulate import tabulate
import sys

def Imagen(size, imagen):
    try:
        img = Image.open(imagen)
    except:
        print("Imagen No Encontrada")
        sys.exit(1)
    x = len(imagen)
    x1 = imagen[x-3]+imagen[x-2]+imagen[x-1]
    if (x1 == "jpg"):
        print("El archivo es formato jpg")
    else:
        print("El archivo no es formato jpg")
        sys.exit(1)
        
    ancho, alto = img.size
    if (size == 1):
        img.show()
    elif (size == 0.5):
        img2 = img.copy()
        img2.thumbnail((ancho//2, alto//2))
        img2.show()
    elif (size == 2):
        img3 = img.copy()
        img3.thumbnail((ancho*2, alto*2))
        img3.show()    
    
def Sonido(Cant, Sound):
    x = len(Sound)
    x1 = Sound[x-3]+Sound[x-2]+Sound[x-1]
    if (x1 == "mp3"):
        print("El archivo es formato mp3")
    else:
        print("El archivo no es formato mp3")
        sys.exit(1)
    for i in range (0, Cant):
        try:
            playsound(Sound)
        except:
            print("Sonido No Encontrado")
            sys.exit(1)
        
def Analizador(Texto):
    cont = 0
    l1 = ""
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    try:
        fic = open(Texto , "r")
    except:
        print("Doumento No Encontrado")
        sys.exit(1)
    lines = fic.readlines()
    l0 = str(lines[0])
    i = 0
    fic.close()
    while (1):
        if (l0[i] == "_"):
            z = 0
            for l in range (0, len(l2)-1):
                if (l2[l] == l1):
                    l3[l] = l3[l] + 1
                    z = 1
                    break
            if(z == 0):
                l2.append(l1)
                l3.append(1)
            l1 = ""
        else:
            l1 = l1 + l0[i]
        i = i+1
        try:
            l0[i]
        except:
            break
    for p in range (0, len(l2)-1):
        #l4.append(l2[p])
        #l4.append(13[p])
        l4 = [l2[p], l3[p]]
        l5.append(l4)
    Sal = open("Analizado.txt", "w")
    Sal.write(tabulate(l5, ["Item", "Cantidad"],tablefmt="github"))
    Sal.close()
        
            
    
