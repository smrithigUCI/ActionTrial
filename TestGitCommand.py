import  git 

repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
origin = repo.remote(name='origin')
origin.push()
