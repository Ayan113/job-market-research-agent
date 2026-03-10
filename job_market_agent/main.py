from crewai import Crew, Process
from job_market_agent.agents import researcher, analyst, writer
from job_market_agent.tasks import task1, task2, task3
from dotenv import load_dotenv

load_dotenv()

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Launching Job Market Research Agent...\n")
    result = crew.kickoff()
    
    print("\n\n========== FINAL REPORT ==========")
    print(result)
    
    with open("job_report_output.md", "w") as f:
        f.write(str(result))
    
    print("\n✅ Report saved to job_report_output.md")