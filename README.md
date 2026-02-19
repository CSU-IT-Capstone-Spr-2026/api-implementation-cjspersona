[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zN2AskmG)
# XKCD Comic Viewer

[Add your 2-3 sentence description of what your application does here]

## Features Implemented

Check off the features you implemented (must have at least 4 and 2 are implemeted for you already):

- [X] Feature #1: Display the Latest Comic
- [X] Feature #2: Display a Specific Comic by Number
- [X] Feature #3: Random Comic Button
- [X] Feature #4: Navigation (Previous/Next)
- [X] Feature #5: Search by Comic Number Form
- [ ] Feature #6: Display Multiple Recent Comics

## Technologies Used

- Python 3.8+
- Flask 3.0.0
- Requests 2.31.0
- XKCD API

## Installation and Setup

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Steps to Run

1. Clone or download this repository

2. Navigate to the project directory in your terminal:
   ```
   cd projectName
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Usage

[Explain how to use your application - what can users do? What buttons should they click?]

## Screenshots

[Add screenshots of your application here - you can drag and drop images into GitHub or use Markdown image syntax]

Example:
```

<img width="704" height="772" alt="Screenshot 2026-02-18 210929" src="https://github.com/user-attachments/assets/3ad089c2-4570-4586-af57-719d0352afc8" />

<img width="693" height="791" alt="Screenshot 2026-02-18 211012" src="https://github.com/user-attachments/assets/6d0b79f7-2909-43f6-92a3-458419c81b4d" />


```

## API Endpoints Used

- `GET /info.0.json` - Fetches the latest comic
- `GET /{comic_number}/info.0.json` - Fetches a specific comic by number

## Challenges and Solutions

[Write 2-3 paragraphs about:]
One challenge I ran into was handling invalid comic numbers. Some XKCD comic numbers don’t exist, so the API sometimes returned as an error. My way of solving this were adding checks and error handling so the app shows an error message instead of crashing.

Another challenge was making sure the Previous and Next buttons worked correctly. I had to prevent the user from going below comic #1 or past the newest comic. I fixed this by fetching the latest comic number and using it as the limit for navigation.

This assignment helped me understand how to make API requests, work with JSON data, and display it in a Flask web application.

## Future Improvements

[Optional: What would you add if you had more time?]
 Add a page that shows the 5 most recent comics in a grid like layout. Also, I would personally fix up the UI and the design.

## Author

CJ
