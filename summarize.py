import google.generativeai as palm

api_key_filepath = r".\Api.txt"
with open(api_key_filepath, 'r', encoding='utf-8') as file:
    api_key = file.read()
print(api_key)
palm.configure(api_key=api_key)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
}

filepath = ".\demo.txt"
with open(filepath, 'r', encoding='utf-8') as file:
    file_contents = file.read()

prompt = file_contents + "summarize this"
print("Summary:\n")
# prompt = input("User: ")
response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print("Chatbot:", response.result)
