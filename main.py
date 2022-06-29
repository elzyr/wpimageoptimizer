import os
from PIL import Image
import shutil


def oblicz_wage(directory):
    size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(('.png', '.jpg', '.jpeg')):
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
    return size

def optimize(path):
    os.mkdir('tempfolder')
    res = []
    size_przed = oblicz_wage(path)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
                res.append(os.path.join(root, file))
    print('znalazlem '+str(len(res))+" zdjec")

    for zdjecie in res:
        image_name=zdjecie.split('\\')[-1]
        wagaprzed=int(os.path.getsize(zdjecie))
        image = Image.open(zdjecie)
        image.save('tempfolder\\'+image_name,optimize=True,quality=90)
        wagapo=int(os.path.getsize('tempfolder\\'+image_name))
        roznica_wag=round((1-(wagapo/wagaprzed))*100,2)

        if roznica_wag>0:
            print('zmniejszyłem wage pliku o ' + zdjecie + " o " + str(roznica_wag)+ "%")
            image.save(zdjecie, optimize=True, quality=90)

    os.system('optimize-images '+path)

    print('\nkoniec, folder jest lzejszy o: ' + str(round((size_przed - oblicz_wage(path)) * pow(10, -6),2)) + "MB ("+str(round((1-(oblicz_wage(path)/size_przed))*100,2))+"%)")

    shutil.rmtree('tempfolder', ignore_errors=True)

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