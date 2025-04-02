# visibrain-tech_test : 🎮 Twitch Video Finder
A web application that allows users to search for Twitch videos related to a specific video game using the Twitch API. The project is structured as a monorepo containing a FastAPI backend and a Vue.js frontend.

## 📌 Technologies
### Backend:
- **FastAPI** (Python) – for API development
- **Uvicorn** – for running the FastAPI server
- **Pydantic** – for data validation
- **MongoDB** – for storing game data
- **Pytest & pytest-asyncio** – for backend testing

### Frontend:
- **Vue.js** – for building the user interface
- **Axios** – for API requests
- **Vite** – for development and build setup

## ⚙️ Installation

### Prerequisites:

- **Python 3.8+**
- **pip** (Python package manager)
- **Virtual environment** (recommended)
- **Node.js** (v16+ recommended)
- **MongoDB** (running locally or via Docker)

### Setup Instructions:
1. **Clone the repository:**

```bash
git clone https://github.com/Charlotte-Men/visibrain-tech_test.git
cd visibrain-tech_test
```

2. **MongoDB Setup**
Install MongoDB Locally
Linux (Ubuntu):
```bash
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongod
```

3. **Backend set up:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Set up the .env file with mongo URI:
```bash
MONGO_URI=mongodb://localhost:27017
```

- Set up the .env file with Twitch API credentials (Documentation [here](https://dev.twitch.tv/docs/api/)).

You will need to create a profile on [Twitch developers](https://dev.twitch.tv/login)

- Run the FastAPI server:

```bash
fastapi dev backend/main.py  
```
The API will be available at [http://localhost:8000](http://localhost:8000).

4. **Frontend set up:**
```bash
cd frontend
npm install
npm run dev
```
This starts a development server at [http://localhost:5173/](http://localhost:5173/).

## 🚀 Usage
- Enter a game name in the search bar.
- The backend fetches the game ID from Twitch (or MongoDB cache).
- The backend retrieves Twitch videos for the game.
- The frontend displays the videos.
- Results refresh every 2 minutes.

## 🧪 Testing
### Backend:
Run tests using:

```bash
cd backend
pytest
```
### Frontend:
To be implemented (possible tools: Jest, Vue Test Utils).

## 📡 API Endpoints
[Api documentation](http://127.0.0.1:8000/docs)

### 🔍 Fetch Videos for a Game
Endpoint: `GET /videos/`

Query Param: `game_name=<game_name>`

Example Request:

```bash
curl "http://localhost:8000/videos/?game_name=Fortnite"
```
Example Response:

```json
{
  "videos": [
    {
      "id": "123456",
      "title": "Amazing Fortnite Match!",
      "url": "https://twitch.tv/video/123456",
      "thumbnail": "https://example.com/thumb.jpg"
    }
  ]
}
``` 
## 📁 Project Structure
```bash
visibrain-tech_test/
│── backend/              # FastAPI backend
│   ├── api/              # API endpoints
│   ├── db/               # MongoDB config
│   ├── models/           # Pydantic models
│   ├── services/         # Business logic
│   ├── tests/            # Unit tests
│   ├── .env.sample       # Sample environment variables
│   ├── main.py           # FastAPI entry point
│   └── requirements.txt  # Backend dependencies
│
│── frontend/             # Vue.js frontend
│   ├── src/
│   │   ├── assets/       # CSS sheets
│   │   ├── components/   # Vue components
│   │   ├── services/     # API handling
│   │   ├── App.vue       # Root Vue component
│   │   └── main.js       # Vue entry point
│   ├── package.json      # Frontend dependencies
│   └── vite.config.js    # Vite configuration
│
│── .gitignore
│── README.md
```

## 🔧 Possible Improvements
- Docker use for an easier setup & deployment, and better portability
### Backend:
- Integration tests to validate API endpoints
- Linter & Formatter (e.g., `black`, `Ruff`)
- Error handling improvements (e.g., Twitch API failures)

### Frontend:
- Unit & integration tests for components
- Error handling (e.g., API failures)
- User-friendly messages when no videos are found
- Better UI for failed requests (loading states, retries, etc.)
- Handle video thumbnails & placeholders
- Pagination support for large video lists
- Mobile responsiveness improvements