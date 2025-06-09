import git
from typing import List, Dict

def analyze_commits(repo_path: str, modules: List[str]) -> Dict[str, List[str]]:
    repo = git.Repo(repo_path)
    diff_summary = {mod: [] for mod in modules}
    for commit in repo.iter_commits('main', max_count=10):
        diff = commit.diff(commit.parents[0] if commit.parents else git.NULL_TREE, create_patch=False)
        for d in diff:
            for mod in modules:
                if f"{mod}.py" in d.a_path or f"{mod}.py" in d.b_path:
                    diff_summary[mod].append(commit.message.strip())
    return diff_summary
