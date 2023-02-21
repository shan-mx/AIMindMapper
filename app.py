import openai
import streamlit as st
import os
import xmind
from helper import *
from vars import *

openai.api_key = api_key
st.set_page_config(page_title='AI MindMapper', page_icon='🤖')
st.title('AI MindMapper')
topic = st.text_area('Topic or Text', '')
gen_button = st.button('Generate')
if gen_button:
    with st.spinner("Please wait..."):
        d = eval(openai.Completion.create(model="text-davinci-003", prompt=instruction_prompt + topic + "\n", max_tokens=3000, temperature=0.3)["choices"][0]["text"])
        print(d)
        #except:
        #    st.error("There's an error accessing the GPT model, please try again.")
        #    exit(0)
        topic = d["title"]
        st.markdown(generate_markdown(d))
        workbook = xmind.load(topic + ".xmind")
        sheet = workbook.getPrimarySheet()
        sheet.setTitle(topic)
        root_topic = sheet.getRootTopic()
        root_topic.setTitle(topic)
        for each in d["children"]:
            add_subtopic(root_topic, each)
        xmind.save(workbook, path=topic + '.xmind')
        with open(topic + '.xmind', 'rb') as f:
            st.download_button('Download XMind File (for XMind 8)', f, file_name=topic + '.xmind')
        os.remove(topic + '.xmind')