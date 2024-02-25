import time
import pgzrun
WIDTH = 690
HEIGHT = 410

home = Actor("home")
home.pos = (150,273)

river =Actor("river")
river.pos = (670, 20)

rock = Actor("rock")
rock.pos = (200,50)


tree = Actor("tree")
tree.pos = (190,80)

tree2 = Actor("tree")
tree2.pos = (80,60)

tree3 = Actor("tree")
tree3.pos = (600,340)

rock = Actor("rock")
rock.pos = (630,250)

cat = Actor("cat")
cat.pos = (400,40)

cat2 = Actor("cat2")
cat2.pos = (60,190)

rakun = Actor("rakun")
rakun.pos = (600,160)

busra_animasyon_saga = ["right_1", "right_2", "right_3", "right_4"]
busra_animasyon_sola = ["left_1", "left_2", "left_3", "left_4"]
busra_animasyon_yukari = ["up_1", "up_2", "up_3", "up_4"]
busra_animasyon_asagi = ["down_1", "down_2", "down_3", "down_4"]
animasyon_indeksi = 0
animasyon_sayisi = len(busra_animasyon_saga)


busra = Actor(busra_animasyon_saga[0], (WIDTH/2, HEIGHT/2))

busra.prev_x, busra.prev_y = busra.x, busra.y # RAKUNA CARPISMA İCİN
rakun.prev_x, rakun.prev_y = rakun.x, rakun.y #  RAKUNA CARPISMA İCİN
tree.prev_x, tree.prev_y = tree.x, tree.y # tree carpısma icin
tree2.prev_x, tree2.prev_y = tree2.x, tree2.y # tree2 carpısma ıcın
tree3.prev_x, tree3.prev_y = tree3.x, tree3.y # tree3 carpısma icin
cat.prev_x, cat.prev_y = cat.x, cat.y # cat carpısma icin
cat2.prev_x, cat2.prev_y = cat2.x, cat2.y # cat2 carpısma icin
rock.prev_x, rock.prev_y = rock.x, rock.y # tree3 carpısma icin
river.prev_x, river.prev_y = river.x, river.y # tree3 carpısma icin
home.prev_x, home.prev_y = home.x, home.y # tree3 carpısma icin

baloncuk = Actor("baloncuk1")
baloncuk.pos = (110,380)
baloncuk2 = Actor("baloncuk2")
baloncuk2.pos = (305,382)
kalp = Actor("kalp_simge")
kalp.pos = (40,380)
yardimci = Actor("help",(470,380))
emoji = Actor("emoji")
emoji.pos = (238,380)

ada = Actor("ada", (300,210))

menu_start = False # menuyu kapatır
menu_screen = True # menu ekranda baslatır
yardim_al = False # yardımcıyı konusturur
yardim_bilgi = False

bilgi_menu = Actor("bilgi_menu", (WIDTH/2, HEIGHT/2))
balik = 0
seviye = 0
ada_gorev_1 = False
ada_son = True
cat_1_konusma = False
cat2_1_konusma = False
rakun_1_konusma = False
ilk_gorev = False
ilk_gorev_bitis = False
tas_efekt = False
agac_efekt = False
tas = 0
odun = 0
collision_occurred = False
ikinci_gorev = False
ilk_gorev_kapanis = False
eve_giris = False
river_efekt = False
cat_2_konusma = False
cat_gozukme = True
rakun_2_konusma = False

