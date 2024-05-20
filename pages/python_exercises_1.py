import streamlit as st
from streamlit_ace import st_ace
from python_func import *

# from pylint import epylint as lint

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

if st.session_state["authentication_status"]:
    st.subheader("HW1. Блок Python. Задача 1")
    st.markdown(
        "- Создайте переменную **x** и присвойте ей значение равное 6\n"
        "- Создайте переменную **y** и присвойте ей значение равное 2.5\n"
        "- Создайте переменную **result** и запишите в нее выражение, используя ранее объявленные переменные **x**, **y**, арифметические операторы, числа/цифры, так, чтобы по итогу значение в **result** было равно **8.75**\n"
        "Например:"
    )
    st.code("result = x * 2 - 2 * y / 2", language="python")

    loc = {}
    content = st_ace(
        placeholder="Ваш код",
        language="python",
        theme="chrome",
        keybinding="vscode",
        show_gutter=True,
        min_lines=10,
        key="ace",
    )

    if content:
        st.markdown("### Результат")
        x_check = 6
        y_check = 2.5
        result_check = x_check + 2 * 2 - y_check / 2
        try:
            with stdoutIO() as s:
                exec(content, globals(), loc)
            # with open('ttt.py', mode='w') as f:
            #     f.write(content)
            # (pylint_stdout, pylint_stderr) = lint.py_run('ttt.py', return_std=True)
            #
            # st.write(pylint_stdout.getvalue())
            # st.write(pylint_stderr.getvalue())
            # exec(content, globals(), loc)
            try:
                assert "x" in loc.keys(), "Проверьте название переменной x"
                assert loc["x"] == x_check, "Проверьте значение в переменной x"
                assert "y" in loc.keys(), "Проверьте название переменной y"
                assert loc["y"] == y_check, "Проверьте значение в переменной y"
                assert "result" in loc.keys(), "Проверьте название переменной result"
                assert (
                    loc["result"] == result_check
                ), "Проверьте значение в переменной result"
                st.success("Все верно! Ключ = 51")
            except Exception as ex:
                st.error(ex)
        except Exception as ex:
            st.error(ex)
else:
    st.error("Войдите в систему, либо введите верный пароль")
