import pygame  # impordime pygame mooduli

pygame.init()  # käivitame pygame mooduli

ekraan = pygame.display.set_mode([640, 480])  # määrame ekraani suuruse ja omistame muutujasse ekraan
pygame.display.set_caption("Ülesanne 2: Tekstide ja piltide kasutamine")  # määrame ekraanie pealkirja
taust = pygame.image.load("pildi_failid/bg_shop.jpg")  # muutuljale taustapilt omistame pildifaili väärtuse
ekraan.blit(taust, [0, 0])  # kuvame ekraanil taustapildi faili kordinaatidega 0,0

myygimees = pygame.image.load("pildi_failid/seller.png")  # muutuljale myygimees omistame pildifaili väärtuse
laius = myygimees.get_width()  # loeme myygimees muutujas oleva pildifaili laiuse
korgus = myygimees.get_height()  # loeme myygimees muutujas oleva pildifaili kõrguse
myygimees = pygame.transform.scale(myygimees, [laius / 3.5, korgus / 3.5])  # teeme myygimehe muutjas oelva pildifaili 3.5 korda väiksemaks
ekraan.blit(myygimees, [100, 150])  # kuvame ekraanil myygimehe pildi faili kordinaatidega 100,150

mull = pygame.image.load("pildi_failid/chat.png")  # muutuljale mull omistame pildifaili väärtuse
laius = mull.get_width()  # loeme mull muutujas oleva pildifaili laiuse
korgus = mull.get_height()  # loeme mull muutujas oleva pildifaili kõrguse
mull = pygame.transform.scale(mull, [laius / 1.2, korgus / 1.2])  # teeme myygimehe muutjas oleva pildifaili 1.2 korda väiksemaks
ekraan.blit(mull, [250, 50])  # kuvame ekraanil mull pildi faili kordinaatidega 250,50

font = pygame.font.Font(pygame.font.match_font('Comic Sans'),
                        20)  # määrame muutujale "font" suuruseks 35 ja fondiks "Comic Sans"
tekst = font.render("Tere, olen Asko Aru", True, [255, 255, 255])  # määrame muutujale "tekst" väärtuseks lause mille värv on kollane
ekraan.blit(tekst, [275, 125])  # kuvame ekraanil teksti kordinaatidega 275,125

pygame.display.flip()  # värskendame tervet ekraani

while True:  # nii kaua, kui tsükkel on tõene,
    for syndmus in pygame.event.get():  # sükkli muutujale omistatakse kõik pygame.event.get() väärtused
        if syndmus.type == pygame.QUIT:  # kui tsüklimuutuja syndmus tüüp võrdub pygame.QUIT
            pygame.quit()  # sugelem pygame
            exit()  # lõpetame programmi
