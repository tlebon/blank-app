import streamlit as st
import pandas as pd
import numpy as np

st.header("I'm tim 😊")
st.write('wassup folks. my name is tim and im a very complicated person with many wants and desires.')

tab1, tab2, tab3 = st.tabs(
    ["get to know me", "get to know one of my loves", "Owl"])

with tab1:
    option = st.selectbox(label='which thing is my favorite?', options=[
                          'cat', 'dog', 'lizard', 'french fries'], placeholder='choose one!', index=None)
    if st.button('Make a choice'):
        if option == 'dog':
            st.balloons()
            st.success(
                'Yes its a dog, but french fries are a close second!', icon="✅")
            st.image(image='Oskar.jpeg')
        elif option == 'french fries':
            st.error('ooh i do love fries, but not number 1 🍟')
        else:
            st.error('Do you know me at all?', icon="😩")
with tab2:
    fries = pd.DataFrame([['curly', 30, 'spicy', 'Arbys (USA)'], ['thin', 60, 'salty', 'Belgium (or maybe France?)'], [
        'thick cut', 40, 'soft', "England"], ['waffle', 15, 'texture', "Chick-fil-A (USA)"], ['crinkle', 30, 'crispy', "USA"]], columns=['type', 'serving', 'quality', 'origin'])
    if "fry" not in st.session_state:
        st.session_state.fry = fries.iloc[np.random.randint(
            low=0, high=len(fries))]
    fry = st.session_state.fry
    col1, col2 = st.columns(spec=[1, 1])
    with col1:
        st.header(
            f'How many {fry["type"]} french fries  is recommended for a single serving?')
        serving = st.select_slider(
            options=[a*5 for a in range(0, 15)], label='choose a serving')
        if st.button('fries'):
            if serving == fry["serving"]:
                st.balloons()
                st.success(
                    'yummy', icon="🍟")
            elif serving < fry["serving"]:
                st.error(
                    'im still hungry', icon="🤤")
            elif serving > fry["serving"]:
                st.error(
                    'i feel gross', icon="🫃")

    with col2:
        if "fry2" not in st.session_state:
            st.session_state.fry2 = fries.iloc[np.random.randint(
                low=0, high=len(fries))]
        fry2 = st.session_state.fry2
        st.header(f'where was this fry born?{fry2["type"]}')

   
        selection = st.segmented_control(
            "Tool",
            options=fries['origin'].unique().tolist(),
            format_func=lambda option: option.title(),
            selection_mode="single",
        )

        if st.button('lets eat!'):
            if selection is None:
                st.warning('Choose where you think this fry came from.')
            elif selection == fry2['origin']:
                st.success(
                    'You know your fries! 🍟', icon="✅")
            else:
                st.error('wrong, still tastes good tho')
