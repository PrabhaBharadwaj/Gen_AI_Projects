# Gen_AI_Projects

    This is the Generative AI repo, which holds all learning and projects related to Generative AI.

- We have stage branch. Always do changes by shifting to stage branch and then commit to stage, Later do pull request to merge to master branch

git checkout stage and then do changes and upload to stage and then to main

## Note to me:

- Dont clone this main branch on local copy. Local copy has .env etc which is not uploaded to Github, It may be replaced.
  - Better take local copy bkp and then clone and then replace bkp on cloned folder to keep .env etc

# For Others:

## Clone

- Clone this page

  ```
  git clone https://github.com/PrabhaBharadwaj/Gen_AI_Projects.git
  ```

- Change to stage branch

  ```
  git checkout stage
  ```

- Replace main branch content to local stage, in case stage is not uptodate with main branch

  ```
  git pull origin main
  ```

## Upload

- After changes check the status

  ```
  git status
  ```

- After changes add changes

  ```
  git add .
  ```

- Commit changes

  ```
  git commit -m "XXX Change done in this repo"
  ```

- Push changes

  ```
  git push origin stage
  ```

- Now changes are uploaded to stage , now in UI push changes from Stage to main by raising Pull request
