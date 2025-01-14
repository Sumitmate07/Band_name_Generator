import streamlit as st

def generate_band_names(word1, word2, symbol):
    band_names = [
        f"{symbol} {word1} {word2}{symbol}",
        f"The {word1}s {symbol}",
        f"{symbol} {word2} and the {word1}s",
        f"**{word1}** {symbol} {word2}",
        f"{word1} {symbol} of {word2}",
        f"{word1}{symbol}-{word2}",
        f"{word1}{symbol}{word2}",
        f"**{word2}** {symbol} {word1}",
        f"{word2} {symbol} of {word1}"
    ]
    return band_names

st.title("Band Name Generator🎸✨")
st.write("Enter two words and choose a symbol to generate a list of band names:")

# Get user input
word1 = st.text_input("Enter the first word:")
word2 = st.text_input("Enter the second word:")

# Select symbol
symbol = st.selectbox(
    "Choose a symbol:",
    ["*", "&", "+", "!", "♫", "∞", "♥", "#", "~", "⚡","🎸","✨"]
)

if st.button("Generate Band Names"):
    if word1 and word2:
        band_names = generate_band_names(word1, word2, symbol)
        st.write("Your generated band names are:")
        for name in band_names:
            st.markdown(f"- {name}")
    else:
        st.error("Please enter both words to generate band names.")

