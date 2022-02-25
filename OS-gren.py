import shortr

sports = ["Fotboll", "Handboll", "Skidor", "Simmning", "Stavhopp", "Skidskytte"]


basic_questions = ["Behöver OS en ny gren?", "Är det en sport?", "Är det en laglig sport?", "Är det en genomförbar sport?", "Är det en publiksport?", "Är det tillräckligt många som utför sporten?", "Har OS för många sporter nu?" ]
questioning = True
i = 0

new_sport = input("Vilken sport tycker du borde läggas in i OS?")


while questioning and i != 6:
    answer = shortr.s(input(basic_questions[i]))

    if answer == "yes":
        i += 1

    elif answer == "no":
        print("Okej, då lägger vi inte till nån ny sport")
        questioning = False


while questioning:
    sports.append(new_sport)

    print("\nDe Sporter som finns i OS nu är:")
    for i in range(len(sports)):
        print(sports[i])

    answer = shortr.s(input("Har OS för många sporter nu?"))
    if answer == "yes":
        break
    elif answer == "no":
        questioning = False
        break


while questioning:
    remove = input("Vilken sport ska man ta bort?")
    if remove in sports:
        sports.remove(remove)
        break



print("\nDe Sporter som finns i OS nu är:")
for i in range(len(sports)):
    print(sports[i])
