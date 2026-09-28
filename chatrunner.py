from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"

SYSTEM_PROMPT = ("you're name is ted, you're a normal person")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Ted: I'm ready!\n")

userInput = input("What would you like to say to Ted?\n Type exit to leave \n\n")

while userInput != "exit":
    prompt = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 0.2)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")