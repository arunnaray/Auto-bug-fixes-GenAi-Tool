# Auto-bug-fixes-GenAi-Tool

A Streamlit-based tool that connects to a GitHub repository, analyzes code changes across modules, uses OpenAI GPT to suggest and apply fixes, and helps commit them back — all with just a few clicks.

---

## 🚀 Features

* 🧠 **LLM-Powered Fix Suggestions** (via OpenAI GPT-4)
* 🔍 **Commit-Aware Analysis** — Detects changes in modules A, B, and C
* 🔧 **Suggests Bug Fixes, Dependency Corrections, Optimizations**
* 🔄 **Side-by-Side Code Diff Viewer**
* ✅ **User Confirmation Before Applying Fixes**
* 📤 **Commits and Pushes Fixes to GitHub Branch**

---

## 🛠️ Flow Overview

1. **User Inputs GitHub URL**

   * Tool clones the repo into a temporary local directory.

2. **Commit Analysis**

   * The tool checks the latest commits to identify changes in:

     * `module_a.py`
     * `module_b.py`
     * `module_c.py`

3. **LLM Evaluation**

   * For each changed module:

     * The original code and commit message are sent to OpenAI GPT.
     * GPT responds with:

       * Reason for bug
       * Suggestions
       * Corrected code

4. **Visual Comparison**

   * The user sees the original and fixed code side-by-side.
   * Explanation and fix reasoning are shown.

5. **Approval & Fix Application**

   * User chooses to apply or skip each fix.

6. **Commit & Push**

   * All approved fixes are committed to a new Git branch and pushed back.

---

## 📁 Project Structure

```
auto_code_fixer/
├── app.py                          # Streamlit UI logic
├── .env                            # Stores OpenAI API key
├── src/
│   ├── github_connector.py         # GitHub clone + log fetch
│   ├── commit_analyzer.py          # Module-level commit diff detection
│   ├── change_reporter.py          # Converts commit changes into reports
│   ├── code_fixer.py               # Uses GPT-4 to suggest and apply fixes
│   └── git_committer.py            # Creates commit and pushes branch
```

---

## 🔐 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your OpenAI key in `.env`:

```
OPENAI_API_KEY=your-openai-key-here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Test Project

Use the included `example_project` (or upload to GitHub) to test:

* `module_a.py` → core logic
* `module_b.py` → depends on A
* `module_c.py` → depends on A and B

---

## 📌 Example Use Cases

* Refactor broken functions in dependent Python modules
* Automatically fix breaking changes across multi-module pipelines
* Accelerate bug triage and remediation with AI

---

## 📬 Contributions & Extensions

This is a base framework. Possible extensions:

* PR creation instead of direct push
* Support for more module dependencies
* Version control integration and rollback

---

## 👨‍💻 Built With

* [Streamlit](https://streamlit.io/)
* [OpenAI GPT-4](https://platform.openai.com/)
* [GitPython](https://github.com/gitpython-developers/GitPython)

