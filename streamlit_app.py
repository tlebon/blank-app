import streamlit as st

st.header("I'm tim 😊,")
st.write('wassup folks. my name is tim and im a very complicated person with many wants and desires.')
option = st.selectbox(label='which thing is my favorite?', options=[
                      'cat', 'dog', 'lizard', 'french fries'], placeholder='choose one!', index=None)
if st.button('Make a choice'):
    if option == 'dog':
        st.balloons()
        st.success(
            'Yes its a dog, but french fries are a close second!', icon="✅")
    else:
        st.error('Do you know me at all?', icon="😩")
