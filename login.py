import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from send_email import *
from python_func import *


hide_part_of_page()

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)


authenticator.login()
st.page_link(label="Регистрация", page="pages/register.py")

# Если удалось залогиниться
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(
        f'*{st.session_state["name"]}* вы успешно вошли в систему треккинга практических задач. '
    )
    col1, col2 = st.columns([1, 3])
    if col1.button("Изменить пароль"):
        try:
            if authenticator.reset_password(st.session_state["username"]):
                st.success("Password modified successfully")
        except Exception as e:
            st.error(e)
    if col2.button("Скрыть"):
        st.write("")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
    try:
        (
            username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password,
        ) = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.write("Внимание: кол-во отправлений email в день ограничено до 10!")
            config["credentials"]["usernames"][username_of_forgotten_password][
                "password"
            ] = new_random_password
            send_gmail(new_random_password)
            st.success(f"Новый пароль был выслан вам на почту")
        elif username_of_forgotten_password == False:
            st.error("Username not found")
    except Exception as e:
        st.error(e)
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")


with open("config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
