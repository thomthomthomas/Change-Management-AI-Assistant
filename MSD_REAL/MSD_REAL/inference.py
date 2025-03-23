from groq import Groq
import os
import requests
import time
from threading import Thread
import sys

# Initialize Groq client 
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# News API configuration
NEWS_API_KEY = "8cd6e955c5e4437e929e65e7526dba3a"  
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_QUERY = "tech trends OR market conditions in change management digital transformation"
NEWS_REFRESH_INTERVAL = 30 * 60  # Refresh every 30 minutes (in seconds)

# Cache for news data
news_cache = []

# Static Knowledge Base (with a placeholder for dynamic updates)
KNOWLEDGE_BASE = {
    "frameworks": {
        "ADKAR": {
            "description": "ADKAR is a goal-oriented change management model with five stages: Awareness, Desire, Knowledge, Ability, Reinforcement.",
            "steps": [
                "Awareness: Communicate the need for change to employees.",
                "Desire: Motivate and encourage participation in the change.",
                "Knowledge: Provide training and information on how to implement the change.",
                "Ability: Support practical application through coaching and practice.",
                "Reinforcement: Sustain the change with feedback and recognition."
            ]
        },
        "Lewin": {
            "description": "Lewin's Change Management Model has three stages: Unfreeze, Change, Refreeze.",
            "steps": [
                "Unfreeze: Prepare the organization by breaking down the existing status quo.",
                "Change: Implement the new processes or systems.",
                "Refreeze: Solidify the changes by establishing new norms and stability."
            ]
        },
        "Kotter": {
            "description": "Kotter's 8-Step Model outlines how to lead organizational change through a sequence of steps.",
            "steps": [
                "Create a sense of urgency.",
                "Build a guiding coalition.",
                "Form a strategic vision and initiatives.",
                "Enlist a volunteer army.",
                "Enable action by removing barriers.",
                "Generate short-term wins.",
                "Sustain acceleration.",
                "Institute change."
            ]
        },
        "McKinsey": {
            "description": "The McKinsey 7S Framework focuses on aligning seven key internal elements to ensure effective change.",
            "steps": [
                "Align Strategy, Structure, Systems, Shared Values, Style, Staff, and Skills.",
                "Assess interdependencies among elements.",
                "Identify gaps and develop alignment strategies."
            ]
        },
        "Nudge": {
            "description": "Nudge Theory emphasizes influencing behavior subtly by changing the environment or presentation of choices.",
            "steps": [
                "Identify behavioral drivers.",
                "Design nudges (e.g., defaults, social norms).",
                "Implement changes with minimal resistance.",
                "Measure and adapt based on feedback."
            ]
        }
    },
    "faqs": [ 
        {"q": "What is change management?", "a": "Change management is a structured approach to transitioning individuals, teams, and organizations from a current state to a desired future state, ensuring successful adoption of changes."},
        {"q": "How does the ADKAR model work?", "a": "The ADKAR model focuses on individual change through five stages: Awareness of the need for change, Desire to participate, Knowledge of how to change, Ability to implement the change, and Reinforcement to sustain it."},
        {"q": "What are common challenges in change management?", "a": "Common challenges include resistance to change, lack of communication, insufficient training, and failure to sustain changes over time."},
        {"q": "How does Lewin's model work?", "a": "Lewin's change model is a simple yet powerful framework for managing organizational change, broken down into 3 key stages: Unfreeze, Change and Refreeze. Lewin’s model emphasizes a systematic approach to change, involving preparation, implementation, and stabilization, ensuring that the new practices are lasting."},
        {"q": "Why is change management important?", "a": "Change management is crucial because it helps organizations implement change smoothly and efficiently. It reduces resistance, minimizes disruptions, ensures employee engagement, and leads to successful outcomes such as increased productivity, enhanced performance, and long-term sustainability of the change."},
        {"q": "How can resistance to change be managed?", "a": "Resistance can be managed by communicating reasons for change clearly, involving employees early and gathering feedback,recognising and addressing concerns to build trust and using change champions to advocate for the change."},
        {"q": "How can communication impact change management?", "a": "Effective communication is essential to explain the change. It helps to reduce uncertainty, manage expectations, and address concerns. Consistent, clear, and open communication builds trust and encourages employee buy-in."},
        {"q": "How do I ensure that change is sustainable?", "a": "Reinforce new behaviors and processes through continuous training and Regularly assess the impact of the change and make adjustments as needed."},
        {"q": "What is a change champion, and why are they important?", "a": "A change champion is an individual or group who advocates for the change, influences others, and leads by example. They are important because they help build momentum, address resistance, and maintain enthusiasm for the change process."}    
    ],
    "past_campaigns": [ 
        {"id": 1, "title": "CRM System Rollout 2023", "description": "Implemented a new CRM system across the sales team.", "actions": ["Conducted town hall meetings to build awareness.", "Offered incentives to encourage adoption.", "Provided two weeks of training sessions.", "Set up a helpdesk for ongoing support."], "outcome": "80% adoption rate within 3 months, improved sales tracking.", "recommendations": "Increase training duration for complex systems."},
        {"id": 2, "title": "Remote Work Transition 2020", "description": "Shifted to a fully remote work environment during the pandemic.", "actions": ["Sent weekly updates to communicate the need for remote work.", "Provided laptops and software access to all employees.", "Hosted virtual workshops on remote collaboration tools."], "outcome": "90% employee satisfaction, but initial resistance due to tech issues.", "recommendations": "Ensure IT infrastructure is robust before rollout."}
        
    ],
    "emotions": {
        "resistance": "Acknowledge concerns, provide clear benefits of the change, and involve employees in the planning process to increase buy-in.",
        "trust": "Be transparent with communication, maintain consistency in messaging, and show empathy to build trust.",
        "resilience": "Offer support resources like counseling, celebrate small wins, and provide clear timelines to reduce uncertainty.",
        "optimism": "Highlight success stories, share positive outcomes, and engage employees with a vision of the future."
    },
    "industry_trends": [
        "Increased adoption of AI tools for change management, with 60% of organizations using AI by 2024 (Source: Gartner).",
        "Focus on employee upskilling to keep pace with digital transformation, especially in tech-driven industries."
    ],
    "what_if_scenarios": [
        {"scenario": "What if we apply Lewin's model instead of ADKAR?", "analysis": "Lewin's model focuses on organizational-level change with three stages (Unfreeze, Change, Refreeze), making it simpler for large-scale structural changes. ADKAR, however, is more individual-focused, better for ensuring employee adoption. Lewin's might miss individual barriers, while ADKAR might be too granular for quick, top-down changes."}
    ],
    "tech_trends": [
        "AI-driven analytics for predicting change resistance (e.g., sentiment analysis).",
        "Virtual reality training programs for immersive learning experiences."
    ],
    "benchmarks": [
        "Adoption Rate: Successful change initiatives typically achieve 70-90% adoption within 6 months (Source: Prosci).",
        "Employee Satisfaction: Post-change satisfaction should be above 75% to indicate effective management (Source: McKinsey).",
        "Operational efficiency: A common benchmark in IT services is 10-20% improvement post-implementation (Source: Whatfix).",
        "Sales Growth: 5%-15% increase in sales or revenue within the first 6-12 months post-change (Source: Whatfix).",
        "Customer Experience: At least 80%-90% customer satisfaction with new services or processes (Source: Whatfix).",
        "Student Performance:  5%-15% improvement in student performance or engagement after implementing new learning tools or platforms (Source: Whatfix).",
        "Manufacturing Efficiency: 10%-20% improvement in manufacturing output or cost reduction within 6-12 months (Source: Whatfix)."
    ],
    "case_studies": [ 
        {"industry": "Healthcare", "description": "A hospital implemented an electronic health record (EHR) system.", "challenge": "High resistance from staff due to unfamiliarity.", "solution": "Used ADKAR: Built awareness through meetings, provided extensive training, and reinforced with regular feedback.", "outcome": "85% adoption within 4 months, improved patient record accuracy."},
        {"industry": "Retail", "description": "A retail chain adopted a new inventory management system across 50 stores.", "challenge": "Geographic diversity and varying tech skills.", "solution": "Applied Lewin's model: Unfroze by communicating benefits, changed by rolling out in phases, refroze with new SOPs.", "outcome": "Reduced stockouts by 30%, but initial rollout was slow in rural stores."},
        {"industry": "Technology", "description": "General Electric wanted to shift from a traditional manufacturing-focused company to a more data-driven, digitally integrated organization.", "challenge": "Required a shift in organizational mindset and significant change in daily workflows.", "solution": "Applied Lewin's Model by highlighting the need for the company to adapt to the changing market conditions and tech advancements, while ensuring digital tools were enbedded in the company's culture and everyday processes.", "outcome": "GE managed to integrate digital technologies across its business, driving efficiency, reducing costs, and enhancing productivity."},
        {"industry": "F&B", "description": "Coca-Cola decided to overhaul its internal communication systems and processes in order to improve communication and collaboration in its workforce.", "challenge": "Employees were initially resistant to the change as theyy were more accustomed to traditional communication methods.", "solution": "The company emphasized the importance of its new collaboration platform and how it could help improve efficiency, reduce bottlenecks and help employees connect more easily.", "outcome": "Coca-Cola managed to implement the ARKAR change model which led to better internal collaboration and communication across the organisation, with employees beginning to be more comfortable with the new platform making it integral to the company's daily operations."},
        {"industry": "Technology", "description": "Microsoft aimed to transition from its legacy software-based business model to a cloud-first approach.", "challenge": "Invovled major changes towards the company's culture, structure as well as their business model to accommodate the cloud-first strategy.", "solution": "Applied ARKAR framework to not only show how the new businness model would improve the work environment, but also ensure that all employees were given the necessary resources to upskill in cloud technologies.", "outcome": "Microsoft smoothly transitioned into a cloud-first company by fostering awareness, building desire, ensuring knowledge, enhancing ability, and reinforcing the new model."}
    
    ],
    "market_conditions": []  # New dynamic section for news updates
}

