# Make New Branch prod to puch changes
git checkout -b prod
# Update the Static Data Files
python find_video_info.py $YT_API_KEY
# Deploye the New Changes
hugo
# Move all the changes to docs dir for deployment
rm -rf docs;mv public docs; mv resources docs/; cp CNAME docs/
# Add the changes
git add .
# Commited the Chages to GH repo
git commit -m "Updating the data as of `date`"
# Push the Chages
git push origin prod
# Remove the branch
git checkout main; git branch -D prod