from enum import Enum, unique


@unique
class KisiTip(Enum):
	KIRACI = 0
	SAHIBI = 1


class Site:
	def __init__(self, ad: str, adres: str, sehir: str) -> None:
		self.ad = ad
		self.adres = adres
		self.sehir = sehir


class Bina:
	def __init__(self, ad: str, blok: str, site: Site) -> None:
		self.ad = ad
		self.blok = blok
		self.site = site


class Daire:
	def __init__(self, no: int, kat: int, bina: Bina) -> None:
		self.no = no
		self.kat = kat
		self.bina = bina


class Kisi:
	def __init__(self, ad: str, daire: Daire, tip: KisiTip, tel: str) -> None:
		self.ad = ad
		self.daire = daire
		self.tip = tip
		self.tel = tel

	def toString(self) -> str:
		"Override method"
		# default arguments
		return '{}, {}, {}, {}'.format(self.ad, self.daire.no, self.tip.name, self.tel)
