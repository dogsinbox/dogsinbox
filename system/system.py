import webbrowser
password = input("Введите пароль: ")
if password == "w5ga1": 
	print("Зравствуйте, пользователь")
else:
    print("нет, пароль не верный")
    input('Нажми Enter чтобы Выйти')
    quit()
while True:
        # Выводим сообщение какие действия есть
        print("Выберите, какой сайт хотите открыть:\n"
              "YouTube: 1\n"
              "Google: 2\n"
              "ВКонтакте: 3\n"
              "Tetamix: 4\n"
              "Дневник.ру: 5\n"
              "Выйти: 6\n")
        action = input('Напишите число сайта, который вы хотите открыть: ')
        if action == "1":
        	webbrowser.open_new('https://youtube.com')
        if action == "2":
        	webbrowser.open_new('https://google.com')
        if action == "3":
        	webbrowser.open_new('https://vk.com')
        if action == "4":
        	webbrowser.open_new('https://tetamix.org/')
        if action == "5":
          webbrowser.open_new('https://dnevnik.ru/userfeed')
        if action == "6":
          quit()
       