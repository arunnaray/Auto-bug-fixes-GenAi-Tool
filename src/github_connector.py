import os
import git
import tempfile

def clone_repo(github_url: str) -> str:
    repo_dir = tempfile.mkdtemp()
    git.Repo.clone_from(github_url, repo_dir)
    return repo_dir
