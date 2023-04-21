import yaml
import streamlit as st
import streamlit_authenticator as stauth

data = ['1MS21IS016 2003-09-24 AMITESH VERMA', '1MS21CI055 2003-03-24 SIDDHARTH RAO KODIKAL',
        '1MS21IS014 2002-09-21 AKHILESH', '1MS21CI056 2003-09-18 SIRI R S', '1MS21CI057 2003-09-15 SUHA JAMEEL S',
        '1MS21CI004 2003-07-19 ANIRUDDH MANTRALA', '1MS21CI006 2003-03-05 ANSH SINGHAL',
        '1MS21CI049 2003-05-21 SHRAVAN', '1MS21IS017 2003-06-07 AMITH', '1MS22AI017-T 2004-05-28 SANA ABDUL RAHIMAN']
credential = {}
for i in range(len(data)):
    data[i] = data[i].split(' ')
    usn = data[i][0]
    email = usn + '@msrit.edu'
    dob = data[i][1]
    formated_dob = dob[8:10] + dob[5:7] + dob[0:4]
    password = formated_dob
    hashed_pass = stauth.Hasher([password]).generate()
    name = data[i][2]
    for j in range(3, len(data[i])):
        name = name + ' ' + data[i][j]
    credential[usn] = {'password': hashed_pass[0], 'name': name, 'email': email}
    st.write(credential)

with open('./newconfig.yaml', 'w') as file:
    yaml.dump(credential, file, default_flow_style=False)
