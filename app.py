import streamlit as st

st.set_page_config(page_title="Streamlit Cheat Sheet - by Shravan", page_icon="😎")
st.title("Streamlit Cheat Sheet - by Shravan")

st.header("Display Text")
display_text = "st.text('Fixed width text')\nst.markdown('_Markdown_') # see *\nst.caption('Balloons. Hundreds of them...')\nst.latex(r''' e^{i\pi} + 1 = 0 ''')\nst.write('Most objects') # df, err, func, keras!\nst.write(['st', 'is <', 3]) # see *\nst.title('My title')\nst.header('My header')\nst.subheader('My sub')\nst.code('for i in range(8): foo()')\n* optional kwarg unsafe_allow_html = True"
st.code(display_text, language="python")

st.header("Display Data")
display_data = "st.dataframe(my_dataframe)\nst.table(data.iloc[0:10])\nst.json({'foo':'bar','fu':'ba'})\nst.metric(label='Temp', value='273 K', delta='1.2 K')"
st.code(display_data, language="python")

st.header("Display interactive widgets")
display_widget = "st.button('Hit me')\nst.download_button('On the dl', data)\nst.checkbox('Check me out')\nst.radio('Radio', [1,2,3])\nst.selectbox('Select', [1,2,3])\nst.multiselect('Multiselect', [1,2,3])\nst.slider('Slide me', min_value=0, max_value=10)\nst.select_slider('Slide to select', options=[1,'2'])\nst.text_input('Enter some text')\nst.number_input('Enter a number')\nst.text_area('Area for textual entry')\nst.date_input('Date input')\nst.time_input('Time entry')\nst.file_uploader('File uploader')\nst.camera_input("")\nst.color_picker('Pick a color')"
st.code(display_widget, language="python")

st.header("Display progress and status")
display_progress = "st.progress(progress_variable_1_to_100)\nst.balloons()\nst.snow()\nst.error('Error message')\nst.warning('Warning message')\nst.info('Info message')\nst.success('Success message')\nst.exception(e)"
st.code(display_progress, language="python")

st.header("Display Media")
display_media = "st.image(image, caption='Sunrise by the mountains', use_column_width=True)\nst.audio(audio_file, format='audio/ogg')\nst.video(video_file, format='video/mp4')\nst.iframe(src='https://docs.streamlit.io/en/stable/getting_started.html')"
st.code(display_media, language="python")

st.subheader("Detailed Cheat Sheet")
st.write("https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlit.app/")
