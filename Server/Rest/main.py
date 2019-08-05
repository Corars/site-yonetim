# import os, sys
# root = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
# sys.path.insert(0, root)

from Entity import KisiTip, Site, Bina, Daire, Kisi

sitemiz = Site("Bilimkent", "75.Yıl Mh Bekir Sıtkıpaşa Cd No 35", "Kütahya")
binamiz = Bina("Apartman", "A", sitemiz)
dairemiz = Daire(2, 1, binamiz)

ilyas = Kisi("İlyas Nuhoğlu", dairemiz, KisiTip.SAHIBI, "05306845433")
ozlem = Kisi("Özlem Nuhoğlu", dairemiz, KisiTip.KIRACI, "05445263982")

print(ilyas.toString())
print(ozlem.tip.name)