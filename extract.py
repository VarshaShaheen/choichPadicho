import ollama

res = ollama.chat(
    model="llava",
    messages=[
        {
            'role': 'user',
            'content': 'Extract the text from this image and give it to me.',
            'images': ['image.png']
        }
    ]
)

print(res['message']['content'])
