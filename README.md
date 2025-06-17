# MediTrack - AI-Powered Healthcare App 🏥💡

MediTrack is a full-stack healthcare appointment app designed to provide easy appointment booking, secure user authentication, and an AI-powered symptom checker. The app is built with modern technologies and is deployable on cloud platforms.

---

## 🔧 Tech Stack

| Layer     | Technology                             |
|-----------|--------------------------------------|
| Frontend  | React.js + Tailwind CSS + TypeScript |
| Backend   | Django (Python)                      |
| Database  | MongoDB (via Djongo)                 |
| AI        | Simple AI symptom checker (keyword-based) |
| Deployment| Vercel (frontend), Heroku (backend) |

---

## 📁 Folder Structure

```
MediTrack_Final_App/
├── meditrack_backend/       # Django backend with MongoDB
│   ├── manage.py
│   ├── meditrack_backend/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── ai.py
│   │   ├── tests/
│   │   │   └── test_auth.py
│   ├── requirements.txt
│   ├── Procfile
│   └── runtime.txt
├── meditrack_frontend/      # React + Tailwind frontend
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── pages/
│   │   │   ├── AppointmentForm.jsx
│   │   │   ├── SymptomChecker.jsx
│   │   │   └── Auth.jsx
│   │   ├── services/
│   │   │   └── api.js
│   ├── .env
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── index.html
│   ├── package.json
│   └── vercel.json
├── venv/                    # Python virtual environment (ignored by Git)
├── .gitignore
└── README.md            # This file
```

---

## ⚙️ Backend Setup (Django + MongoDB)

### 1. Create & activate virtual environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r meditrack_backend/requirements.txt
```

### 3. Configure MongoDB in `meditrack_backend/settings.py`

Replace the `DATABASES` section with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'meditrack_db',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'your_mongodb_uri_here'
        }
    }
}
```

### 4. Run migrations and start the server

```bash
cd meditrack_backend
python manage.py migrate
python manage.py runserver
```

---

## 💻 Frontend Setup (React + Tailwind + TypeScript)

### 1. Install dependencies

```bash
cd meditrack_frontend
npm install
```

### 2. Run the development server

```bash
npm run dev
```

---

## 🔒 Environment Variables

Create `.env` files in **both** backend and frontend folders.

**Frontend (`meditrack_frontend/.env`):**

```
VITE_API_URL=http://localhost:8000
```

**Backend (`meditrack_backend/.env`):**

```
SECRET_KEY=your_django_secret_key
DEBUG=True
MONGODB_URI=your_mongodb_uri
```

---

## 🚀 Deployment

### Frontend (Vercel)

- Connect your repo to Vercel.
- Set `VITE_API_URL` environment variable.
- Deploy the frontend from `meditrack_frontend`.

### Backend (Heroku)

- Create a Heroku app.
- Ensure `requirements.txt`, `Procfile`, and `runtime.txt` are present.
- Set environment variables (`SECRET_KEY`, `DEBUG`, `MONGODB_URI`).
- Deploy backend code.

---

## ✅ Running Tests

**Backend:**

```bash
cd meditrack_backend
python manage.py test
```

**Frontend:**

```bash
cd meditrack_frontend
npm run test
```

---

## 🛑 .gitignore Highlights

Files and folders ignored by Git:

- `venv/`
- `node_modules/`
- `.env`
- `__pycache__/`
- build outputs like `dist/`

---

## 🧠 AI Feature

The backend includes a simple AI symptom checker (`api/ai.py`) that analyzes user symptoms using keyword matching. This can be extended with advanced machine learning models.

---

## 🙋 Contribution

Feel free to open issues or pull requests for improvements.

---

## 📝 License

MIT License © 2025 MediTrack Team

---

Thank you for using MediTrack! 🚀
