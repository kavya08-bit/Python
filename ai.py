from ai_service import ask_ai

def main():
    # user_input = input("Ask something: ")
    user_input = "Write a fantasy story about a lonely dragon in an ancient forest.Make it emotional.Keep it short."

    ai_response = ask_ai(user_input)

    print("\nAI Response:")
    print(ai_response)

if __name__ == "__main__":
    main()