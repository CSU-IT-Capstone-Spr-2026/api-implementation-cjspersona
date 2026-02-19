"""
XKCD Comic Viewer - Starter Code
"""
from flask import Flask, render_template, request, redirect, url_for
import requests
import random


app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"

def get_latest_comic():
    # Fetch the most recent XKCD comic from the API and returns dict: Comic data if successful, None if there's an error
    try:
        response = requests.get(f"{XKCD_BASE_URL}/info.0.json")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
            


def get_comic_by_number(comic_num):
    # Fetch a specific XKCD comic by its number. Takes argument comic_num (int): The comic number to fetch
    try:
        response = requests.get(f"{XKCD_BASE_URL}/{comic_num}/info.0.json")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Comic #{comic_num} not found")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


@app.route('/')
def index():
    #Home page - displays the latest XKCD comic. Implements Feature #1: Display the Latest Comic
    # Fetch the latest comic and if successful, render the template with comic data else show an error
    comic = get_latest_comic()
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None, 
                             error="Sorry, we couldn't fetch the comic right now. Please try again later.")


@app.route('/comic/<int:comic_num>')
def show_comic(comic_num):
    # Display a specific comic by number. Use this as a reference for implementing other features. example websiteUrl.com/comic/234
    # Validate comic number will pull back a comic
    if comic_num < 1 or comic_num > 3200:
        return render_template('index.html', comic=None,
                             error="Invalid comic number. Comics start at #1.")
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                             error=f"Comic #{comic_num} could not be found. It may not exist.")
    
@app.route('/random')
def random_comic():
    latest = get_latest_comic()
    if not latest:
        return render_template('index.html', comic=None,
                               error="Could not fetch the latest comic to generate a random comic.")

    max_num = latest["num"]
    rand_num = random.randint(1, max_num)

    comic = get_comic_by_number(rand_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                               error="Random comic could not be loaded. Please try again.")


@app.route('/navigate/<int:comic_num>/<direction>')
def navigate_comic(comic_num, direction):
    latest = get_latest_comic()
    if not latest:
        return render_template('index.html', comic=None,
                               error="Could not fetch latest comic for navigation.")

    max_num = latest["num"]

    if direction == "prev":
        new_num = comic_num - 1
    elif direction == "next":
        new_num = comic_num + 1
    else:
        return render_template('index.html', comic=None,
                               error="Invalid navigation direction.")

    if new_num < 1:
        new_num = 1
    if new_num > max_num:
        new_num = max_num

    return redirect(url_for("show_comic", comic_num=new_num))


@app.route('/search', methods=["POST"])
def search_comic():
    comic_num = request.form.get("comic_num")

    if not comic_num or not comic_num.isdigit():
        return render_template('index.html', comic=None,
                               error="Please enter a valid comic number.")

    comic_num = int(comic_num)

    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                               error=f"Comic #{comic_num} could not be found.")

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
