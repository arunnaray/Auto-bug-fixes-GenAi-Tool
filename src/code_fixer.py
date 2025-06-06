from openai import OpenAI
from difflib import unified_diff
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_code_diff(original: str, modified: str) -> str:
    diff = unified_diff(original.splitlines(), modified.splitlines(), lineterm='')
    return "\n".join(diff)

def ask_openai_to_fix(code: str, commit_msg: str) -> dict:
    prompt = f"""
You're an expert Python code reviewer and fixer.

Here is a code snippet:\n\n{code}\n\n
Commit message:\n{commit_msg}\n\n
1. Identify any potential bugs or issues.
2. Explain why the issues exist (logic error, misuse, etc.).
3. Suggest improvements or fixes.
4. Show the corrected code.

Respond strictly in this format:

---Reason---
<your analysis>

---Suggestions---
<your fix ideas>

---Fixed Code---
<only the corrected code>
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    full_response = response.choices[0].message.content
    parts = full_response.split("---")
    result = {
        "reason": "",
        "suggestions": "",
        "fixed_code": ""
    }
    for i, section in enumerate(parts):
        if "Reason" in section:
            result["reason"] = parts[i + 1].strip()
        elif "Suggestions" in section:
            result["suggestions"] = parts[i + 1].strip()
        elif "Fixed Code" in section:
            result["fixed_code"] = parts[i + 1].strip()
    return result
