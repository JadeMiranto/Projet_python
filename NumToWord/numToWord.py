"""
Fonction pour convertir un nombre entiers en lettres
Langues disponibles Français (fr) et Anglais (en)
Nombre supporté : [-999_999_999_999_999_999_999_999_999_999, 999_999_999_999_999_999_999_999_999_999] 

numToWords(n=nombre, lang=langue) : str 

_Miranto_
"""

def numToWords(n=0, lang='fr'):
    #nombres en anglais
    nombresEn = {
        "unites" : ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        "dixs" : ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
        "dizaines" : ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
        "grandeur" : ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion"]
    }
    #nombres en francais
    nombresFr = {
        "unites" : ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"],
        "dixs" : ["dix","onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"],
        "dizaines" : ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt","quatre-vingt"],
        "grandeur" : ["cent", "mille", "millions", "milliards", "billions", "billiards", "trillions", "trilliards", "quadrillions", "quadrillards"]
    }
    #langues disponibles
    langues = ['fr', 'en']
    
    lang = lang.lower()
    if lang not in langues:
        lang = 'fr'
        
    if lang=='en':
        nombres = nombresEn
    else:
        nombres = nombresFr
    
    #conversion en int
    n = int(n)
    
    #verifier si le nombre donné est négatif
    moins = True if n<0 else False
    n = (-1)*n if moins else n
    
    if n < 10:
        mots = nombres['unites'][n]
    elif n < 20:
        mots = nombres['dixs'][n%10] 
    elif n < 100:
        dizaines = nombres['dizaines'][n//10]
        
        if n%10 == 0:
            if (n//10==7 or n//10==9) and lang=='fr':
                mots = dizaines + '-dix'
            else:
                mots = dizaines
        else:
            if (n//10==7 or n//10==9) and lang=='fr':
                mots = dizaines + '-' + nombres['dixs'][int(str(n)[-1])]
            else:
                mots = dizaines + '-' + nombres['unites'][int(str(n)[-1])]
                
    elif n < 1000:
        centaine = nombres['unites'][n//100]
        
        suite = numToWords(n=int(str(n)[1:]), lang=lang)
        
        if suite=='zéro' or suite=='zero':
            suite = ''
            
        if centaine == 'un':
            mots = nombres['grandeur'][0] + ' ' + suite
        else:
            mots = centaine + ' ' + nombres['grandeur'][0] + ' ' + suite
            
    else:        
        """
            g : catégorie (mille, millions, ....)
            avant: avant la categorie
            apres: apres la catégorie
            ex: n = 2_123_456 (deux millions cent vingt trois mille quatre cent cinquante-six)
                puissance = 6
                g = 2 (millions)
                avant = 2 (avant millions)
                apres = 123_456 (apres les millions)
            
        """
        puissance = len(str(n)) - 1 
        g = puissance // 3
        avant = n // (1000**g)
        apres = int(str(n)[(-3*g):])
        grandeur = nombres['grandeur'][g]
        suite = numToWords(n=apres, lang=lang)
        
        if suite=='zéro' or suite=='zero':
            suite = ''
            
        if grandeur == 'mille' and avant==1:
            mots = grandeur + ' ' + suite
        else :
            mots = numToWords(n=avant, lang=lang) + ' ' + grandeur + ' ' + suite
    
    #Ajout du moins (ou negative) a la fin
    if moins:
        if lang=='en':
            moins = 'negative '
        else:
            moins = 'moins '
    else:
        moins = ''
        
    return moins + mots
