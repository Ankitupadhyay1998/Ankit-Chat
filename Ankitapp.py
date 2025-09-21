import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# Streamlit UI
st.set_page_config(page_title="Interactive LLM Chat", page_icon="💬")
st.title("💬 Interactive Q&A Chat")

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box for user question
question = st.text_input("Type your question here:")

# When user clicks Send
if st.button("Send"):
    if question.strip() != "":
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model="groq/compound",
        )
        answer = chat_completion.choices[0].message.content

        # Append to session history
        st.session_state.history.append((question, answer))

        # Save to file
        with open("response.txt", "a", encoding="utf-8") as file:
            file.write(f"Q: {question}\nA: {answer}\n{'-'*40}\n")

# Display chat history in chat style
for q, a in st.session_state.history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    st.markdown("---")
