# 💼 Change Management AI Assistant – IEEE Hackathon 2025

An AI-powered assistant designed to guide organizations through **digital transformation** using industry-recognized change management frameworks and real-time trend analysis.

🚀 Built by **NTU Year 1 CCDS Undergraduates Thomas Thi, Siva, Ethan, and Matthias** for the **IEEE Hackathon 2025**, this solution integrates:

- 🧠 A Groq-powered large language model
- ⚙️ A FastAPI backend
- 🌐 A responsive HTML/CSS/JS frontend
- 📈 Real-time industry and market insights via NewsAPI
- 📥 Feedback loop integration for continuous learning

---

## 🚀 Features

- 💬 **Web-Based Chat Interface**: Interact with "Navi", your friendly AI change management advisor  
- 🧠 **Framework Intelligence**: Recommendations based on ADKAR, Lewin, Kotter, McKinsey 7S, and Nudge Theory  
- 📚 **Knowledge Base**: Includes frameworks, FAQs, case studies, emotional strategies, past campaigns, benchmarks, and more  
- 📰 **Live Market Insights**: Fetches and analyzes news articles to reflect current tech and industry trends  
- ❤️ **Emotion-Aware Advice**: Tailored suggestions for handling resistance, trust, resilience, and optimism  
- 🔁 **Feedback Logging**: Records timestamped user feedback for future assistant improvements  
- 🐳 **Docker-Ready**: Deployable with a single command using Docker  

---

## 📁 Project Structure
├── backend/ # FastAPI backend ├── inference.py # AI inference with embedded knowledge base ├── index.html # Frontend chat interface ├── Dockerfile # Docker configuration ├── requirements.txt # Python dependencies ├── feedback.log # Runtime feedback storage └── README.md # Project documentation


---

## ⚙️ Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)
- Groq API Key ([groq.com](https://groq.com))
- NewsAPI Key ([newsapi.org](https://newsapi.org))
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
export GROQ_API_KEY="your-groq-api-key"
export NEWS_API_KEY="your-newsapi-key"

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

"Based on the latest market conditions, which change management framework should I use for a new AI-driven project"

"How to apply Kotter's 8 steps in a finance department merger?"

##📝 License
This project is licensed under the MIT License.


