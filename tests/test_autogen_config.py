# test_autogen_ollama.py
import autogen 
from utils.autogen_config import CODE_MODEL_CONFIG

# Create a simple assistant agent
assistant = autogen.AssistantAgent(
    name="TestAssistant",
    llm_config=CODE_MODEL_CONFIG,
    system_message="You are a helpful coding assistant."
)

# Create a user proxy (represents the human)
user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Fully automated for testing
	max_consecutive_auto_reply=0,
    code_execution_config=False
)

# Test interaction
user_proxy.initiate_chat(
    assistant,
    message="Write a Python function that returns 'Hello World'"
)