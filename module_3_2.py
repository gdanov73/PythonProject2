def send_email(message:str, recipient:str, sender="university,help@gmail.com") : # функция
    if (('@' not in recipient) or not recipient.endswith((".com",".ru",".net"))) or ("@" not in sender or not sender.endswith((".com",".ru",".net"))) : # проверка условия
        print("Невозможно отправить письмо с адреса " + sender + " на адрес "+recipient+".") # печать результата
        return # возврат значения
    if sender == recipient : # проверка условия
        print( "Нельзя отправить письмо самому себе!") # печать результата проверки
        return # возврат значения
    if sender == "university,help@gmail.com" : # проверка условия
        print( "Письмо успешно отправлено с адреса " + sender + " на адрес "+recipient+".") # печать результата проверки
        return # возврат значения
    else: print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес "+recipient+".") # печать результата

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com') # ввод данных

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
