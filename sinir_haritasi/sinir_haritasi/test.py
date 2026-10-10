# -*- coding: utf-8 -*-
"""Örnek raporlar: python -m sinir_haritasi.test"""
import os, json
from .puanla import puanla
from .rapor import rapor_pdf, koc_notu_pdf

os.makedirs("ornek", exist_ok=True)

# Örnek 1: aile ve kendine sızan, suçluluk baskın
c1 = {"a1":4,"a2":2,"a3":3,"a4":3,"a5":4,"a6":"a","a7":"d","a8":"d",
      "i1":1,"i2":1,"i3":2,"i4":1,"i5":2,"i6":"b","i7":"b","i8":"a",
      "r1":2,"r2":2,"r3":1,"r4":1,"r5":3,"r6":"b","r7":"d","r8":"a",
      "e1":2,"e2":2,"e3":2,"e4":1,"e5":1,"e6":"a","e7":"b","e8":"e",
      "n1":4,"n2":3,"n3":3,"n4":2,"n5":4,"n6":"a","n7":"c","n8":"c",
      "z1":"a","z2":"a","z3":"a","z4":"a","z5":"a","z6":"a","z7":"b","z8":"a",
      "cumle":"Annem bayramda bize gelin dedi, yorgundum ama peki dedim."}
s1 = puanla(c1)
rapor_pdf("Elif", s1, "ornek/ornek-elif.pdf", whatsapp_link="https://wa.me/905000000000")
koc_notu_pdf("Elif", "elif@example.com", s1, "ornek/koc-notu-elif.pdf")
print(json.dumps({k: s1[k] for k in ("alan_yuzde","tip_yuzde","baskin","ikinci","cift_kapi","oruntu","baglam","incele")}, ensure_ascii=False))

# Örnek 2: risk yolu (E5=4, E8=a)
c2 = dict(c1); c2.update({"e1":4,"e2":4,"e3":3,"e4":3,"e5":4,"e6":"a","e7":"d","e8":"a","cumle":"Hayır dediğimde bağırıyor, sonra günlerce konuşmuyor."})
s2 = puanla(c2)
rapor_pdf("Deniz", s2, "ornek/ornek-deniz.pdf")
koc_notu_pdf("Deniz", "deniz@example.com", s2, "ornek/koc-notu-deniz.pdf")
print("risk:", s2["bayraklar"], "incele:", s2["incele"], "oruntu:", s2["oruntu"])

# Örnek 3: tutuyor profili
c3 = {k: (0 if isinstance(v, int) else "b") for k, v in c1.items() if k != "cumle"}
c3.update({"e8":"e","a1":1,"n2":2,"z1":"a","z2":"b","z3":"a","z4":"b","z5":"a","z6":"b","z7":"a","z8":"b","cumle":""})
s3 = puanla(c3)
rapor_pdf("Ayşe", s3, "ornek/ornek-ayse.pdf")
print("tutuyor:", s3["tutuyor"], s3["alan_yuzde"])
