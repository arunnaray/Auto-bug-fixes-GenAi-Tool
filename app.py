import streamlit as st
import os
from src.github_connector import clone_repo
from src.commit_analyzer import analyze_commits
from src.change_reporter import generate_report
from src.code_fixer import ask_openai_to_fix
from src.git_committer import commit_and_push

def display_code_diff(original_code, fixed_code):
    col1, col2 = st.columns(2)
    col1.markdown("### 🔴 Original Code")
    col1.code(original_code, language="python")
    col2.markdown("### ✅ Fixed Code")
    col2.code(fixed_code, language="python")

st.set_page_config(layout="centered")
st.title("🛠️ Auto Code Evaluator & Fixer (LLM-based)")

github_url = st.text_input("Enter GitHub Repo URL")

if "fix_stage" not in st.session_state:
    st.session_state.fix_stage = False
    st.session_state.changes = None
    st.session_state.repo_path = None

if st.button("🔍 Analyze Repo"):
    with st.spinner("Cloning and analyzing..."):
        repo_path = clone_repo(github_url)
        modules = ['module_a', 'module_b', 'module_c']
        changes = analyze_commits(repo_path, modules)
        report = generate_report(changes)
        st.session_state.fix_stage = False
        st.session_state.changes = changes
        st.session_state.repo_path = repo_path

    st.subheader("📊 Change Impact Report")
    st.dataframe(report)

if st.session_state.changes and st.button("✅ Apply Fixes and Push"):
    st.session_state.fix_stage = True

if st.session_state.fix_stage:
    st.subheader("🔧 LLM-Powered Fix Suggestions")
    modules = ['module_a', 'module_b', 'module_c']
    for mod in modules:
        if st.session_state.changes.get(mod):
            file_path = os.path.join(st.session_state.repo_path, f"{mod}.py")
            with open(file_path, "r") as f:
                original_code = f.read()
            st.write(f"🔍 Asking OpenAI to fix `{mod}.py`...")
            result = ask_openai_to_fix(original_code, st.session_state.changes[mod][0])
            st.success(f"✔ OpenAI responded for `{mod}.py`")

            display_code_diff(original_code, result["fixed_code"])
            st.markdown(f"**🔍 Reason:** {result['reason']}")
            st.markdown(f"**💡 Suggestions:** {result['suggestions']}")

            apply_key = f"apply_{mod}"
            if st.button(f"✅ Apply Fix to `{mod}.py`", key=apply_key):
                with open(file_path, "w") as f:
                    f.write(result["fixed_code"])
                st.success(f"✅ Fix applied to `{mod}.py`")

    if st.button("🚀 Commit & Push Fixes"):
        branch = commit_and_push(st.session_state.repo_path)
        st.success(f"✅ Fixes committed and pushed to branch: `{branch}`")
