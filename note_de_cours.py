
######### les remarques

# ceci est une remarque ou un commentaire
# this is a rem or a comment



#########################################
#les types et des exemples de valeur

# les 4 core types int, float, string, bool
# core type vs custom types (type personalise)

# int pour integer / nombre entier
# 2 exemple de valeurs:
4500
-12
# float nombre decimal ou a vergule flotante
0.15
12.0
-500.015
-9.0

#chaine de de caractere / string
# ' apostrophe, quote
# " guillemet , double-quote
'hello' # cette chaine contient 5 caracteres
'hello world' # 11 
"hello"
"hello world"
"C'est l'heure"
'C'est l'heure' # errue ce n'est pas une valeur 
# conflit entre caracteres ' et "
# caractere en en anglais character

'Il a dit le mot "bonjour"'
"Il a dit le mot "bonjour""

Il m'a dit "c'est l'heure"

# / barre oblique, slash
# \ barre oblique inversee, backslash

# remplace '  par  \' 
# remplace " par \"

"Il m\'a dit \"c\'est l\'heure\""
'Il m\'a dit \"c\'est l\'heure\"'

#bool boolean
True 1
False 0

####################################################
#Output Sortie
print('hello') #affiche la valeur de type string hello
print(hello) #ne reconnais pas le type ->erreur

#instruction ou fonction print
#qui prends en compte 1 a n arguments
#ici 4 arguement
#1 ier argument de type string
#2d argumeny de type int ou integer ou entier
#3iem argument de type float ou nombre a virgule flottante
#4iem de type bool boolean
print("hello", 5, 9.45, True )

#le caractere special "retour chariot" ou line feed \n 

print("Hello \n World")

print("Hello World", end='\n') 
print("Hello World")

print("")

print("Hello World") # end est en valeur par default \n
print("Hello World")

print("")

print("Hello World",end=' ' ) #changement de la valeur par default \n en espace
print("Hello World") # les deux instructions ecrivent sur la meme ligne

#########################################
#Variables

prenom = 'Pierre' # je cree la variable nom et 
#je lui assigne la valeur Pierre de type string chaine

#une variable est comme une boite ou on peut ranger une valeur
#la boite est accessible par son nom de variable

chaine1 = 'hello'
chaine2 = 'world'

print(chaine1,chaine2) 

chaine1 = 'hello'
chaine2 = 'world'

print('hello','world')
print(chaine1,chaine2) 
print('hello','world\n', chaine1,chaine2)


#ex
chaine1 = 'hello' #creation variable chaine1 et affectation valeur 
chaine2 = 'world' #creation variable chaine2 et affectation valeur 
chaine1 = chaine2 #reaffectation de la variable chaine1 avec la valeur de chaine2
print(chaine1,chaine2) # resultat world world

##################################################
#les conventions de nommage des variables

#il faut choisir le nom des variables judicieusement
#en suivant les convention
# la nom dois decrire ce que fait la variable par exemple:

age=20 # cette variable contient un age

#on ne peut pas utiliser de caracteres speciaux
# comme @ # $ % ^ & -

#on peut utiliser les lettres majuscule et minuscules

abc = 12
ABC = 13

#on peut utiliser les chiffre mais pas en debut de variable

32a #est interdit
a32 #est autorisé
a32b64 #est autorisé

hello_world #snake_case oui underscore seul exception en caractere special
helloWorld #camelCase non

# le caracteres underscore/sousligné _ et le seul caractere special autorisé

hello_world #variable en 2 mots
hello-world #operation soustraction

# les variable sont case sensitive, sensible a la casse

Hello = 5
hello = 6
print(Hello,hello) # 5 6

############################################################
#les entrees utilisateur

nom = input("Nom: ") #on cree la variable nom pour y entrer
#la valeur de l'utlisateur
#Note on met un espace apres : pour que les program soit plus lisible

print("Bonjour",nom) #on ecrit Bonjour et le nom qu'a entré l'utilisateur

#autre exemple
Nom = input('Prenom: ')
Age = input('Age: ')
print('Bonjour', Nom, "tu as", Age, "ans")

#########################################################
#les operateurs arithmetiques et les operandes
#

#ici l'operateur arthmetique (addition) prends 2 operandes
# l'entier 4 et l'entier 5. ces deux operrandes sont des valeurs
print(4+5)

# ici les deux operandes sont des variables de type entier , integer
a=4
b=5
print(a+b)

#d'autre cobinaisons
print(4+5)
print(a+b)
print(a +5)
print (4+b)


#il faut que les type de donnees des 2 operandes soit la meme
'hello' + 3 #n'a pas de sens et fait une erreur
'hello' - 3 #erreur
'hello' / 3 #erreur
'hello' * 3 #oui c'est possible repete 3 fois hellohellohello

x= 9 
y= 3
resultat = x + y #int + int donne int
print(resultat)

x= 9 
y= 3.5
resultat = x + y #int + float donne float
print(resultat)

x= 9
y= 3.5
resultat = x - y #soustraction
print(resultat)

x= 9
y= 3.5
resultat = x * y #multiplication
print(resultat)

x= 9
y= 3.5
resultat = x / y #division
print(resultat)

x= 9
y= 3
resultat = x / y  #Attention diviser 2 int retourne un float
print(resultat)    #retourne un float meme si resultat est entier 
#car il ne sais pas si il aura a retourner un float a l'avance
#retourne 3.0 et non 3









