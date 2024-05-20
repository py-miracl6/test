from redmail import gmail


gmail.user_name = "annikulina6@gmail.com"
gmail.password = "fxaj vxjc zmet vlak"

def send_gmail(password):
    gmail.send(
        subject="Смена пароля",
        receivers=["annikulina.08@gmail.com"],
        text=f"Добрый день!\n\nВаш новый пароль {password}\n\nС уважением,\nНикулина Анастасия\nCEO PyMagic",
    )