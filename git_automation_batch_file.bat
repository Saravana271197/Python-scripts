@ECHO OFF 

:: This batch file automates commands of git
git status
echo '**************************************************'
echo "Performing an add for all files in this directory"
git add .
git status
echo '**************************************************'
echo 'Enter the commit message:'
read CommitMessage
git commit -m "$CommitMessage"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
git push -u origin master
echo '**************************************************'
echo 'Done!'