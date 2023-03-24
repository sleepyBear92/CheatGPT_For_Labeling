<div align="center">

<img src="https://github.com/sleepyBear92/CheatGPT_For_Labeling/blob/main/assets/cheatGPT2.png" width="1200px">

</div>

## Introduction
ChatGPT is a really good generation model. I'm not capable of developing such a model, but I thought. 
"Could I develop a model similar to ChatGPT with as few resources as possible?" 
So I decided to label the data with ChatGPT and learn this labeling, which has two advantages.

**1. we can reduce the resources for data acquisition.** 
- As of GPT3.5, one data instance costs only $0.008192!

**2. We can develop a model that can't beat ChatGPT, but can come close.** 
- You can experiment with different models using ChatGPT data, and use ChatGPT as a benchmark to select effective experiments.

To conclude, we've written an example code to call **ChatGPT using the API to label a conversation**, which is designed to **summarize the conversation.** If you want to do different labeling, just change the data and prompt!

## How to use it
**1. Prepare your data**
- Prepare the data you want to label in a txt file.
- In the txt file, one instance of data should be separated by **"\n\n".** To change the delimiter, change the value of "sep" in "load_data" in "main.py". 
- See the example data('data' folder) and preprocessing code('sampling_example.ipynb') for details

**2. Labeling**
```bash
python main.py --key {your_key} --model {model_name} --txt_path {sample.txt}
```
 Model Name         | Description                                                                                                                                                                                                                                                                                                                                 |
| :-----------------| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gpt-3.5-turbo      | Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003. Will be updated with our latest model iteration.                                                                                                                                                                                                   |
| gpt-3.5-turbo-0301 | Snapshot of gpt-3.5-turbo from March 1st 2023. Unlike gpt-3.5-turbo, this model will not receive updates, and will only be supported for a three month period ending on June 1st 2023.                                                                                                                                                          |
| text-davinci-003   | Can do any language task with better quality, longer output, and consistent instruction-following than the curie, babbage, or ada models. Also supports inserting completions within text.                                                                                                                                                  |
| text-davinci-002   | Similar capabilities to text-davinci-003 but trained with supervised fine-tuning instead of reinforcement learning                                                                                                                                                                                                                         |
| text-curie-001     | Very capable, faster and lower cost than Davinci.                                                                                                                                                                                                                                                                                           |
| text-babbage-001   | Capable of straightforward tasks, very fast, and lower cost.                                                                                                                                                                                                                                                                                |
| text-ada-001       | Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.                                                                                                                                                                                                                                               |
> Warning: Be sure to [check your usage](https://platform.openai.com/account/usage). If you don't have any credits available, you won't be able to use it anymore.

**3. ETC**
- You can also develop a **post-processing module** in 'postprocessor' to get only labeling results from the API results. This will require modifications based on the API results of the modified prompt.
- For an example, see 'postprocessing.py' in 'postprocessor'
