def run():
    print("This feature is not implemented yet.")

# ============================================
# TODO LIST - Git Branch Management Learning
# ============================================
# 
# This is a learning project for our team to practice Git workflows.
# Follow these steps to learn branch operations, merging, and pushing.
#
# NEXT STEPS:
#
# 1. [ ] Review Current Branch Status
#        - Run: git branch (to see all local branches)
#        - Run: git branch -a (to see all branches including remote)
#        - Run: git status (to check current branch and changes)
#
# 2. [ ] Create and Switch to a New Branch
#        - Run: git checkout -b feature/your-feature-name
#        - Or: git branch feature/your-feature-name && git checkout feature/your-feature-name
#
# 3. [ ] Make Changes and Commit
#        - Make some changes to files
#        - Run: git add .
#        - Run: git commit -m "Your commit message"
#
# 4. [ ] Push Your Branch to Remote
#        - Run: git push origin feature/your-feature-name
#        - Or: git push -u origin feature/your-feature-name (sets upstream tracking)
#
# 5. [ ] Switch Back to Main Branch
#        - Run: git checkout main
#        - Or: git checkout master (depending on your default branch name)
#
# 6. [ ] Pull Latest Changes from Remote
#        - Run: git pull origin main
#        - This ensures you have the latest changes before merging
#
# 7. [ ] Merge Your Feature Branch into Main
#        - Run: git merge feature/your-feature-name
#        - This will merge changes from feature branch into main
#
# 8. [ ] Resolve Merge Conflicts (if any)
#        - Open conflicted files and resolve conflicts manually
#        - Look for conflict markers: <<<<<<<, =======, >>>>>>>
#        - Run: git add <resolved-files>
#        - Run: git commit -m "Resolved merge conflicts"
#
# 9. [ ] Push Merged Changes to Remote
#        - Run: git push origin main
#
# 10. [ ] Delete Feature Branch (Optional - after successful merge)
#         Local: git branch -d feature/your-feature-name
#         Remote: git push origin --delete feature/your-feature-name
#
# ADDITIONAL PRACTICE:
#
# 11. [ ] Practice Viewing Merge History
#         - Run: git log --oneline --graph --all
#         - This shows a visual representation of branch history
#
# 12. [ ] Learn About Different Merge Strategies
#         - Fast-forward merge (default when possible)
#         - Three-way merge (when branches have diverged)
#         - Run: git merge --no-ff feature/branch-name (forces merge commit)
#
# 13. [ ] Practice Rebasing (Advanced)
#         - Run: git rebase main (while on feature branch)
#         - This replays your commits on top of main branch
#
# 14. [ ] Collaborate with Team Members
#         - Pull team members' branches
#         - Review their code
#         - Practice resolving conflicts together
#
# ============================================
# IMPORTANT NOTES:
# - Always pull before pushing to avoid conflicts
# - Communicate with team before merging to main
# - Test your code before merging
# - Write clear commit messages
# ============================================ 