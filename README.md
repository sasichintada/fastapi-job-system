
---

## 📌 FastAPI Background Job Processing System

A backend service built with **FastAPI** that handles **asynchronous job processing with JWT authentication**, SQLite database, and job lifecycle tracking.

---

## 🚀 Features

* 🔐 JWT Authentication (Register/Login)
* 🧾 Create background jobs
* ⚙️ Asynchronous job processing (simulated delay 5–10 sec)
* 📊 Job status tracking (pending → in_progress → completed)
* 🗄️ SQLite database integration
* 📖 Swagger UI documentation (`/docs`)
* 📬 Postman collection support

---

## 🏗️ Project Structure

```
app/
│── main.py
│
├── core/
│   └── security.py
│   └── config.py
│
├── db/
│   └── database.py
│
├── models/
│   └── job.py
│   └── user.py
│
├── routers/
│   ├── auth.py
│   └── job.py
│
├── schemas/
│   ├── job.py
│   └── user.py
```

---

## ⚙️ Tech Stack

* FastAPI
* SQLite (SQLAlchemy)
* Python-JOSE (JWT)
* Passlib (bcrypt)
* Uvicorn

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sasichintada/fastapi-job-system.git
cd fastapi-job-system
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

#### Windows:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Access

Once running, open:

* Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 Authentication Flow

### 1. Register User

```
POST /auth/register
```

### 2. Login User

```
POST /auth/login
```

Response:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

### 3. Authorize in Swagger

Click **Authorize** and paste:

```
Bearer <your_token>
```

---

## 🧾 Job APIs

### Create Job

```
POST /jobs/
```

Example:

```json
{
  "task_name": "process data"
}
```

---

### Get All Jobs

```
GET /jobs/
```

---

### Get Job by ID

```
GET /jobs/{job_id}
```

---

## 🔄 Job Lifecycle

| Status      | Description    |
| ----------- | -------------- |
| pending     | Job created    |
| in_progress | Job is running |
| completed   | Job finished   |

---

## ⚡ How Background Processing Works

* Job is created with `pending` status
* System processes job in background
* Simulates delay (5–10 seconds)
* Updates status to `in_progress`
* Finally marks as `completed`

---

## 🧪 Testing

Use:

* Swagger UI (`/docs`)
* Postman Collection

---

## 📌 Example Workflow

1. Register user
2. Login and get token
3. Create job
4. Check job status
5. Wait 5–10 seconds
6. Job becomes `completed`

---

## 👨‍💻 Author

**Sasank Kumari Chintada**
* GitHub: [@sasichintada](https://github.com/sasichintada)

---

