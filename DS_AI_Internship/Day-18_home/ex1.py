# 1. Initialize git repository
git init

# 2. Create a file and make first commit
echo Hello > file.txt
git add file.txt
git commit -m "First commit"

# 3. Create a new branch called feature and change the file
git checkout -b feature
echo Hello from feature > file.txt
git add file.txt
git commit -m "Change in feature branch"

# 4. Go back to main branch and change the same file differently
git checkout main
echo Hello from main > file.txt
git add file.txt
git commit -m "Change in main branch"

# 5. Try to merge feature into main (this will cause conflict)
git merge feature