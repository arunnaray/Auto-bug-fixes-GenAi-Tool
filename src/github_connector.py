import os
import git
import tempfile

def clone_repo(github_url: str) -> str:
    """
    Clones the GitHub repo to a temporary directory and returns the path.
    """
    repo_dir = tempfile.mkdtemp()
    git.Repo.clone_from(github_url, repo_dir)
    return repo_dir

def get_recent_commits(repo_path: str, n=5):
    repo = git.Repo(repo_path)
    return list(repo.iter_commits('main', max_count=n))
