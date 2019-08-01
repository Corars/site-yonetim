import os, sys

root = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.insert(0, root)


from BL.Entity.Kisi import *
from BL.Entity.Daire import *
from BL.Entity.Bina import *
from BL.Entity.Site import *

sitemiz = Site("Bilimkent", "75.Yıl Mh Bekir Sıtkıpaşa Cd No 35", "Kütahya")
binamiz = Bina("Apartman", "A", sitemiz)
dairemiz = Daire(2, 1, binamiz)

ilyas = Kisi("İlyas Nuhoğlu", dairemiz, 1, "05306845433")
ozlem = Kisi("Özlem Nuhoğlu", dairemiz, 0, "05445263982")


print(ozlem.daire.no)