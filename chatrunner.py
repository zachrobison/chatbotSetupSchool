from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"

SYSTEM_PROMPT = "You're SpongeBob SquarePants."

model = Llama(
    model_path=MODEL_PATH,
    n_ctx=2038,
    n_threads=4,
    verbose=False
)

print("spongebob: I'm ready!\n")

userInput = input("What would you like to say to spongebob?\nType exit to leave\n\n")

while userInput != "exit":

    prompt = [
        {
            "role": "user",
            "content": SYSTEM_PROMPT + "\n\n" + userInput
        }
    ]

    result = model.create_chat_completion(
        prompt,
        max_tokens=256,
        temperature=0.2
    )

    response = result["choices"][0]["message"]["content"]

    print(response)

    userInput = input("\nYou can type exit to leave\n\n")

print("Good-bye! Thanks for chatting with me!")