[Introduction]
ChatGPT is a really good generation model. I'm not capable of developing such a model, but I thought. 
"Could I develop a model similar to ChatGPT with as few resources as possible?" 
So I decided to label the data with ChatGPT and learn this labeling, which has two advantages.

1. we can reduce the resources for data acquisition. 
- As of GPT3.5, one data instance costs only $0.008192!

2. We can develop a model that can't beat ChatGPT, but can come close. 
- You can experiment with different models using ChatGPT data, and use ChatGPT as a benchmark to select effective experiments.

To conclude, we've written an example code to call ChatGPT using the API to label a conversation, which is designed to summarize the conversation. If you want to do different labeling, just change the data and prompt!

[How to use it]
1. Prepare your data
- Prepare the data you want to label in a txt file.
- In the txt file, one instance of data should be separated by "\n\n". To change the delimiter, change the value of 'sep' in 'load_data' in 'main.py'. 
- See the example data ('data' folder) and preprocessing code ('sampling_example.ipynb') for details.

2. labeling
- python main.py --key {your_key} --model {model_name} --txt_path {sample.txt}
- your_key can be obtained after signing up at this link.
- For model_name, you can use one of the models below.
{Table} 
- Warning: Be sure to check your usage. If you don't have any credits available, you won't be able to use it anymore.

2. labeling
- python main.py --key {your_key} --model {model_name} --txt_path {sample.txt}
- your_key can be obtained after signing up at this link.
- For model_name, you can use one of the models below.
{Table} 
- Warning: Be sure to check your usage. If you don't have any credits available, you won't be able to use it anymore.

3. etc
- You can also develop a post-processing module in 'postprocessor' to get only labeling results from the API results. This will require modifications based on the API results of the modified prompt.
- For an example, see 'postprocessing.py' in 'postprocessor'