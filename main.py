from api import RequestChatGPT
from prompt import prompt_fn
from postprocessor import postprocessor_fn

from tqdm import tqdm
import pandas as pd
import argparse


def load_data(file_path, sep='\n\n'):
    with open(file_path, "r") as f:
        text = ''.join(f.readlines())
    dialog_list = text.split(sep)
    
    return dialog_list

def prompt_data(path):
    with open(path+'prefix.txt', "r") as f:
        prefix = ''.join(f.readlines())
    with open(path+'surfix.txt', "r") as f:
        surfix = ''.join(f.readlines())
        
    return prefix, surfix
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type=str)
    parser.add_argument("--model", type=str)
    parser.add_argument("--response_token_num", default=300, type=str)
    parser.add_argument("--path", default='', type=str)
    parser.add_argument("--txt_path", type=str)
    parser.add_argument("--save_path", default='', type=str)

    args, _ = parser.parse_known_args()
    
    dialog_list = load_data(args.txt_path)    
    prefix, surfix = prompt_data(args.path)
   
    api = RequestChatGPT(args.key, args.response_token_num)
    df = pd.DataFrame({'prompt_type':[], 'dialog':[], args.model:[]})    
    prompt_name = "combination"
    # model_list = ['gpt-3.5-turbo', 'text-davinci-003', 'text-babbage-001']
    model_list = ['gpt-3.5-turbo']
    
    for dialog in tqdm(dialog_list):
        row_dic = {'prompt_type':prompt_name, 'dialog':dialog}
        for model_name in model_list:
            result = api.summary(model_name, prompt_fn[prompt_name](dialog, prefix, surfix))     
            
            # If you have developed a suitable post-processing module, please remove the comment.
            # result = postprocessor_fn["tuning1"](result)            
            row_dic[model_name] = result
        df = df.append(row_dic, ignore_index=True)
    
    df.to_csv(args.save_path+'/result.csv', index=False, sep='\t')