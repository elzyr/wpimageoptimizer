import os
from PIL import Image


def oblicz_wage(directory):
    size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size

def optimize(path):
    res = []
    size_przed = oblicz_wage(path)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jpeg"):
                res.append(os.path.join(root, file))
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jpg"):
                res.append(os.path.join(root, file))
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                res.append(os.path.join(root, file))

    for zdjecie in res:
        wagaprzed=int(os.path.getsize(zdjecie))
        image = Image.open(zdjecie)
        w,h=image.size
        aspect=h/w

        if w>1920:
            print('zdjecie za duże, skaluje')
            new_width=1920
            new_height=new_width*aspect
            image.thumbnail((new_width,new_height))

        image.save(zdjecie,optimize=True,quality=20,resample=1)
        wagapo=int(os.path.getsize(zdjecie))
        roznica_wag=round((1-(wagapo/wagaprzed))*100,2)

        if roznica_wag>0:
            print('zmniejszyłem wage pliku o ' + zdjecie + " o " + str(roznica_wag)+ "%")

    print('\nkoniec, folder jest lzejszy o: ' + str(round((size_przed - oblicz_wage(path)) * pow(10, -6),2)) + "MB")
    koniec=input('czy chcesz zoptymalizować więcej folderów?(Y/N): ').capitalize()

    if koniec =="Y":
        start = input('podaj sciezke: ')
        optimize(start)

    else:
        return 0

print('wersja 0.1KW')
print('program obsługuje pliki typu JPG, PNG, JPEG')
start = input('podaj sciezke bezwzględną: ')
optimize(start)