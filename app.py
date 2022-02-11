import os

from flask import Flask
from flask_discord_interactions import *
import requests
import io
import re
import internal_process as proc
from subprocess import Popen
from threading import Thread
from flask import send_file

app = Flask('')
discord = DiscordInteractions(app)

@app.route('/')
def a():
    return 'hello'

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]


@discord.command()
def ping(ctx):
    "Respond with a friendly 'pong'!"
    return "Pong!"

@discord.command()
def printer(ctx, user: User=None, link: str=None):
    "Print. That's all."
    params = {}
    pattern = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    if user is None and link is None:
        params['image_url'] = ctx.author.avatar_url
    elif user is None and link is not None and re.fullmatch(pattern, link):
        params['image_url'] = link
    elif user is not None and link is None:
        params['image_url'] = user.avatar_url
    elif user is not None and link is not None:
        return "Sorry, but it looks like you can't fill all of the two arguments!"

    answer = proc.request('print', params)
    with open(f"{ctx.id}.png", "wb") as f:
        f.write(answer)
    ctx.send(Message(file=(f'{ctx.id}.png', open(f'{ctx.id}.png', 'r'), 'image/png'))
    os.remove(f'{ctx.id}.png')
    
    

        

    

discord.set_route("/interaction")


#discord.update_commands(guild_id=os.environ['TESTING_GUILD'])

def run():
    app.run('0.0.0.0', 8080)

t = Thread(target=run)
t.start()
