

cenaNettoJava = 10
cenaNettoAjax = 20
cenaNettoJablek = 1.02
cenaNettoBananow = 1.20
cenaNettoMiesa = 22.22


vat8 = 8
vat12 = 12
vat23 = 23
obliczonyVat23 = (1 + vat23 / 100)
obliczonyVat8 = 1 + vat8 / 100
obliczonyVat12 = 1 + vat12 / 100

cenaBruttoJava = cenaNettoJava * obliczonyVat23
cenaBruttoAjax = cenaNettoAjax * obliczonyVat23
cenaBruttoJablek = cenaNettoJablek * obliczonyVat8
cenaBruttoBananow = cenaNettoBananow * obliczonyVat8
cenaBruttoMiesa = cenaNettoMiesa * obliczonyVat12


print('Cena brutto Java = ',cenaBruttoJava)
print('Cena brutto Ajax = ',cenaBruttoAjax)
print('Cena brutto Jabłek = ',cenaBruttoJablek)
print('Cena brutto Bananów = ',cenaBruttoBananow)
print('Cena brutto Mięsa = ',cenaBruttoMiesa)





