import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "dummy-not-used")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

search_tool = SerperDevTool()

researcher = Agent(
    role="AI/ML Job Market Researcher",
    goal="Find the latest AI, ML, and Gen AI job openings in India for 2025 CSE graduates",
    backstory="""You are an expert tech recruiter with deep knowledge of India's 
    AI/ML job market. You find entry-level roles at MNCs, startups, and consulting 
    firms for CSE graduates with Gen AI skills.""",
    tools=[search_tool],
    llm=llm,
    verbose=True
)

analyst = Agent(
    role="Career Profile Analyst",
    goal="Match job requirements against candidate skills and rank opportunities by fit",
    backstory="""You are a senior career coach specializing in AI/ML roles. 
    You analyze job descriptions, score them 1-10 against candidate profiles, 
    and identify skill gaps clearly.""",
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Career Report Writer",
    goal="Produce a clean, actionable job application report with ranked opportunities",
    backstory="""You are a professional technical writer who transforms raw job 
    data and analysis into structured, prioritized action plans for job seekers.""",
    llm=llm,
    verbose=True
)