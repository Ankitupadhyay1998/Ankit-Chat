import os
from groq import Groq

client = Groq(
    api_key="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"
)

# Open file once in append mode, write continuously until user exits
with open("response.txt", "a", encoding="utf-8") as file:
    while True:
        question = input("Ask a question (or type 'exit' to quit): ").strip()
        if question.lower() == "exit":
            print("Exiting... all Q&A saved to response.txt")
            break

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model="groq/compound",
        )

        answer = chat_completion.choices[0].message.content
        print(f"\nAnswer: {answer}\n")

        # Write both question and answer to file
        file.write(f"Q: {question}\n")
        file.write(f"A: {answer}\n")
        file.write("-" * 40 + "\n")  # separator for readability
        file.flush()  # ensure it's written immediately
