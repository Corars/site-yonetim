from .Daire import *
from .KisiTip import *

class Kisi:
    def __init__(self, ad: str, daire: Daire, tip: KisiTip, tel: str) -> None:
        self.ad = ad
        self.daire = daire
        self.tip = tip
        self.tel = tel

    def toString(self) -> str:
        return str("{} ", self.ad, self.daire.no, self.tip.name, self.tel)