ask1 = Actor("ask")
ask1.pos = (400,40)
ask3 = Actor("ask")
ask3.pos = (60,190)
final = 0
ask2 = Actor("ask")
ask2.pos = (600,160)
cat2_gozukme = True
rakun_gozukme = True
son_mesaj = False
cat2_2_konusma = False
def draw():
    global menu_start, menu_screen, yardim_bilgi,cat2_gozukme, seviye, cat_1_konusma,cat_gozukme,cat2_2_konusma, rakun_gozukme, rakun_2_konusma, cat_2_konusma, cat2_1_konusma, balik, eve_giris,river_efekt, ikinci_gorev,ilk_gorev_kapanis, ada_son,ilk_gorev, ilk_gorev_bitis, tas_efekt, odun, tas, agac_efekt, collision_occurred
    if menu_screen == True:
        screen.blit("menu", (0,0))
        screen.draw.text("HOSGELDIN KUZUCUGUM, BASLAMAK ICIN SPACE'E BASABILIRSIN MUCK<3",(50,50))
        screen.draw.text("OYUN TUSLARI ICIN ALTTA BIR MELEK GORECEKSIN, O SANA YARDIM EDEBILIR<3", (20,100))

    if menu_start == True:
        screen.blit("garden", (0,0))
        river.draw()
        rock.draw()
        tree.draw()
        #tree2.draw()
        #tree3.draw()
        if cat_gozukme == True:
            cat.draw()
        if cat2_gozukme == True:
            cat2.draw()
        if rakun_gozukme == True:
            rakun.draw()
        yardimci.draw()
        if ada_son == True:
            ada.draw()
        busra.draw()
        baloncuk.draw()
        baloncuk2.draw()
        emoji.draw()
        kalp.draw()
        if son_mesaj == True:
            screen.draw.text("Seni Seviyorum Bitanem, Butun hayvanlarİ eve sokabildin, SEVGILILER GUNUN KUTLU OLSUN", (50,30),color="black" )
            screen.draw.text("PAT! KUT! BAM!", (255,367), fontsize=18, color="black")
            screen.draw.text("BIRAZ SERT BIR KAYA:", (230,340),fontsize=20, color="black")
        if agac_efekt == True:
            screen.draw.text("GUM! BAM! GUM!", (255,367), fontsize=18, color="black")
            screen.draw.text("AGAC YASKEN BILMEM NE OLUR:", (220,345), fontsize=17, color="black")



        if yardim_al == True: # yardımcıya yaklasınca yardım alıp alamayacagını sorar
            screen.draw.text("PERI:", (225,340), color="black")
            screen.draw.text("Merhaba Kucuk Hanim,\n Yardim mi Istiyorsun? 'Z'", (255,367), fontsize=15, color="black")
        if yardim_bilgi == True:
            bilgi_menu.draw()
            screen.draw.text("KONUSMA ICIN: 'Z'", (150,110))
            screen.draw.text("ETKILESIM ICIN ORN:(AGAC,ODUN,KAYA VS. 'X'", (150,130))
            screen.draw.text("SV: SEVGINI TEMSIL EDER, \n SEVGINI YUKSELTMEYE BAK", (150,150))
            screen.draw.text("ETKILESIM ICIN YAKLAS VE BIR\nTUSA BAS, FAZLA YAKLASIRSAN ITILIRSIN:(", (150,270))
            screen.draw.text("CIKIS ICIN 'E'\nKedilere balik vermek\nicin 'C'", (150, 190))
            if keyboard.e:
                yardim_bilgi = False
        screen.draw.text(f"Sv: {seviye}", (60,370), fontsize=25, color="black") #baloncugun ustune peri yazar

        if ada_gorev_1 == True:
            screen.draw.text(f"Sokakta kalamayiz, bizim\nIcin 10 Tas 10 Odunla ev Yap<3", (255,367), color="black", fontsize=15)
            screen.draw.text("ADA<3:", (225,340), color="black")

        if cat_1_konusma == True:
            screen.draw.text("Nazli Bir kedi gibi, Eminim\nSV 10 da birseyler mirildar", (255,367), fontsize=15, color="black")
            screen.draw.text("KEDI AMA CILVE YAPIYOR:", (220,340), color="black", fontsize=20)

        if rakun_1_konusma == True:
            screen.draw.text("Yavas Ol, Altina Yapacak,\n SV 20'de Sansini tekrar dene<3", (255,367), fontsize=15, color="black")
            screen.draw.text("RAKUN AMA KORKAK GIBI:", (220,340), color="black", fontsize=20)

        if cat2_1_konusma == True:
            screen.draw.text("Kendini Birsey Saniyor,\nSV 30'da Akli Basina Gelir", (255,367), fontsize=15, color="black")
            screen.draw.text("CINS VE EGOLU BIR KEDI:", (220,340), fontsize=20, color="black")

        screen.draw.text(f"ODUN: {odun}\nTAS: {tas}\nBALIK: {balik}", (120,363), fontsize=17, color="black")

        if ilk_gorev == True: # yeterli tas ve odun toplanırsa ev gelsin
            home.draw()
            ilk_gorev_bitis = True # bidaha ada tas ve odun istemesin

            if ilk_gorev == True and not collision_occurred: #eger ev gelmisse 1 arttırsın
                seviye+=1
                collision_occurred = True

        if ikinci_gorev == True:
            screen.draw.text("Eline Saglik<33 ben eve Gidiyorum, Malum\nOmrumun son zamanlari..", (255,367), fontsize=15, color="black")

        if ilk_gorev_kapanis == True: # eger son gorevdeyse
            if busra.colliderect(ada) and keyboard.z: #ve adaya yaklasıp z ye basarsa ada gitsin ve son sozunu soylesin
                ada_son = False



        if eve_giris == True: #eve yaklasıp z ye basıp girince menu ve bahcedekiler silinsin
            screen.blit("inhome", (0,0)) # evin gorunumu
            ada.pos = (460,230)
            ada.draw()
            ada_son = False
            if cat_gozukme == False:
                cat.draw()
                cat.pos = (420,255)
                ask1.pos = (700,700)
            if rakun_gozukme == False:
                rakun.draw()
                rakun.pos = (190,330)
            if keyboard.e: # evin icindeyken e ye basılırsa evden cıksın
                eve_giris = False
            if cat2_gozukme == False:
                cat2.draw()
                cat2.pos = (300,300)


        if cat_gozukme == False: # eger kedi giderse yerine kalp gelsin
            ask1.draw()

        if river_efekt == True:
            screen.draw.text("GLU! GLU! BLUP!", (255,367), fontsize=18, color="black")
            screen.draw.text("BIRAZ DERINE BENZIYOR:",(220,340), fontsize=20, color="black")

        if cat_2_konusma == True:
            screen.draw.text("Boyle guzel birinin evi Varken\n neden Hala Sokaktayim.\n Evde Gorusuruz<333",(255,367), fontsize=15, color="black")
            screen.draw.text("KEDI BIRAZ SEVDI GIBI:", (220,340), fontsize=20, color="black")
            cat_gozukme = False


        if rakun_2_konusma == True: # yeteri kadar balık aldıysa rakun gozukmesin
            rakun_gozukme = False

            screen.draw.text("Altina yapti, ama onemli degil\nSeni seviyor, ve artik evine\n iseyecek", (255,367), fontsize=15, color="black")
            screen.draw.text("UMARIM CIS TEMIZLEYEBILIYORSUNDUR:", (220,340), fontsize=17, color="black")
        if rakun_gozukme == False:
            ask2.draw()





        if cat2_2_konusma == True:
            cat2_1_konusma = False
            screen.draw.text("On Yargiyi bir kenara birakip\nSeni sevdigini soyledi",(255,367), fontsize=15, color="black")
        if cat2_2_konusma == True:
            cat2_gozukme = False
        if cat2_gozukme == False:
            ask3.draw()



