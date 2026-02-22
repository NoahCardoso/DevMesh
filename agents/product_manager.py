# agents/product_manager.py
import autogen
from typing import Dict
from utils.autogen_config import PLANNING_MODEL_CONFIG

class ProductManagerAgent:
    def __init__(self):
        self.agent = autogen.AssistantAgent(
            name="ProductManager",
            llm_config=PLANNING_MODEL_CONFIG,
            system_message=self._get_system_message(),
        )
    
    def _get_system_message(self) -> str:
        return (
            """You are a Product Manager agent in a software development team.

            YOUR ROLE:
            1. Clarify project requirements from user input
            2. Generate detailed user stories in standard format
            3. Specify technical requirements (language, framework, database)
            4. Create a structured requirements document

            OUTPUT FORMAT:
            When providing final requirements, format as:

            PROJECT: [name]
            DESCRIPTION: [brief description]

            USER STORIES:
            - As a [user], I want to [action] so that [benefit]
            - As a [user], I want to [action] so that [benefit]
            ...

            TECHNICAL REQUIREMENTS:
            - Language: [Python/JavaScript/Java]
            - Framework: [Flask/Express/Spring Boot]
            - Database: [SQLite/PostgreSQL]
            - Other: [any other requirements]

            ACCEPTANCE CRITERIA:
            1. [specific measurable criterion]
            2. [specific measurable criterion]
            ...

            Be thorough but concise. If requirements are unclear, make reasonable MVP assumptions."""
                )
    
    def clarify_requirements(self, user_input: str) -> str:
        """
        Main method to generate requirements from user input.
        Uses AutoGen's conversational pattern.
        """
        # Create a temporary user proxy to interact with PM
        user_proxy = autogen.UserProxyAgent(
            name="RequirementsGatherer",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=1,
            code_execution_config=False
        )
        
        # Initiate conversation
        user_proxy.initiate_chat(
            self.agent,
            message=f"""Please analyze this project request and create a detailed requirements document:

                    {user_input}

                    Generate complete requirements following your output format."""
        )
        
        # Extract last message from agent
        return self.agent.last_message()["content"]

# Usage example
if __name__ == "__main__":
    pm = ProductManagerAgent()
    
    requirements = pm.clarify_requirements(
        "Build a REST API for a todo list application"
    )
    
    print(requirements)