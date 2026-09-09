import streamlit as st

st.header("I'm tim 😊")
st.write('wassup folks. my name is tim and im a very complicated person with many wants and desires.')

tab1, tab2, tab3 = st.tabs(["get to know me", "get to know one of my loves", "Owl"])

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
    col1, col2 = st.columns(spec=[1, 1])
    with col1:
        st.header(
            'How many french fries (thick cut) is recommended for a single serving?')
        serving = st.select_slider(
            options=[a*5 for a in range(0, 15)], label='choose a serving')
        if st.button('fries'):
            if serving == 20:
                st.balloons()
                st.success(
                    'yummy', icon="🍟")
            elif serving < 20:
                st.error(
                    'im still hungry', icon="🤤")
            elif serving > 20:
                st.error(
                    'i feel gross', icon="🫃")

    with col2:
        st.header('which french fries types are not real')
        option_map = {
            0: "curly",
            1: "thin",
            2: "thick cut",
            3: "crinkle",
            4: "waffle",
            5: "tornado",
            6: "wedge",
            7: "croquette",
            8: "popsicle"
        }
        selection = st.segmented_control(
            "Tool",
            options=option_map.keys(),
            format_func=lambda option: option_map[option],
            selection_mode="single",
        )

        if st.button('lets eat!'):
            if selection == [8]:
                st.snow()
                st.success(
                    'hey, not real yet anyway, but i can dream', icon='☃️')
            else: 
                st.error('i had one of those earlier today')
