# 🧾 Slush Bill Split – Take-Home Project by Stefano Rueda

## 🌟 Overview
This is a take-home project for Slush to build a simple, clean interface for manually splitting a bill between participants. The project includes:

- **Frontend**: Built with Next.js + Tailwind CSS
- **Backend**: FastAPI service deployed on Railway

The user can enter a total amount, add participants, assign individual splits manually, and validate the split.

---

## 🔗 Live Links

- 🌐 Frontend: [https://slush-frontend-wn6z.vercel.app](https://slush-frontend-wn6z.vercel.app)
- ⚙️ Backend: [https://slush-backend-production-bc16.up.railway.app](https://slush-backend-production-bc16.up.railway.app)

---

## 🖥 Tech Stack

### Frontend
- [Next.js](https://nextjs.org/) (App Router)
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS](https://tailwindcss.com/)

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) for serving
- [Pytest](https://docs.pytest.org/) for backend tests

---

## ⚙️ How to Run Locally

### Frontend
```bash
cd frontend
npm install
npm run dev
# Open http://localhost:3000
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# Open http://localhost:8000/docs to test
```

---

## 🔁 API Endpoint

`POST /validate-split`

**Request:**
```json
{
  "total": 125.00,
  "splits": {
    "Alice": 60,
    "Bob": 65
  }
}
```

**Response:**
```json
{
  "valid": true,
  "message": "Split is valid"
}
```

---

## ✅ Bonus Features
- [x] Even Split button
- [x] Validation for matching total and split
- [x] Unit tests for backend validation logic

---

## 📁 Repo Structure
```
frontend/
  ├── app/
  ├── components/
  └── utils/
backend/
  ├── main.py
  ├── test_main.py
  └── requirements.txt
```

---

## 🙌 Thanks!
