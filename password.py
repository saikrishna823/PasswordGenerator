import random
import string
import streamlit as st
html_code = '''
<h1 style="color:blue; text-align:center">Welcome to Password Generator !!!</h1>
'''
def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.markdown(html_code,unsafe_allow_html=True)
    length = st.text_input("Enter the length of the password: ")
    use_uppercase = st.selectbox("Include uppercase letters? (yes/no): ",("Yes","No"))
    use_numbers = st.selectbox("Include numbers? (yes/no): ",("Yes","No"))
    use_special_chars = st.selectbox("Include special characters? (yes/no): ",("Yes","No"))
    if(st.button("Generate Password")):
       
       password = generate_password(int(length), use_uppercase.lower()=="yes", use_numbers.lower()=="yes", use_special_chars.lower()=="yes")
       st.write(password)

if __name__ == "__main__":
    main()
