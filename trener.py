import aiml

def learn_aiml(kernel):
    kernel.learn("hockey_chat.aiml")

def main():
    kernel = aiml.Kernel()
    learn_aiml(kernel)

    while True:
        input_text = input("> Ojciec: ")
        response = kernel.respond(input_text)
        print("Trener: " + response)

        # Sprawdź, czy bot powinien zakończyć rozmowę
        if response == "Do widzenia!":
            break

if __name__ == "__main__":
    main()