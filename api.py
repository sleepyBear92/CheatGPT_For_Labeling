import openai
from utils import Tokenizer

class RequestChatGPT:
    def __init__(self, key: str, response_token_num=300):
        self.key = key
        openai.api_key = self.key
        self.completion = openai.Completion()
        self.model_info = {'gpt-3.5-turbo':{'max_sequence':4097},
                           'gpt-3.5-turbo-0301':{'max_sequence':4097},
                           'text-davinci-003':{'max_sequence':4097},
                           'text-davinci-002':{'max_sequence':4097},
                           'text-babbage-001':{'max_sequence':2049},
                           'text-curie-001':{'max_sequence':2049},
                           'text-ada-001':{'max_sequence':2049}}
        self.response_token_num = response_token_num
        self.tokenizer = Tokenizer()
    
    def summary(self, model_name: str, instruction: str) -> str:
        # checking the length of a token
        est_token_num = self.tokenizer.count_tokens(instruction)
        response_token_num = self.response_token_num
        remain_token_num = self.model_info[model_name]['max_sequence'] - self.response_token_num - est_token_num
        if remain_token_num <= 0:
            print('Length exceeded')
            return 'Length exceeded'
        
        # Request API
        if model_name in self.model_info.keys():
            if model_name == 'gpt-3.5-turbo' or model_name == 'gpt-3.5-turbo-0301':
                completion = openai.ChatCompletion.create(
                    model=model_name,
                    messages=[{"role": "system", "content": instruction}],
                    max_tokens=response_token_num,
                    temperature=0.1,
                    top_p=1
                )
                return completion['choices'][0]['message']['content']
            else:
                completion = openai.Completion.create(
                    engine=model_name,
                    prompt=instruction,
                    max_tokens=response_token_num,
                    temperature=0.1,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                return completion['choices'][0]['text']
        else:
            raise ValueError("There is no such model with {}.".format(model_name))
        