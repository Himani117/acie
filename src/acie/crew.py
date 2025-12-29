from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import List


@CrewBase
class Acie():
    """Acie crew"""

    agents_config = "config/agents.yaml"
    tasks_config= "config/tasks.yaml"
    tools = [SerperDevTool(), ScrapeWebsiteTool()]

    @agent
    def client_engagement_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['client_engagement_manager'], # type: ignore[index]
        )

    @agent
    def market_research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_analyst'], # type: ignore[index]
            tools=self.tools
        )

    @agent
    def strategy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_analyst'], # type: ignore[index]
            tools=[SerperDevTool()]
        )

    @agent
    def domain_industry_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_industry_analyst'], # type: ignore[index]
            tools=self.tools
        )

    @agent
    def data_normalization_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_normalization_analyst'], # type: ignore[index]
        )

    @agent
    def meta_quality_auditor(self) -> Agent:
        return Agent(
            config=self.agents_config['meta_quality_auditor'], # type: ignore[index]
        )

   
    @task
    def client_intake(self) -> Task:
        return Task(
            config=self.tasks_config['client_intake'], # type: ignore[index]
        )

    @task
    def baseline_discovery(self) -> Task:
        return Task(
            config=self.tasks_config['baseline_discovery'], # type: ignore[index]
        )
    
    @task
    def product_signal_extraction(self) -> Task:
        return Task(
            config=self.tasks_config['product_signal_extraction'], # type: ignore[index]
        )
    
    @task
    def competitor_identification(self) -> Task:
        return Task(
            config=self.tasks_config['competitor_identification'], # type: ignore[index]
        )

    @task
    def business_model_inference(self) -> Task:
        return Task(
            config=self.tasks_config['business_model_inference'], # type: ignore[index]
        )

    @task
    def assumption_validation(self) -> Task:
        return Task(
            config=self.tasks_config['assumption_validation'], # type: ignore[index]
        )
    
    @task
    def normalization(self) -> Task:
        return Task(
            config=self.tasks_config['normalization'], # type: ignore[index]
        )

    @task
    def benchmarking(self) -> Task:
        return Task(
            config=self.tasks_config['benchmarking'], # type: ignore[index]
        )

    @task
    def insight_synthesis(self) -> Task:
        return Task(
            config=self.tasks_config['insight_synthesis'], # type: ignore[index]
        )

    @task
    def recommendations(self) -> Task:
        return Task(
            config=self.tasks_config['recommendations'], # type: ignore[index]
        )

    @task
    def final_audit_and_reporting(self) -> Task:
        return Task(
            config=self.tasks_config['final_audit_and_reporting'], # type: ignore[index]
            output_dir="output",
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Acie crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
           
        )
