import re

def simple(result: str) -> str:
    return result.strip()

def tuning1(result: str) -> str:
    pattern = r'^5\.(.+)$'
    match = re.search(pattern, result, re.MULTILINE)

    if match:
        result = match.group(1).strip()
    else:
        return "No match found."
    return result

def tuning2(result: str) -> str:
    pattern = r'^4\.(.+)$'
    match = re.search(pattern, result, re.MULTILINE)

    if match:
        result = match.group(1).strip()
    else:
        print("No match found.")

    return result


if __name__=="__main__":
    
    result = '''[Assignment]
1. There are a total of 2 speakers.
2. The customer service representative is named Sarah Johnson, and the customer is anonymous.
3. Customer's questions: Is there a Burberry store in the Macy's department store? / Which location? / Is there a Missha store as well?
4. Representative's answers: Are you looking for a place that sells soap? / It operates as a unified exchange center. / The Bobbi Brown store in the Macy's department store in Dayton was closed at the end of August, twenty years ago. / The Missha store is located on this floor.
5. The customer asked for the location of the Burberry and Missha stores in the Macy's department store, and the representative provided the locations of each store. The Bobbi Brown store has already closed down.
'''
    
    print(tuning1(result))