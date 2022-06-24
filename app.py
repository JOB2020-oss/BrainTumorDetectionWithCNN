import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
from predict import brain_work,back_ground
from PIL import Image
import streamlit.components.v1 as component


conn = sqlite3.connect("database.db")
c = conn.cursor()

back_ground("back/brain0.jpg")

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)')
    
def add_user(username,password):
    c.execute('INSERT INTO users(username,password) VALUES (?,?)',(username,password))
    conn.commit()
    
def login_user(username,password):
    c.execute('SELECT * FROM users WHERE username =? AND password=?',(username,password))
    data = c.fetchall()
    return data

def view_all():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    return data

def delete_all():
    c.execute('DELETE  FROM users')

def main():
    h1 = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h1 style='text-align: center; color: Black;'>Brain Tumor Detector</h1>
    </div>
    """
    h2d = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <h2 style='text-align: center; color: Black;'>Patient Diagnosis</h2>
    </div>
    """
    h2a = """
    <div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
    <a href="#"><h2 style='text-align: center; color: Black;'>Analyse Users</h2></a>
    </div>
    """
    with st.sidebar:
        choice = option_menu(None, ["Home","Info","Login",  "SignUp"], 
            icons=['house',"info",'key', "list-task"], 
            menu_icon="cast", default_index=0, orientation="vertical",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }
        )
    if choice == "Home":
        component.html(h1)
        st.image("back/image3.jpg",width=750)
    elif choice == "Login":
        component.html(h1)
        def login():
            def clear_form():
                st.session_state["foo"] = ""
                st.session_state["bar"] = ""
            name =  st.sidebar.text_input("UserName",key="foo")
            pwd = st.sidebar.text_input("Password",type="password",key="bar")
            st.session_state["name"] = name
            #name = st.session_state["name"]
            if st.sidebar.checkbox("Login"):
                st.sidebar.button(label="Logout", on_click=clear_form)
                create_table()
                result = login_user(name,pwd)
                if result:
                    #st.success(st.session_state["name"])
                    brain_work()
        login()
            
    elif choice == "SignUp":
        component.html(h1)
        st.subheader("Register Here")
        name = st.text_input("UserName")
        pwd = st.text_input("Password")
        if st.button("Register"):
            create_table()
            add_user(name,pwd)
            st.write("Succesfully")
            st.balloons()
            
            
hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) #FOR HIDING OF STREAMLIT HAMBURGER

footer = """
<style>
footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'Made With Love For Python'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;}
    </style>
"""
component.html(footer)
if __name__=='__main__':
    main()