def update():
    global son_mesaj
    hareket_ve_animasyon()
    menu()
    etkilesim()
    olay()
    inhome()

    if seviye>=30:
        son_mesaj = True


def menu(): # menu ekranı
    global menu_start
    if keyboard.space:
        menu_start = True
        menu_screen = False



def etkilesim():
    global yardim_al, yardim_bilgi, ada_gorev_1, cat_1_konusma, rakun_1_konusma,cat2_2_konusma, cat2_1_konusma,balik,river_efekt, tas, odun, tas_efekt, agac_efekt,ilk_gorev_kapanis, ilk_gorev_bitis, ikinci_gorev
    if busra.colliderect(yardimci): #yardımcıya yaklasınca yardım isteyio istemedgini sorar
        yardim_al = True

    if yardim_al == True and keyboard.z: #eger y ye basıp kabul edilmişse yardım sayfası acar
        yardim_bilgi = True

    if not busra.colliderect(yardimci): # eger yardımcıya yakın degil ve y ye basmıyorsa sormasın
        yardim_al = False


    if busra.colliderect(ada) and keyboard.z: #ADAYA YAKLASIR Z YE BASARSA TAS ODUN ISTESIN
        ada_gorev_1 = True

    if not busra.colliderect(ada): #UZAKLASIRSA İSTEMESİN
        ada_gorev_1 = False


    if busra.colliderect(cat) and keyboard.z: # eger kediye temas eder ve zye basarsa cat_1_konusma olsun
        cat_1_konusma = True
    if not busra.colliderect(cat): # eger uzaklasırsa olmasın
        cat_1_konusma = False


    if busra.colliderect(rakun) and keyboard.z: #rakuna deger ve z ye basarsa rakun_1_konusma olsun
        rakun_1_konusma = True
    if not busra.colliderect(rakun): #eger uzaklasırsa olmasın
        rakun_1_konusma = False

    if busra.colliderect(cat2) and keyboard.z: #cat2 ye deger ve z ye basarsa cat2_1_konusma olsun
        cat2_1_konusma = True
    if not busra.colliderect(cat2): #eger uzaklasırsa olmasın
        cat2_1_konusma = False

    if busra.colliderect(rock) and keyboard.x: # eger rocka deger ve x e basarsa tas_efekt yazısı gelsin ve tas artsın
        tas+=1
        tas_efekt = True
        time.sleep(0.6)
    if not busra.colliderect(rock): # eger rocktan uzaklasırsa olmasın
        tas_efekt = False

    if busra.colliderect(tree) and keyboard.x: #agaca yaklasırsa ve z ye basarsa odun artsın ve agac_efekt yazsın
        odun+=1
        time.sleep(0.6)
        agac_efekt = True

    if not busra.colliderect(tree): # eger uzaklasırsa calısmasın
        agac_efekt = False

    if ilk_gorev_bitis == True: #ilk gorev bittiginde odun ve tas toplandıgında ada_gorev_1 calısmasın ve bidaha istemesin
        ada_gorev_1 = False

    if ilk_gorev_kapanis == True:
        if busra.colliderect(ada) and keyboard.z:
            ikinci_gorev = True

    if not busra.colliderect(ada):
        ikinci_gorev = False


    if busra.colliderect(river) and keyboard.x: #nehire deger ve x e basarsa balik 1 artsın ve river_efekt ile yazı gelsin
        river_efekt = True
        balik+=1  # ve bir balık tutsun
        time.sleep(0.6)
    if not busra.colliderect(river):
        river_efekt = False




