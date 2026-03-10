from crewai import Task
from job_market_agent.agents import researcher, analyst, writer

task1 = Task(
    description="""Search for the top 10 AI/ML/Gen AI fresher job openings 
    in India right now (March 2026). Focus on: LangChain, RAG, Agentic AI, 
    Python, LLM roles at EY, IBM, Deloitte, Meesho, Flipkart and AI startups. 
    Return: company name, role title, estimated CTC, and apply link.""",
    expected_output="List of 10 jobs with company, role, CTC estimate, apply link",
    agent=researcher
)

task2 = Task(
    description="""Score each job 1-10 for this candidate:
    Skills: Python, LangChain, RAG, Agentic AI, Llama, Mistral, Cohere, Docker, REST APIs, SQL
    Experience: Gen AI Engineer (Arvantis.ai), Full Stack AI (Unified Mentor), Google ML Intern
    Achievements: National Hackathon Winner (Agentic AI), Top 5 National Ideathon
    Education: B.E. CSE VTU 2025, CGPA 8.0
    Flag any skill gaps per role.""",
    expected_output="Ranked job list with fit score and gap analysis per role",
    agent=analyst
)

task3 = Task(
    description="""Write a structured markdown report with:
    1. Top 5 jobs to apply RIGHT NOW (ranked by fit score)
    2. For each: company, role, why it fits, apply link, one interview prep tip
    3. Top 2 skill gaps to close in the next 30 days with free resources""",
    expected_output="Clean markdown report",
    agent=writer
)