conversation_history = []

# Function to fetch and update news data
def fetch_news():
    global news_cache
    while True:
        try:
            params = {
                "q": NEWS_QUERY,
                "sortBy": "relevancy",
                "apiKey": NEWS_API_KEY,
                "language": "en",
                "pageSize": 5  # Limit to 5 articles
            }
            response = requests.get(NEWS_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            news_cache = [
                f"{article['title']}: {article['description'] or 'No description'} (Source: {article['source']['name']})"
                for article in data.get("articles", [])
            ]
            # Update KNOWLEDGE_BASE with news data
            KNOWLEDGE_BASE["market_conditions"] = news_cache
            print("News cache updated and integrated into KNOWLEDGE_BASE:", news_cache)  # Debugging
        except Exception as e:
            print(f"Failed to fetch news: {e}")
            news_cache = ["News unavailable: Could not fetch latest trends."]
            KNOWLEDGE_BASE["market_conditions"] = news_cache
        time.sleep(NEWS_REFRESH_INTERVAL)

# Start news fetching in a background thread
news_thread = Thread(target=fetch_news, daemon=True)
news_thread.start()

# Function to format the knowledge base as a string for the prompt
def format_knowledge_base(kb):
    kb_str = ""
    # Frameworks
    kb_str += "Frameworks:\n"
    for name, details in kb["frameworks"].items():
        kb_str += f"- {name}: {details['description']}\n  Steps: {', '.join(details['steps'])}\n"
    # FAQs
    kb_str += "\nFAQs:\n"
    for faq in kb["faqs"]:
        kb_str += f"- Q: {faq['q']} A: {faq['a']}\n"
    # Past Campaigns
    kb_str += "\nPast Campaigns:\n"
    for campaign in kb["past_campaigns"]:
        kb_str += f"- {campaign['title']}: {campaign['description']} (Outcome: {campaign['outcome']})\n"
    # Emotions
    kb_str += "\nEmotion Strategies:\n"
    for emotion, strategy in kb["emotions"].items():
        kb_str += f"- {emotion.capitalize()}: {strategy}\n"
    # Industry Trends
    kb_str += "\nIndustry Trends:\n"
    for trend in kb["industry_trends"]:
        kb_str += f"- {trend}\n"
    # What-If Scenarios
    kb_str += "\nWhat-If Scenarios:\n"
    for scenario in kb["what_if_scenarios"]:
        kb_str += f"- {scenario['scenario']}: {scenario['analysis']}\n"
    # Tech Trends (static)
    kb_str += "\nStatic Tech Trends:\n"
    for trend in kb["tech_trends"]:
        kb_str += f"- {trend}\n"
    # Market Conditions (dynamic news)
    kb_str += "\nCurrent Market Conditions (from News):\n"
    for condition in kb["market_conditions"]:
        kb_str += f"- {condition}\n"
    # Benchmarks
    kb_str += "\nBenchmarks:\n"
    for benchmark in kb["benchmarks"]:
        kb_str += f"- {benchmark}\n"
    # Case Studies
    kb_str += "\nCase Studies:\n"
    for study in kb["case_studies"]:
        kb_str += f"- {study['industry']}: {study['description']} (Outcome: {study['outcome']})\n"
    return kb_str

def process_news_into_trends(news_cache):
    trends = []
    for article in news_cache:
        # Extract title and source, simplify into a trend statement
        title, rest = article.split(": ", 1)
        source = rest.split("(Source: ")[-1].rstrip(")")
        trend = f"{title} indicates a focus on {title.split()[-1].lower()} (Source: {source})"
        trends.append(trend)
    return trends if trends else ["No recent trends available from news."]

def generate_response(message):
    # Append the new user message to conversation history
    conversation_history.append({"role": "user", "content": message})

    # Format the full knowledge base, including dynamic news
    full_knowledge_base = format_knowledge_base(KNOWLEDGE_BASE)

    # Process news_cache into concise trends
    news_trends = process_news_into_trends(KNOWLEDGE_BASE["market_conditions"])
    print("Debug - Processed News Trends:", news_trends)

    system_prompt = (
        "You are Navi, an AI Assistant specialized in change management, built for the IEEE Hackathon 2025. "
        "Your purpose is to assist organizations in navigating digital transformation using change management frameworks, "
        "driven by the latest industry trends from recent news.\n\n"
        "**Instructions**:\n"
        "- Use conversation history to recall details (e.g., names) and weave them into responses naturally.\n"
        "- For every query, identify the scope (organizational, project, or people-level) and recommend a framework.\n"
        "- Compare at least 2-3 frameworks (ADKAR, Lewin, Kotter, McKinsey, Nudge) and justify your choice. **Base your reasoning directly on the 'Processed News Trends' provided below, as of March 22, 2025.** Summarize these trends at the start of your reasoning and tie them explicitly to your recommendation. Only use static knowledge base data if news trends are unavailable, noting this limitation.\n"
        "- Provide actionable steps based on the chosen framework, referencing past campaigns or case studies if relevant.\n"
        "- Maintain a professional, empathetic tone and request feedback after each response.\n"
        "- When referencing news trends, you may optionally cite the source (e.g., 'Source: Crescendo.ai') for clarity.\n\n"
        "**Processed News Trends (from News API, as of March 22, 2025)**:\n"
        f"{'; '.join(news_trends)}\n\n"
        "**Full Knowledge Base (Static + Dynamic News)**:\n"
        f"{full_knowledge_base}\n\n"
        "**Conversation History**:\n"
        "{history}"
    ).format(
        history="\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation_history])
    )

    try:
        full_messages = [{"role": "system", "content": system_prompt}] + conversation_history
        print(f"Debug: Sending {len(full_messages)} messages to API")
        chat_completion = client.chat.completions.create(
            messages=full_messages,
            model="llama3-70b-8192",
            max_tokens=1000,
            temperature=0.7,
            top_p=0.9
        )
        reply = chat_completion.choices[0].message.content.strip()

        conversation_history.append({"role": "assistant", "content": reply})
        print("\nResponse:\n")
        for line in reply.split('\n'):
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
            print()
        print("\n---\n *Was this helpful? Please provide feedback to improve my responses.*")
        return f"Response:\n\n{reply}\n\n---\n *Was this helpful? Please provide feedback to improve my responses.*"

    except Exception as e:
        print(f"Error calling Groq API: {type(e).__name__}: {str(e)}")
        return "Sorry, I couldn't process your request right now."

# Testing block with updated test messages
if __name__ == "__main__":
    test_messages = [
        "My name is Siva.",
        "What's my name?",
        "Recommend actions for a new CRM system.",
        "Employees are resisting the AI tools rollout.",
        "What is change management?",
        "Based on current market conditions, what is the best framework?"
    ]
    for msg in test_messages:
        print(f"\nInput: {msg}\n")
        response = generate_response(msg)
        print(response)  # Print the returned string as well
        print("\n" + "="*80 + "\n")
