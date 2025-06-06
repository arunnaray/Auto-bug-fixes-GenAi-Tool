import git

def commit_and_push(repo_path, branch_name="auto_fix"):
    repo = git.Repo(repo_path)
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()
    repo.git.add(A=True)
    repo.index.commit("Auto-applied fixes to impacted modules.")
    origin = repo.remote(name='origin')
    origin.push(refspec=f"{branch_name}:{branch_name}")
    return branch_name
