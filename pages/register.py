import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
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

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = (
        authenticator.register_user(pre_authorization=False)
    )
    if email_of_registered_user:
        creds = authenticator.authentication_handler.credentials
        config["credentials"] = creds
        st.success("User registered successfully")
except Exception as e:
    st.error(e)

st.page_link(label="Назад", page="login.py")

with open("config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
