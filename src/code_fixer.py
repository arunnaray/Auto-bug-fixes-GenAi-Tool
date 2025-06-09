import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    full_response = response["choices"][0]["message"]["content"]
    parts = full_response.split("---")
    result = {"reason": "", "suggestions": "", "fixed_code": ""}
    for i, section in enumerate(parts):
        if "Reason" in section:
            result["reason"] = parts[i + 1].strip()
        elif "Suggestions" in section:
            result["suggestions"] = parts[i + 1].strip()
        elif "Fixed Code" in section:
            result["fixed_code"] = parts[i + 1].strip()
    return result
