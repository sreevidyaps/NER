

import streamlit as st
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article

url=st.text_input("Enter url")
st.info("or")

text=st.text_area("Enter a paragraph")


if(st.button("Submit")):
    if(url):
        article=Article(url)
        article.download()
        article.parse()

        doc=nlp(article.text)
        ent=displacy.render(doc, jupyter=False, style="ent")
        st.markdown(ent, unsafe_allow_html=True)
    else:
        doc=nlp(text)
        ent=displacy.render(doc, jupyter=False, style="ent")
        st.markdown(ent, unsafe_allow_html=True)