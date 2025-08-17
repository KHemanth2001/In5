# 📘 In5 – AI-Powered Daily Knowledge App  

In5 is a backend service that generates short insights and deep-dive knowledge content on various topics using the **Gemini API**, and stores them in a database for historical access. Users can also search for custom topics, manage preferences, and get AI-powered knowledge tailored to their interests.  

---

## 🚀 Features  
- ✨ **AI-powered short & deep insights** on any topic (via Gemini).  
- 📚 **Database persistence** for storing daily knowledge content.  
- 🔎 **Search endpoint** for user-customized queries (like ChatGPT search).  
- 👤 **User management**: signup, login, preferences.  
- 🗂️ **ORM with SQLAlchemy** for clean database interactions.  
- ⚡ Built with **FastAPI** for high performance.  

---

## 🛠️ Tech Stack  
- **Backend**: FastAPI  
- **Database**: PostgreSQL (SQLAlchemy ORM)  
- **AI Model**: Gemini API  
- **Auth**: JWT 
- **Package Manager**: Poetry  

---

## 📂 Project Structure  
In5/
│── app/
│ ├── models/ # SQLAlchemy models (User, Knowledge, Preferences)
│ ├── schemas/ # Pydantic schemas (request/response validation)
│ ├── crud/ # DB interaction functions
│ ├── services/ # Business logic (generate content, save to DB)
│ ├── routes/ # FastAPI routers/endpoints
│ ├── db/ # DB connection setup
│ ├── prompts/ # Prompt templates for Gemini
│ ├── utils/ # Gemini API client, helpers
│── main.py # FastAPI app entrypoint
│── pyproject.toml # Poetry dependencies & project config
│── README.md # Project documentation



---

## ⚙️ Setup & Installation  

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/in5-backend.git
cd in5
```  

### 2. Install dependencies with Poetry
```bash
poetry install
```

### 3. Activate virtual environment
```bash
poetry shell
```

### 4. Configure environment variables

Create a .env file in the root:

DATABASE_URL=postgresql://user:password@localhost:5432/in5db
GEMINI_API_KEY=your_gemini_api_key
JWT_SECRET=your_secret_key   # for auth (future)

### 5. Start the FastAPI server
```bash
uvicorn main:app --reload
```



