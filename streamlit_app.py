import streamlit as st

st.header("I'm tim 😊")
st.write('wassup folks. my name is tim and im a very complicated person with many wants and desires.')

tab1, tab2, tab3 = st.tabs(["get to know me", "get to know the world", "Owl"])

with tab1:
  option = st.selectbox(label='which thing is my favorite?', options=[
                        'cat', 'dog', 'lizard', 'french fries'], placeholder='choose one!', index=None)
  if st.button('Make a choice'):
      if option == 'dog':
          st.balloons()
          st.success(
              'Yes its a dog, but french fries are a close second!', icon="✅")
          st.image(image='Oskar.jpeg')
      elif option =='french fries':
          st.error('ooh i do love fries, but not number 1 🍟')
      else:
          st.error('Do you know me at all?', icon="😩")
with tab2:
    col1, col2 = st.columns(spec = [1,1])
    with col1:
        st.header('What year was gandhi born?')
        year = st.select_slider(options=[a for a in range(1860, 1980)], label= 'choose a year')
        if st.button('gandhi bday party'):
          if year == '1869':
            st.balloons()
            st.success('wtf... you cheated? how did you know that? theres no way')
          else: 
            st.error('yea how would you guess that, its impossible.. ok its closer to the beginning and divisible by 3')

    with col2: 
       st.header('how many european cities have i been to')
       
