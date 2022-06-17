import csv
import matplotlib.pyplot as plt

scoreSigne = {
    "Axolotl" : 0,
    "Crapaud" : 0,
    "Crevette" : 0,
    "Eggdog" : 0,
    "Phantom" : 0,
    "Astre" : 0,
    "Faucille" : 0,
    "Marteau" : 0,
    "Pute" : 0,
    "Chimère" : 0,
    "Indigène" : 0,
    "Weeb" : 0,
    "Spyrheaux" : 0,
    "Chat / Pouic" : 0,
    "Choco" : 0,
    "Dinosaure" : 0,
    "Coyote" : 0
}

linkPersoSigne = dict()
liFinalSigne = list()

def main():
    # opening the CSV file
    with open('./response.csv', mode='r', encoding="utf8")as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        title = True
        # displaying the contents of the CSV file
        for lines in csvFile: #line of classement: 1 to 17
            #print(lines)
            if not title:
                for i in range(1,18):
                    scoreSigne[lines[i]] += 324-(i*i)
                linkPersoSigne[lines[19]] = lines[18]
            title = False


    orderedScoreSigne = dict(sorted(scoreSigne.items(), key=lambda x:x[1])) #order as 17,16,15,...,1
    #print(orderedScoreSigne)
    reverseOrderedScoreSigne = dict(reversed(list(orderedScoreSigne.items()))) #order as 1,2,3,...,17
    print(reverseOrderedScoreSigne)
    #plt.bar(orderedScoreSigne.keys(), orderedScoreSigne.values(), width=0.25, color='g')
    plt.bar(list(reverseOrderedScoreSigne.keys()), reverseOrderedScoreSigne.values(), width=0.25, color='b')

    #print("Association:")
    print(linkPersoSigne)
    #show graph
    nbToDelete = input("Combien de signes souhaitez vous enlever?")
    for perso, choosenSigne in linkPersoSigne.items():
        if choosenSigne not in liFinalSigne:
            liFinalSigne.append(choosenSigne)
    i = 0
    sup = min(17-int(nbToDelete), len(scoreSigne))
    while i < sup:
        sig = list(reverseOrderedScoreSigne.keys())[i]
        if sig not in liFinalSigne:#if not already in because choosen:
            liFinalSigne.append(sig)
        i += 1

    #for i in range(0, ):
    #   liFinalSigne.append(list(reverseOrderedScoreSigne.keys())[i])

    print(liFinalSigne)

    with open('result.txt', "w") as fichier:
        fichier.writelines(f"Signes gardés ({len(liFinalSigne)}):\n")
        for elm in liFinalSigne:
            fichier.writelines(f"{elm}\n")


        fichier.writelines("\n\nAssignation:\n")
        for key, value in linkPersoSigne.items():
            line = f"{key} ---> {value}\n"
            fichier.writelines(line)
    fichier.close()

    plt.show()


if __name__ == '__main__':
    main()