import openai
import time

openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system",
                   "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
                  {"role": "user", "content": "How are you?"},
                  {"role": "assistant", "content": "I am doing well"},
                  {"role": "user", "content": prompt}]
    )

    return completion

# start the conversation
if __name__ == '__main__':
    print("Dobrý den, jsem AI, co vám odpoví na vaše otázky.")
    print("Prosim abyste používali pouze Angličtinu.")
while True:
    user_input = input("You: ")
    ai_response = generate_response(user_input)
    odpoved = ai_response['choices'][0]['message']['content']
    print(odpoved)
    time.sleep(1)
