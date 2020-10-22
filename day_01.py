from datetime import datetime

curr_time = datetime.now().hour
username = "Natalia"

if 0 <= curr_time <= 4:
    print("Доброй ночи, " + username)
elif 5 <= curr_time <= 9:
    print("Доброе утро, " + username)
elif 10 <= curr_time < 17:
    print("Добрый день, " + username)
else:
    print("Добрый вечер, " + username)




