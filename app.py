import openai
import streamlit as st
import os
import xmind
from helper import *
from vars import *

openai.api_key = api_key1 + api_key2
st.set_page_config(page_title='AI MindMapper')
st.title('AI MindMapper')
topic = st.text_area('Topic or Text', '')
gen_button = st.button('Magic!')
if gen_button and topic != "":
    with st.spinner("Processing..."):
        model_para = {
            "model": "text-davinci-003",
            "prompt": instruction_prompt + topic + "\n",
            "max_tokens": 4000 - int(len(topic) * 2.1),
            "temperature": 0.3
        }
        d = openai.Completion.create(**model_para)
        try:
            d = eval(d["choices"][0]["text"])
        except TypeError:
            st.error("Disconnected from OpenAI. Please try again later")
            exit(0)
        except SyntaxError:
            st.error("Format Error. Please use another prompt")
            exit(0)
        topic = d["title"]
        workbook = xmind.load(topic + ".xmind")
        root_topic = workbook.getPrimarySheet().getRootTopic()
        root_topic.setTitle(topic)
        tmp = [add_subtopic(root_topic, each) for each in d["children"]]
        xmind.save(workbook, path=topic + '.xmind')
        with open(topic + '.xmind', 'rb') as f:
            down = st.download_button('Download XMind File (for XMind 8 only)', f, file_name=topic + '.xmind')
        os.remove(topic + '.xmind')
        st.markdown(generate_markdown(d))
