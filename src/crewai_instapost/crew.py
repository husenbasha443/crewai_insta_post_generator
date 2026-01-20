from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CrewaiInstapost():
    """CrewaiInstapost crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'], 
            verbose=True
       )

    @agent
    def caption_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['caption_writer'], 
            verbose=True
        )

    @agent
    def hashtag_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['hashtag_specialist'], 
            verbose=True
        )

    @task
    def content_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_idea_task'], 
        )

    @task
    def caption_taskk(self) -> Task:
        return Task(
            config=self.tasks_config['caption_task'], 
        )

    @task
    def hashtag_task(self) -> Task:
        return Task(
            config=self.tasks_config['hashtag_task'], 
            output_file='blobs/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiInstapost crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            trace=True
        )
