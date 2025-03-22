# 💼 Change Management AI Assistant

An AI-powered assistant built to guide organizations through **digital transformation** using proven change management frameworks. Created by **Thomas Thi, Siva, Ethan, and Matthias** for the **IEEE Hackathon 2025**.

This project combines a **FastAPI** backend, **Groq-powered inference engine**, and a lightweight **HTML/CSS/JavaScript** frontend for a seamless AI-driven advisory experience.

---

## 🚀 Features

- 💬 **Chat Interface** – Web-based UI for real-time interaction with the AI assistant  
- 🧠 **Change Management Expertise** – Framework-aware insights using **ADKAR**, **Lewin**, **Kotter**, **McKinsey 7-S**, and **Nudge Theory**  
- 📚 **Knowledge Base** – Embedded with FAQs, case studies, past campaign insights, and framework references  
- 📝 **Feedback Logging** – Captures and stores user feedback in a `feedback.log` file  
- 🐳 **Dockerized Deployment** – Easily containerize and run the application anywhere  

---

## 📁 Project Structure
├── backend/ # FastAPI backend │ └── main.py # API routes and server logic ├── inference.py # AI inference with embedded knowledge base ├── index.html # Frontend chat interface ├── Dockerfile # Docker configuration ├── requirements.txt # Python dependencies ├── feedback.log # Runtime feedback storage └── README.md # Project documentation


---

## ⚙️ Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)
- Groq API Key ([Get one here](https://groq.com))
- Git

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/change-management-ai-assistant.git
cd change-management-ai-assistant
```
### 2. Install Virtual Environment and Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configure your environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 4. Start Backend Server
```bash
uvicorn backend.main:app --host 127.0.0.1 --port 8000

```
### 5. Start FrontEnd Server
```bash
python -m http.server 8080 --directory .

```
##💡 Usage
Open your browser and navigate to http://localhost:8080. Type a message into the chatbox — for example:

"Recommend actions for a new CRM system rollout"

The AI will respond with suggestions grounded in popular change management models. You can also submit feedback to improve the assistant via the backend /api/feedback endpoint (frontend integration coming soon).

##🧪 Example Queries
"What is change management?"

"Employees are resisting the AI tools rollout."

"Compare Lewin and ADKAR for HR restructuring."

"How to apply Kotter's 8 steps in a finance department merger?"