def olay():
    global ilk_gorev, ilk_gorev_kapanis, ada_gorev_1, balik, seviye, cat_1_konusma, cat_2_konusma, rakun_1_konusma, rakun_2_konusma, cat2_2_konusma
    if tas >=10 and odun >=10:
        ilk_gorev = True # agac gelsin, ve tas ve odun istemesin bidaha
        ilk_gorev_kapanis = True # artık son sozunu soyleyebilir ve yok olabilir

    if busra.colliderect(cat) and keyboard.c and balik >=5: # eger kediye degiyorsa c ye basıyosa ve balik 5 veya üstte ise seviye artsın balık dussun
        seviye+=3
        balik-=5
    if seviye >=10 and busra.colliderect(cat) and keyboard.z: #eger seviye 10 dan buyukse ve kediye z basılmıssa eski konusma gitsin yenisi gelsin
        cat_1_konusma = False
        cat_2_konusma = True
    if not busra.colliderect(cat):
        cat_2_konusma = False

    if busra.colliderect(rakun) and keyboard.c and balik >=5:
        seviye+=3
        balik-=5
    if seviye>=20 and busra.colliderect(rakun) and keyboard.z:
        rakun_1_konusma = False
        rakun_2_konusma = True
    if not busra.colliderect(rakun):
        rakun_2_konusma = False

    if busra.colliderect(cat2) and keyboard.c and balik>=5:
        seviye+=3
        balik-=5
    if busra.colliderect(cat2) and keyboard.z and seviye>=30:
        cat2_2_konusma = True
    if not busra.colliderect(cat2):
        cat2_2_konusma = False



