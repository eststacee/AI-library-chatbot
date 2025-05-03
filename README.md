#  AI Library Chatbot – Book Search Assistant

This project is a Python-based AI chatbot that helps users search for books in a library system using natural language. It supports fuzzy title matching, author queries, and genre filtering. The chatbot is deployed online and accessible through a browser-based interface.

##  Features

- Search by **book title**, **author**, or **genre**
- Fuzzy matching for misspelled or partial titles
- Real-time web-based chat interface
- Deployed online using **Render**
- Hosted frontend works with **GitHub Pages** or locally
- CORS enabled for cross-origin requests

##  Technologies Used

- Python 3.x
- Flask (web framework)
- flask-cors (CORS handling)
- difflib (for fuzzy search)
- HTML + JavaScript (frontend)
- Render.com (live deployment)
- GitHub (version control)

##  Project Structure

- `app.py` – Flask server and chatbot logic
- `catalog.json` – Sample book database with genres
- `templates/chat.html` – Frontend chat interface
- `requirements.txt` – Required Python libraries
- `render.yaml` – Render deployment config
- `README.md` – Project overview and setup guide

##  Live Demo

- 🌐 [https://ai-library-chatbot.onrender.com](https://ai-library-chatbot.onrender.com)

##  Example Inputs

| User Input                   | Bot Response Example                          |
| `river source`               | `'The River and the Source' by...`            |
| `books by Chinua Achebe`     | List of books by that author                  |
| `fiction books`              | All fiction books in the catalog              |
| `Harry Potter`               | Not found message                             |

##  How to Run Locally

1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run app: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser

##  Author

- **Name**: Stacey Nyongesa
- **Course**: Business and Information Automation
- **Institution**: The University of Nairobi
