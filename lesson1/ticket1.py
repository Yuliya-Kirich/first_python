while True:
    value = input("Введите число или строку. Если хотите завершить ввод, нажмите на клавиатуре 0.  >>>>> ")

    if not value.isdigit():
        print("Вы ввели строку :" + value)

    elif int(value) != 0:
        print("Вы ввели число : " + value)

    else:
        print("Выход")
        break
