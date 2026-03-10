# 🤖 Job Market Research Agent

An autonomous **multi-agent AI pipeline** built with **CrewAI + Llama 3.3 (via Groq)** 
that researches live AI/ML job openings in India, scores them against a candidate 
profile, and generates a prioritized application report — fully automated, end to end.

## 🏗️ Architecture
```
[Researcher Agent] → [Analyst Agent] → [Writer Agent]
       ↓                   ↓                  ↓
  Web Search          Skill Matching     Markdown Report
  (SerperDev)         & Gap Analysis     (job_report_output.md)
```

## 🤖 Agents

- **AI/ML Job Market Researcher** — Searches the web for live fresher 
  AI/ML/Gen AI roles in India using SerperDev
- **Career Profile Analyst** — Scores each job 1-10 against candidate 
  skills, flags gaps
- **Career Report Writer** — Produces a clean, prioritized markdown 
  report with interview prep tips

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| CrewAI | Multi-agent orchestration framework |
| LangGraph | Agent workflow management |
| Llama 3.3 70B (Groq) | Free, fast LLM backbone |
| SerperDev | Real-time web search for agents |
| LiteLLM | LLM provider abstraction layer |
| Python 3.11 | Runtime |

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Ayan113/job-market-research-agent.git
cd job-market-research-agent
```

### 2. Create virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install litellm
```

### 4. Set up API keys
```bash
cp .env.example .env
# Add your keys to .env
```

Get free keys at:
- **Groq** (LLM): https://console.groq.com
- **Serper** (web search): https://serper.dev

### 5. Run the agent
```bash
python -m job_market_agent.main
```

The report is saved to `job_report_output.md` ✅

## 📸 Sample Output
```
🚀 Launching Job Market Research Agent...

[Researcher Agent] → Searching for top AI/ML roles in India...
[Analyst Agent]    → Scoring 10 jobs against candidate profile...
[Writer Agent]     → Generating prioritized report...

✅ Report saved to job_report_output.md
```

## 📄 Sample Report Output

See [job_report_output.md](./job_report_output.md) for a real execution output.

## 🔑 Environment Variables

Create a `.env` file with:
```env
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key
OPENAI_API_KEY=dummy-not-used
```

## 🧠 Key Concepts Demonstrated

- Multi-agent collaboration with role specialization
- Sequential task pipeline (Research → Analysis → Writing)
- Real-time web search tool integration
- LLM-powered structured report generation
- Environment-based API key management

## 📁 Project Structure
```
job-market-research-agent/
├── job_market_agent/
│   ├── __init__.py
│   ├── agents.py      # Agent definitions
│   ├── tasks.py       # Task definitions  
│   └── main.py        # Entry point
├── job_report_output.md  # Sample output
├── requirements.txt
├── .env.example
└── README.md
```

## 👤 Author

**Ayan Chatterjee** — 2025 CSE Graduate | Gen AI Engineer | National Hackathon Winner  
[LinkedIn](https://www.linkedin.com/in/ayanc1318/) | [Portfolio](https://ayan-portfolio-six.vercel.app/)