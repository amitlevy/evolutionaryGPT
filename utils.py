import re
import sys
import os

def file_to_string(filename) -> str:
    with open(filename, 'r') as file:
        return file.read()
    
def code_from_response(response_text: str) -> str:
    """
    Extract python code enclosed in GPT response (from Eureka: Human-Level Reward Design)
    """

    patterns = [
        r'```python(.*?)```',
        r'```(.*?)```',
        r'"""(.*?)"""',
        r'""(.*?)""',
        r'"(.*?)"',
    ]

    for pattern in patterns:
        code_string = re.search(pattern, response_text, re.DOTALL)
        if code_string is not None:
            code_string = code_string.group(1).strip()
            break

    return response_text if not code_string else code_string

def block_print():
    """
    GPT sometimes adds prints, so I disable prints before running exec()
    """
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__