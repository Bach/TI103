# permet de mettre des remarques
# dans le code
# les remarques s'appelent aussi
# des commentaire
# rem and comments

# 4 core types
# Int (Integre), Float, String, Bool (Boolean)

#Exemple de valeurs (Integer) Int
58429
-9

#Float
9.0
11.45
-45.156
-8.0

#chaine string
# entre apostrophe quote
# entre guillement double quote
'Bonjour'
"Bonjour"
"C'est l'heure"
'C'est l'heure' #-> erreur
'C\'est \'\heure'
'45' #c'est une chaine
"-0.67" #c'est une chaine

#bool ou boolean
True #equivaut a 1 
False #equivaut a 0

###################################################
# les sortie Output

print('hello world!')

#ici print prends en entree 4 arguments
#print peut prendre une liste d'arguments

print("j'ai ", 20, "ans", False)

#print utilise un argument par defaut end

# l'instruction ou la fonction print recoit 2 arguments
# argument 1: la chaine hello
# argument 2: l'entier 35
print('hello',35)

#argument end, comment la sortie se termine:
print('hello',35, end="|")

# la valeur par defaut de l'argument end est end="\n" 
# si end n'est pas definit

####################################################
#les variables

# creation de la variable paul
hello ='Paul' # J'assigne la valeur paul a la variable hello
print(hello)

#assigne avec des valeur fix
s1 ='hello'
s2 ='world'
print(s1,s2)

#assigne avec la valeur d'une autre variable
s1 ='hello'
s2 = s1
s2 ='world'
print(s1,s2)

#convention de nommage des variables

# ne peut pas utiliser de caracteres speciaux # $ ! ? 
a$ = 1 #non
# lettre ou chiffres
abcde ABCD 1234
# on ne peut pas commencer par un nombre
1hello # non
#on peut finit par un noumbre
hello32
 #oui

hello_world # underscore _ et le seul caractere special autorise
            # snake_case conventionnel
helloWorld  # camelCase autorise mais pas conventionnel

#python est case sensitive
Hello=5
hello =6
print(hello,Hello) # sortie: 5 6
#Hello et hello sont bien distincts

############################################################
#Entrees utilisateur (recuperer les informations au clavier)
      
input('Votre Nom:')

#pour reutiliser la valeur entree dans un traitement
#je peux la mettre dans une variable
#a la reutiliser plus tard
nom = input('Votre Nom: ')
print('Bonjour',nom)

nom = input('Votre Nom: ')
age = input('Votre Age: ')
print('Bonjour',nom, 'tu as', age , 'ans.')


############################################################
#les operateurs arithmetiques
x=9 #assigne la valeur 9 a la variable x
y=3
resultat = x + y 
print (resultat)

# x + y: est un operateur arithmetique
# x + y: x et y sont des operandes 

#regle generale les 2 types de donnees des operandes 
#doivent etre les meme

'hello' + 9 #erreur
'hello' - 9 #erreur
'hello' / 9 #erreur
'hello' * 9 #oui hellohellohellohellohellohellohellohellohello


x = 9
y = 3
resultat = x + y
print(resultat) #res 12 entier


x = 9    #int
y = 3.5  #float
resultat = x + y #float
print(resultat) #res = 12.5

x = 9
y = 3.5
resultat = x - y #soustraction res 5.5
print(resultat)

x = 9
y = 3
resultat = x * y #multiplication
print(resultat)


# les valeurs des variables varie a long des lignes de commandes
x = 9
y = 3.5
y = y *2 # y =7.0 float
x = x + y # 9+7.0 = 16.0
x = x + x # 32.0
y = x - y # 32.0 - 7.0=25.0
print(y)

x = 9 #int
y = 3 #int
result = x/y # 3.0 float !!!!
print(result)


x = 10 
y = 3 
result = x/y #3.3333333
print(result)

x = 10 
y = 3 
result = int(x/y) #transforme an int en prenant la partie entiere 3
print(result)

#fin groupe 2 24/01/2023

x = 10 
y = 3 
result = x ** y #puissance res 1000
print(result)

x = 10 
y = 3 
result = x // y #division entiere 3
print(result)

x = 10 
y = 3 
result = x % y #modulo (reste de la division entiere 1)
print(result)

#utilisation des parentheses pour prioriser le calcul
#on utilise les parenthese pour faire un code plus facilement lisible

x = 10 
y = 3 
z = 2
result = x + y * z #16
result = (x + y) * z #26
print(result)

# une autre facon de rendre de rendre le code visible est
#de l'ecrire sur plusieurs lignes

x = 10 
y = 3 
z = 2

result = (x + y)
result = result * z #26

print(result)

#ordre des operation dans python
#B Bracket (parenthese)
#E Exponentiel
#D Division
#M Multiplicarion
#A Addition
#S Soustraction

##########################################
#Les methodes de chaines des caracteres

#la methode upper transforme une chaine en majuscule
#methods .upper() appliqué a une valeur


print('hello'.upper()) #j'applique la methode upper a la valeur 'hello'
#resultat HELLO
#methods .upper() appliqué a une variable

chaine = 'hello' #je cree la variable chaine et affecte la valeur 'hello'
print(chaine.upper())  #j'applique la methode upper a la variable chaine
#resultat HELLO

#methode .lower() transforme une chaine en mininuscule

print('heLLo'.lower()) #resultat hello

#methode .capitalize() met le premier caractere le la chaine en maj
#et le rest en minuscule

print('heLLo'.capitalize()) #resultat Hello

#methode .count() conpte les sous chaines d'une chaine

print('heLLo'.count('LL')) #res 1
print('heLLo'.count('L'))  #res 2
print('heLLo'.count('l')) #res 0 case sensitive

#fonction LEN (pas une methode car pas de .)
#donne un entier qui est la longueur de la chaine

print(len('Hello')) #5
print(len('Hello World')) #11 on compte aussi l'espace
print(len('C\'est l\'heure')) #13 car \' ou \" ou\n prennent 1 seul caractere

#repeter une chaine de caractere avec l'operateur *

print('Hello'*3) # HelloHelloHello

#IMPORTANT addition ou concatenation des chaines de caracteres

chaine1='hello'
chaine2='world'

print(chaine1+chaine2) #helloworld

#la contcatenation est une operation importante 
#pour creer des phrase dynamiques


