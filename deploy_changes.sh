# Update the Static Data Files in main branch
python find_video_info.py $YT_API_KEY
# Add and Commit the changes
git add .; git commit -m "Updating the data as of `date`"
# Push the changes to main branch
git push origin main


# Make New Branch prod to puch changes
git checkout -b prod
# Deploye the New Changes
hugo
# Move all the changes to docs dir for deployment
rm -rf docs;mv public docs; mv resources docs/; cp CNAME docs/
# Add the changes
git add .
# Commited the Chages to GH repo
git commit -m "Updating the data as of `date`"
# Push the Chages
git push origin prod -f
# Remove the branch
git checkout main; git branch -D prod