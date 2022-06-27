# Importing stuff
import utils.upload_util as up
import utils.title_util as tt
import utils.discord_util as dc
from datetime import datetime
from time import sleep
import os

def discord_msg(status,link):
        e = dc.discord.Embed(title="Upload Status", description=status)
        e.add_field(name="Title", value=title)
        e.add_field(name="Link", value=link)
        e.add_field(name="Time", value=str(datetime.now()))
        dc.webhook.send(embed=e, username='AutoYoutube')

#----------- Main Loop -----------

while True:
        file_path = os.listdir('clips') # puts the name of the clips in a list
        if len(file_path) == 0:         # checks if the directory is empty
                print('No files')
                break

        file = 'clips/'+file_path[0]
        title = tt.title_selector()   # generates a random title
        description = "Good day!"
        keywords = 'memes,gaming'
        privacy = 'public'
        video_data_up = {
                "file": file,
                "title": title,
                "description": "#shorts \n" + description,
                "keywords": keywords,
                "privacyStatus": privacy
        }
        try:
                up.upload_video(video_data_up) # uploads the videos with the above arguments
                url = 'https://www.youtube.com/watch?v='+up.video[0] # makes the url the video
                up.video.clear()

                sleep(5)
                discord_msg('Uploaded!',url)  # Notifies you on discord about the upload status
                os.remove(file)  # deletes the file after upload
                sleep(28800)  # waits for 8hr to upload the next video (3 videos a day!)
        except:
                discord_msg('Error Uploading!','None') # If somehow it fails to upload, it waits for 6 seconds and then tries again!
                sleep(6)
                continue