def inhome():
    global eve_giris
    if busra.colliderect(home) and keyboard.x:
        eve_giris = True









def hareket_ve_animasyon(): # BUSRAYA HAREKET, YURUME ANİMASYONU VE CARPISMA ONLEMEYİ CALISTIRIR
    global animasyon_indeksi, animasyon_sayisi
    if keyboard.d:
        busra.x+=2
        animasyon_indeksi = (animasyon_indeksi +1) % animasyon_sayisi
        busra.image = busra_animasyon_saga[animasyon_indeksi]
    if keyboard.a:
        busra.x-=2
        animasyon_indeksi = (animasyon_indeksi +1) % animasyon_sayisi
        busra.image = busra_animasyon_sola[animasyon_indeksi]
    if keyboard.w:
        busra.y-=2
        animasyon_indeksi = (animasyon_indeksi +1) % animasyon_sayisi
        busra.image = busra_animasyon_yukari[animasyon_indeksi]
    if keyboard.s:
        busra.y+=2
        animasyon_indeksi = (animasyon_indeksi +1) % animasyon_sayisi
        busra.image = busra_animasyon_asagi[animasyon_indeksi]
    if not (keyboard.w or keyboard.a or keyboard.s or keyboard.d):
        busra.image = busra_animasyon_asagi[0]



    if busra.colliderect(rakun):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(tree):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(tree2):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(tree3):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(cat):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(cat2):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(river):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)

    if busra.colliderect(home):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2,0.01)

    if busra.colliderect(rock):
        move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, 0.01)



def move_back(busra,rakun, tree, tree2, tree3, cat,river, home, cat2, distance): # CARPISMA ONLEMEYI YAPAR YURUME ANİMASYON FONKSİYONUNDADIR
    if busra.x < rakun.x:
        busra.x -= distance
    else:
        busra.x += distance   # RAKUNA CARPMAYI ÖNLER
    if busra.y < rakun.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < tree.x:
        busra.x -= distance
    else:
        busra.x += distance   # TREE CARPMAYI ÖNLER
    if busra.y < tree.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < tree2.x:
        busra.x -= distance
    else:
        busra.x += distance   # TREE2 CARPMAYI ÖNLER
    if busra.y < tree2.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < tree3.x:
        busra.x -= distance
    else:
        busra.x += distance   # TREE3 CARPMAYI ÖNLER
    if busra.y < tree3.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < cat.x:
        busra.x -= distance
    else:
        busra.x += distance   # CAT CARPMAYI ÖNLER
    if busra.y < cat.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < cat2.x:
        busra.x -= distance
    else:
        busra.x += distance   # CAT2 CARPMAYI ÖNLER
    if busra.y < cat2.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < river.x:
        busra.x -= distance
    else:
        busra.x += distance   # river CARPMAYI ÖNLER
    if busra.y < river.y:
        busra.y -= distance
    else:
        busra.y += distance


    if busra.x < rock.x:
        busra.x -= distance
    else:
        busra.x += distance   # rock CARPMAYI ÖNLER
    if busra.y < rock.y:
        busra.y -= distance
    else:
        busra.y += distance



    if busra.x < home.x:
        busra.x -= distance
    else:
        busra.x += distance   # home CARPMAYI ÖNLER
    if busra.y < home.y:
        busra.y -= distance
    else:
        busra.y += distance


pgzrun.go()

















