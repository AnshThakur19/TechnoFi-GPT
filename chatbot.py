import openai


openai.api_key = "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"

def askBot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    
    return response["choices"][0]["message"]["content"]
