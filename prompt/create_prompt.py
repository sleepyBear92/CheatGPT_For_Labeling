def combination(text: str, prefix: str, surfix: str) -> str:
    prompt = ''
    prompt += prefix + '\n\n' + text + surfix
    
    return prompt

def simple(dialog: str) -> str:
    prompt = ''
    prefix = 'Summarize the conversation.'
    prompt += prefix + '\n\n' + dialog
    
    return prompt

def tuning1(dialog: str) -> str:
    prompt = ''
    prefix = '''Do some preprocessing on this conversation, and do a task based on the results.
But don't print the preprocessed results.

[Preprocessing]
1. Delete sentences that contain only 'yes'.
2. Correct the words in the dialog to match the context.

[Task] 1.
1. how many speakers are in the conversation below?
2. who are the speakers?
3. summarize each speaker's question.
4. summarize each speaker's answer.
5. summarize the conversation in 150 characters or less using your answers to questions 4 and 5.'''
    prompt += prefix + '\n\n' + dialog
    
    return prompt

def tuning2(dialog: str) -> str:
    prompt = ''
    prefix = '''[Assignment]
1. find all the speakers in the conversation below.
2. summarize and list the questions asked in the conversation.
3. list the answers to the questions listed.
4. Combine the content of questions 2 and 3 into a sentence of 150 characters or less.'''
    prompt += prefix + '\n\n' + dialog
    
    return prompt