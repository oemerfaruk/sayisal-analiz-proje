us = [] #Denklemdeki kuvvetlerinin tutulduğu liste
katsayı = [] #Denklemdeki katsayıların tutulduğu liste

def denklem(): #denklem oluşturulması
    while(True):
        katsayı.append(int(input("Katsayıyı girin: "))) 
        us.append(int(input("üs girin: ")))
        
        x = input("Devam etmek istemiyorsanız 'e' tuşlayın\t")
        print("---------------------")
        if(x == "e" or x == "E"): #e karakteri dışındaki girişlerde denklem için katsayı ve kuvvet almaya devam edilir
            break
        
def turev():
    n = 0
    for i in katsayı:
        katsayı[n] = katsayı[n] * us[n] #katsayı listesinin n. elemanı ile us listesinin n. elemanı çarpılır ve katsayı listesinin n. elemanına eşitlenir.
        us[n] = us[n] - 1 #us listesinin n. elemanı 1 azaltılarak kendisine eşitlenir.
        n = n + 1;
    print("Türevli denkem\n")
    goster()
    
    
def sonuc():
    sonuc, n = 0, 0
    z = int(input("Bilinmeyen değeri: "))
    for i in katsayı: #tüm katsayı listesi dolaşılarak bilinmeyen denkleme dahil edilir
        sonuc = sonuc + (katsayı[n] * (z ** us[n]))
        n = n + 1
    print("sonuç: ",sonuc)
    


def goster(): #denklemdeki katsayı ve üsler gösterilir
    n = 0
    for i in katsayı:
        print("Katsayı: ",katsayı[n],"\t","Üs: ",us[n])
        n = n + 1;
    print("--------------------------------------")


def main():
    denklem()
    goster()
    derece = int(input("Kaç defa türev alınsın?\t"))
    for i in range(derece): #Derecenin değeri kadar türev fonksiyonu çalışır
        turev()
    sonuc()

main()
