⚡ LinkedIn Post Generator with Agentic AI

An Agentic AI workflow built with LangChain, LangGraph, and Groq LLMs that fetches trending news, summarizes it, reviews/improves content, and generates polished LinkedIn-ready posts — deployed end-to-end with Docker, AWS ECR, EC2, and GitHub Actions CI/CD.



🌟 Features

🔍 News Finder Agent → Fetches trending industry news using Tavily API.

📝 Summarizer Agent → Structures raw content into insights (Headings → Subheadings → Bullets).

✅ Reviewer Agent → Evaluates summaries (tone, engagement, recency).

🔄 Improver Agent → Self-correcting loop, improves summaries based on feedback.

✍️ Generator Agent → Creates LinkedIn posts (hook → insights → CTA + hashtags).

🚀 Deployment Ready → Dockerized, pushed to ECR, deployed on EC2 with GitHub Actions.

![63dd0e38b1b6121af8f71330f702f5b3d9b810d66453bb25500a1eeb](https://github.com/user-attachments/assets/c445c927-8943-403a-b595-1671aaf48003)




🛠️ Tech Stack

LangChain / LangGraph → agent workflow

Groq LLMs → fast reasoning & text generation

Streamlit → web UI for interaction

Docker → containerization

AWS ECR + EC2 → cloud deployment

GitHub Actions → CI/CD pipeline

Python → 3.10+

📂 Project Structure
.
├── app/
│   └── app.py              # Streamlit UI
├── core/
│   ├── clients.py          # LLM + Tavily clients
│   ├── graph.py            # LangGraph workflow definition
│   ├── node.py             # Agents (finder, summarizer, reviewer, etc.)
│   └── schema.py           # State schema + utilities
├── config/
│   └── settings.py         # Environment variables loader
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build config
├── .gitignore              # Ignore secrets & cache
├── .env.example            # Example env file
└── .github/
    └── workflows/
        └── main.yml        # CI/CD pipeline

⚙️ Setup & Run Locally
1. Clone repo
git clone https://github.com/<your-username>/linkedin-agent-app.git
cd linkedin-agent-app

2. Setup environment
conda create -n agentic_ai python=3.11 -y
conda activate agentic_ai
pip install -r requirements.txt

3. Configure .env

Create a .env file (never commit this!):

GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key   # optional

4. Run locally
streamlit run app/app.py

🐳 Docker Usage
Build image
docker build -t linkedin-agent .

Run container
docker run -d -p 8080:8501 --name linkedin-agent \
  -e GROQ_API_KEY=your_groq_key \
  -e TAVILY_API_KEY=your_tavily_key \
  linkedin-agent:latest


Access app → http://localhost:8080

☁️ Deployment (AWS)
1. Push to ECR

Repo URI:

<AWS_ACCOUNT_ID>.dkr.ecr.<region>.amazonaws.com/linkedin-agent


Build & push:

docker build -t linkedin-agent .
docker tag linkedin-agent:latest <ECR_URI>:latest
docker push <ECR_URI>:latest

2. Run on EC2
docker run -d -p 8080:8501 --restart unless-stopped --name linkedin-agent \
  -e GROQ_API_KEY=$GROQ_API_KEY \
  -e TAVILY_API_KEY=$TAVILY_API_KEY \
  <ECR_URI>:latest

3. GitHub Actions CI/CD

Push → GitHub Actions →

Build Docker image → Push to ECR

Deploy latest container on EC2

Workflow: .github/workflows/main.yml

🌐 Access

Once deployed →

http://<EC2-PUBLIC-IP>:8080


(Optional: Use Elastic IP + reverse proxy for stable https:// access.)

📊 Agent Workflow Diagram
graph TD
    A[News Finder Agent] --> B[Summarizer Agent]
    B --> C[Reviewer Agent]
    C -- pass --> D[Generator Agent]
    C -- fail --> E[Improver Agent]
    E --> C

🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

📜 License

MIT License
