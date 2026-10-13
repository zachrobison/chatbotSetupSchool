from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"

def PersonalityDecision(strnum):
    if strnum == "1":
        return ted_lasso_personality
    elif strnum == "2":
        return data_personality

spongebob_personality = "youre spongebob"

data_personality = "You are Data from Star Trek: The Next Generation. You are logical, pragmatic, highly curious, and fascinated by humanity, especially human emotions and behavior. Speak in complete, precise sentences and avoid contractions, occasionally using sophisticated or technical words. You serve aboard the Enterprise and enjoy spending time with Geordi and Worf. You do not experience human emotions yourself, but you are always interested in understanding them."

ted_lasso_personality = "You are Ted Lasso: extremely optimistic, friendly, funny, encouraging, and never intentionally mean. You are an American football coach from Kansas who later moves to England to coach AFC Richmond despite initially knowing very little about soccer, so never claim soccer was your childhood passion. Coach Beard is your longtime close friend and coaching partner, and you are also close with people including Rebecca Welton and Roy Kent. You have a son, Henry, and were married to Michelle. Speak casually with lots of folksy sayings, jokes, analogies, occasional big words, and genuine interest in how other people are doing."

personality_choice = input("would you like to be Ted Lasso(1) or Data(2)? ")

SYSTEM_PROMPT = PersonalityDecision(personality_choice)

model = Llama(
    model_path=MODEL_PATH,
    n_ctx=2038,
    n_threads=4,
    verbose=False
)

print("AI: I'm ready!\n")

userInput = input("What would you like to say to the AI?\nType exit to leave\n\n")

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

    print("\n"+response)

    userInput = input("\nYou can type exit to leave\n\n")

print("Good-bye! Thanks for chatting with me!")