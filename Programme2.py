import csv
import webbrowser
import matplotlib.pyplot as plt

# Ouvrir le fichier "extrait.txt"
with open("DumpFile.txt", "r") as fichier:
    ipsr = []
    ipde = []
    longueur = []
    flag = []
    seq = []
    heure = []

    flagcounterP = 0
    flagcounterS = 0
    flagcounter = 0
    framecounter = 0
    requestcounter = 0
    replycounter = 0
    seqcounter = 0
    ackcounter = 0
    wincounter = 0

    for ligne in fichier:
        split = ligne.split(" ")

        if "IP" in ligne:
            framecounter += 1

            if "[P.]" in ligne:
                flag.append("[P.]")
                flagcounterP += 1
            elif "[.]" in ligne:
                flag.append("[.]")
                flagcounter += 1
            elif "[S]" in ligne:
                flag.append("[S]")
                flagcounterS += 1

            if "seq" in ligne:
                seqcounter += 1
                seq.append(split[8])

            if "win" in ligne:
                wincounter += 1

            if "ack" in ligne:
                ackcounter += 1

            ipsr.append(split[2])
            ipde.append(split[4])
            heure.append(split[0])

            if "length" in ligne:
                split = ligne.split(" ")
                longueur.append(split[-2] if "HTTP" in ligne else split[-1])

            if "ICMP" in ligne:
                if "request" in ligne:
                    requestcounter += 1
                elif "reply" in ligne:
                    replycounter += 1

# Ajouter une vérification pour éviter la division par zéro
globalreqrepcounter = replycounter + requestcounter
if globalreqrepcounter != 0:
    req = requestcounter / globalreqrepcounter
    rep = replycounter / globalreqrepcounter
else:
    req = rep = 0

globalflagcounter = flagcounter + flagcounterP + flagcounterS
P = flagcounterP / globalflagcounter
S = flagcounterS / globalflagcounter
A = flagcounter / globalflagcounter

flagcounter = [flagcounter]
flagcounterP = [flagcounterP]
flagcounterS = [flagcounterS]
framecounter = [framecounter]
requestcounter = [requestcounter]
replycounter = [replycounter]
seqcounter = [seqcounter]
ackcounter = [ackcounter]
wincounter = [wincounter]



# ... (votre code existant)

# Créer le graphique semi-circulaire pour les drapeaux
name = ['Flag [.]', 'Flag [P]', 'Flag [S]']
data = [A, P, S]
colors = ['#2196F3', '#FFC107', '#4CAF50']  # Blue, Yellow, Green

explode = (0, 0, 0)
fig, ax = plt.subplots(figsize=(8, 6))  # Ajuster la taille de la figure ici
ax.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors, wedgeprops=dict(width=0.4))
ax.axis('equal')  # Assurer que le graphique soit circulaire
plt.savefig("graphe1.png")
plt.show()

# Créer le graphique semi-circulaire pour les requêtes et réponses
name2 = ['Request', 'Reply']
data2 = [req, rep]
colors2 = ['#4CAF50', '#FFC107']  # Green, Yellow
explode = (0, 0)
fig, ax = plt.subplots(figsize=(8, 6))  # Ajuster la taille de la figure ici
ax.pie(data2, explode=explode, labels=name2, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors2, wedgeprops=dict(width=0.4))
ax.axis('equal')  # Assurer que le graphique soit circulaire
plt.savefig("graphe2.png")
plt.show()

# ... (le reste de votre code)




# Contenu de la page web
# ... (votre code existant)

# Contenu de la page web
htmlcontenu = '''
<html lang="fr">
   <head>
      <meta charset="utf-8">
      <title> Traitement des données </title>
      <style>
      body{
          background-image: url('https://www.codeur.com/blog/wp-content/uploads/2021/08/image-programmation-1.jpg');
          background-repeat: no-repeat;
          background-size: cover;
          color:#e5f2f7;
          background-attachment: fixed;
          }
      </style>
   </head>
   
   <body>
       <center><h1>Julien Nkoma</h1></center>
       <center><h2>Projet SAE 15</h2></center>
       <center><p>Sur cette page web, nous vous présentons les informations et données pertinentes trouvées dans le fichier à traiter.</p></center>
       <center><h3> Nombre total de trames échangées</h3> %s</center>
       <br>
       <center><h3> Drapeaux (Flags)<h3></center>
       <center>Nombre de flags [P] (PUSH) = %s
       <br>Nombre de flags [S] (SYN) = %s  
       <br>Nombre de flag [.] (ACK) = %s
       <br>
       <br>
       <img src="graphe1.png">
       <h3> Nombre de requêtes et réponses </h3>
       Request = %s 
       <br>
       Reply = %s
       <br>
       <br>
       <img src="graphe2.png">
       <h3>Statistiques entre seq, win et ack </h3>
       Nombre de seq = %s
       <br>
       Nombre de win = %s
       <br>
       Nombre de ack = %s
   </body>
</html>
''' % (framecounter[0], flagcounterP[0], flagcounterS[0], flagcounter[0], requestcounter[0], replycounter[0], seqcounter[0], wincounter[0], ackcounter[0])

# ... (le reste de votre code)


# Contenu de la page web en Markdown
markdown_content = f'''
# Julien Nkoma

## Projet SAE 15

Sur cette page web, nous vous présentons les informations et données pertinentes trouvées dans le fichier à traiter.

### Nombre total de trames échangées
{framecounter[0]}

### Drapeaux (Flags)
- Nombre de flags [P] (PUSH) : {flagcounterP[0]}
- Nombre de flags [S] (SYN) : {flagcounterS[0]}
- Nombre de flag [.] (ACK) : {flagcounter[0]}

![Graphique Drapeaux](graphe1.png)

### Nombre de requêtes et réponses
- Request : {requestcounter[0]}
- Reply : {replycounter[0]}

![Graphique Requêtes/Réponses](graphe2.png)

### Statistiques entre seq, win et ack
- Nombre de seq : {seqcounter[0]}
- Nombre de win : {wincounter[0]}
- Nombre de ack : {ackcounter[0]}
'''

# Ouvrir un fichier Markdown pour les données extraites du fichier texte non traité
with open('donnees.md', 'w', newline='') as fichiermd:
    fichiermd.write('# Données extraites du fichier texte non traité\n\n')
    fichiermd.write('| Heure | IP source | IP destination | Flag | Seq | Length |\n')
    fichiermd.write('|-------|-----------|-----------------|------|-----|--------|\n')
    for row in zip(heure, ipsr, ipde, flag, seq, longueur):
        fichiermd.write(f'| {" | ".join(map(str, row))} |\n')

# Ouvrir un fichier Markdown pour les statistiques générales
with open('Stats.md', 'w', newline='') as fichier2md:
    fichier2md.write('# Statistiques générales\n\n')
    fichier2md.write('| Flag[P] (PUSH) | Flag[S] (SYN) | Flag[.] (ACK) | Nombre total de trames | Nombre de request | Nombre de reply | Nombre de sequence | Nombre de acknowledg | Nombre de window |\n')
    fichier2md.write('|-----------------|-----------------|-----------------|------------------------|---------------------|------------------|----------------------|------------------------|------------------|\n')
    for row in zip(flagcounterP, flagcounterS, flagcounter, framecounter, requestcounter, replycounter, seqcounter, ackcounter, wincounter):
        fichier2md.write(f'| {" | ".join(map(str, row))} |\n')

# Ouvrir un fichier Markdown pour la page web
with open("webpage.md", "w") as md:
    md.write(markdown_content)
    print("Page web en Markdown créée avec succès.")

