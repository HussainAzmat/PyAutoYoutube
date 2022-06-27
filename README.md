
# ✨ PyAutoYoutube ✨

A Python Script which simply uploads 3 videos a day on Youtube with a generated random title and also notifies on discord about the upload status of videos!


## ☄️ What does it do?

 - Chooses the first video from the given videos.
 - Generates a random title out of the given keywords.
 - Uploads the video using Youtube Data V3 API.
 - Notifies on discord using webhooks.
 - Sleeps for 8hrs
 - Repeat :)


## 🛠 Installing

Step 1:

```bash
  git clone https://github.com/notAZMAT/PyAutoYoutube/

  cd PyAutoYoutube
```
Step 2:

```bash
  pip3 install -r requirements.txt
```


## 💡 Setting Up

There are some things which you need to setup before using the script.

- Create a Project in Google cloud with Youtube Data V3 API enabled.
- Create Oauth2 Credentials and update your details to the ```client_secrets.json``` file in ```utils``` directory of this Project.
- Use your own keywords in the file ```title_util.py``` in the ```utils``` directory.
- Upload your clips in the ```clips``` directory.
- Change the discord webhook in the ```discord_util.py``` in the ```clips``` directory.


## ⚡️ Starting

- Run the ```main.py``` file and authorise it on your computer.
- After authorising for the first time, it will create a file ```main.py-oauth2.json```.
- Deploy the whole project on cloud.
- Run :)


## 📝 Contact

For support, email at azmathussainearn@gmail.com

