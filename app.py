import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from src.rag_chain import create_rag_chain


print("Loading Medical ChatBot...\n")

rag_chain = create_rag_chain()


print("Medical ChatBot is Ready")
print("Type 'exit' to quit")

# chat loop
while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("\nChatBot: Goodbye!")
        break

    try:
        response = rag_chain.invoke(
            {
                "input": user_question
            }
        )

        print("\nChatBot:", response["answer"])
        print()

    except Exception as e:
        print("\nError:", str(e))
        print()