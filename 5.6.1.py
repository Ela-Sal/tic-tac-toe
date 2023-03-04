text = {
        "0.0" : "-", "0.1": "-", "0.2": "-",
        "1.0" : "-", "1.1": "-", "1.2": "-",
        "2.0" : "-", "2.1": "-", "2.2": "-"
}
def print_field():
    print(" 012")
    print("0" + text["0.0"] + text["0.1"] + text["0.2"])
    print("1" + text["1.0"] + text["1.1"] + text["1.2"])
    print("2" + text["2.0"] + text["2.1"] + text["2.2"])

print_field()

count = 0
while count < 9:
    a = input("Введите координаты")
    count += 1
    while a not in  text:
        a = input("Введите координаты")

    text[a] = "X"
    if count % 2 == 0:
        text[a] = "O"


    #######################################
    #проверка на наличие победителя

    for i in range(0,3):

        if text[str(i) + ".0"] == text[str(i) + ".1"] and text[str(i) + ".1"] == text[str(i) + ".2"]:
            if text[str(i) + ".0"] == "X":
                print("победитель X")
                exit()
            elif text[str(i) + ".0"] == "O":
                print("победитель O")
                exit()



        if text["0." + str(i)] == text["1." + str(i)] and text["1." + str(i)]== text["2." + str(i)]:
            if text["0." + str(i)] == "X":
                print("победитель X")
                exit()
            elif text["0." + str(i)] == "O":
                print("победитель O")
                exit()



    if text["0.0"] == text["1.1"] and text["1.1"] == text["2.2"]:
            if text["0.0"] == "X":
                print("победитель X")
                exit()

            elif text["0.0"] == "O":
                print("победитель O")
                exit()


    if text["2.0"] == text["1.1"] and text["1.1"] == text["0.2"]:
            if text["2.0"] == "X":
                print("победитель X")
                exit()
            elif text["2.0"] == "O":
                print("победитель O")
                exit()

    print_field()


