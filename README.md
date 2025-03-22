# Change Management AI Assistant

This project is an AI-powered assistant designed to help organizations navigate digital transformation using change management frameworks. Done by Thomas Thi , Siva , Ethan and Matthias. Built for the **IEEE Hackathon 2025**, it integrates a FastAPI backend, a Grok-powered inference engine (via the Groq API), and a simple HTML/CSS/JavaScript frontend.

## Features
- **Chat Interface**: Users can interact with the AI assistant via a web-based chat UI.
- **Change Management Expertise**: Provides recommendations based on frameworks like ADKAR, Lewin, Kotter, McKinsey, and Nudge Theory.
- **Feedback Logging**: Stores user feedback in a `feedback.log` file.
- **Knowledge Base**: Embedded with change management frameworks, FAQs, past campaigns, case studies, and more.
- **Dockerized Deployment**: Includes a Dockerfile for easy containerization.

## Project Structure
├── backend/                # FastAPI backend code
│   └── main.py             # Main FastAPI application
├── inference.py            # Grok inference logic with embedded knowledge base
├── index.html              # Frontend chat interface
├── Dockerfile              # Docker configuration for backend
├── requirements.txt        # Python dependencies
├── feedback.log            # Feedback storage (generated at runtime)
└── README.md               # Project documentation

## Prerequisites
- Python 3.9+
- Docker (optional, for containerized deployment)
- Groq API Key (sign up at [Groq](https://groq.com) to obtain one)
- Git

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/<your-username>/change-management-ai-assistant.git
cd change-management-ai-assistant
### 2. Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
### 3. Configure Environment
export GROQ_API_KEY="your-groq-api-key"  # On Windows: set GROQ_API_KEY=your-groq-api-key
### 4. Run the back-end
uvicorn backend.main:app --host 127.0.0.1 --port 8000
### 5. Run the front-end
python -m http.server 8080 --directory .

###Usage
Type a message in the chat interface (e.g., "Recommend actions for a new CRM system").
The AI will respond with framework-based recommendations and request feedback.
Feedback can be submitted via the /api/feedback endpoint (not yet integrated into the frontend).
###Example Queries
"What is change management?"
"Employees are resisting the AI tools rollout."
"Compare Lewin and ADKAR for HR restructuring."


License
This project is licensed under the MIT License.
