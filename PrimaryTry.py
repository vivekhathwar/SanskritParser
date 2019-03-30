# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:29:43 2018

@author: HATHWAR
"""

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def iterh(a):
    part=a[slice(-2,len(a),1)]
    if(part=='aH'):
        if(a[-3]=='y'):
            return("Chaturthi/Panchami-bahu")
        else:
            return("Prathama-eka")
    elif(part=='AH'):
        if(a[-3]=='y'):
            return("Panchami/Shasti-eka")
        else:
            return("Prathama-bahu")
    elif(part=="oH"):
        return("Shasti/Saptami-dvi")
    elif(part=='iH'):
        if(a[-3]=='a' or a[-3]=='h'):
            return("Truteeya-bahu")
        return("prathama-eka")
    elif(part=='IH'):
        return("Dviteeya-Bahu")

def iterm(a):
    part=a[slice(-2,len(a),1)]
    if(part=="Am" or part=='AM'):
        if(a[-3]=='y'):
            if(a[-4]=='A'):
                return("Saptami-eka")
            if(a[-4]=='h'):
                return("Truteeya/Chaturthi/Panchami-dvi")
            return("saptami-eka")
        elif(a[-3]=='N' or a[-3]=='n'):
            return("Shasti-bahu")
    return("Dviteeya-eka")

def itera(a):
    part=a[slice(-3,len(a),1)]
    if(part=="sya"):
        return("Shasti-eka")
    if(part=='Aya'):
        return("Chaturthi-eka")
    if(part=='eNa'):
        return("truteeya-eka")

def iteru2(a):
    part=a[-2]
    if(part=='a'):
        return("Prathama/Dwiteeya-Dvi")
    if(part=='S' or part=='s'):
        return("sapthami-bahu")

def iterA(a):
    if(a[-2]=='y'):
        return("Truteeya-eka")
    elif(a[-2]=='N'):
        return("Truteeya-eka")
    return('prathama-eka')
def itere(a):
    if(a[-2]=='y'):
        return("Chaturti-eka")
    else:
        return("Saptami-eka")
def vibhakthi(a):
    part=a[-1]
    if(part=='N'):
        return("Truteeya-Eka")
    if(part=='n'):
        return("Dwiteeya-Bahu")
    if(part=='t'):
        return("Panchami-Eka")
    if(part=='e' or part=='E'):
        return(itere(a))
    if(part=='u'):
        return(iteru2(a))
    if(part=='a'):
        return(itera(a))
    if(part=='m' or part=='M'):
        return(iterm(a))
    if(part=='H'):
        return(iterh(a))
    if(part=='i'):
        return("Chaturti-eka")
    if(part=='A'):
        return(iterA(a))
    if(part=='I'):
        return("Pratama-eka")

words="रमा रमे रमाः रमाम् रमे रमाः रमया रमाभ्याम् रमाभिः रमायै रमाभ्याम् रमाभ्यः रमायाः रमाभ्याम् रमाभ्यः रमायाः रमयोः रमाणाम् रमायाम् रमयोः रमासु"
words=words.split(" ")
for word in words:
    word=transliterate(word,sanscript.DEVANAGARI,sanscript.HK)
    print(word,end=':')
    print(vibhakthi(word))
def purusha(a):
    part=a[slice(-4,len(a),1)]
    if(part=='thaH'):
        return("Madyama purusha-dvi")
    part=a[slice(-3,len(a),1)]
    if(part=='taH'):
        return("Pratama purusha-dvi")
    if(part=='nti'):
        return("Pratama purusha-bahu")
    if(part=='tha'):
        return("Madyama purusha-bahu")
    if(part=='Ami'):
        return("Uttama purusha-eka")
    if(part=="vaH"):
        return("Uttama purusha-dvi")
    if(part=='maH'):
        return("Uttama purusha-bahu")
    part=a[slice(-2,len(a),1)]
    if(part=='ti'):
        return("Pratama purusha-eka")
    if(part=='si'):
        return("Madyama purusha-eka")
"""   
l=input()
l=(transliterate(l,sanscript.DEVANAGARI,sanscript.HK))
l=l.split()
print(vibhakthi(l[0]))
print(vibhakthi(l[1]))
print(purusha(l[2]))
"""