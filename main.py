import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)


def main():
    name, authentication_status, username = authenticator.login('Login with USN and DOB', 'main')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.title(f'Welcome {name}')
        st.subheader(f'USN: {username.upper()}')
        st.write('Some Hidden content content')
    elif authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your USN and DOB  in the format: DDMMYYYY')


with open('./config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

if __name__ == '__main__':
    main()
