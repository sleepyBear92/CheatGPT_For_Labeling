from transformers import GPT2Tokenizer
import os
import json

# Find all extension files in the subpath
def search_subdir(root, type='.json'):
    file_names = []
    for (path, dir, files) in os.walk(root):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == type:
                f = "{}/{}".format(path, filename)
                file_names.append(f)
    return file_names


# Count the number of tokens
class Tokenizer:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        
    def count_tokens(self, text):
        try:
            tokens = self.tokenizer.encode(text, return_tensors="pt")
            token_count = tokens.shape[1]
            return token_count
        except:
            print("Cannot count the number of tokens.")

    
if __name__=="__main__":
    tokenizer = Tokenizer()

    text = "Hello, how are you?"
    token_count = tokenizer.count_tokens(text)
    print(f"The number of tokens in the text is: {token_count}")