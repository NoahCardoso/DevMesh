import ollama
response = ollama.chat(
    model='qwen2.5-coder:7b',
    messages=[{'role': 'user', 'content': 'Write a hello world in Python'}]
)
print(response['message']['content'])