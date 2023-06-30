from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import streamlit as st
import openai

ANTHROPIC_API_KEY = "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"

anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

st.set_page_config(page_title="My GPT - by Shravan", page_icon="🤖")

openai.api_key = "Your API KEY"

st.title("AI Text Gen 🤖")
st.subheader("Write the Prompt")
prompt = st.text_area("Prompt", "Enter the Text Here")

check = st.button("Ask the AI")
if check:
    st.subheader("Anthropic Claude AI")
    completion = anthropic.completions.create(
        model="claude-1",
        max_tokens_to_sample=250,
        prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}",
    )
    out = completion.completion
    st.write(out)

    st.subheader("OpenAI Davinci-3 AI")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}",
        max_tokens=100,
        temperature=0
    )
    text = completion.choices[0].text
    st.write(text)
