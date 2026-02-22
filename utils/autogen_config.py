import autogen
from typing import Dict, Any

def get_ollama_config(
    model: str = "qwen2.5-coder:7b",
    temperature: float = 0.7,
    base_url: str = "http://localhost:11434/v1"
) -> Dict[str, Any]:
    """
    Generate AutoGen config for Ollama backend.
    
    AutoGen expects OpenAI-compatible API, which Ollama provides.
    """
    return {
        "config_list": [{
            "model": model,
            "base_url": base_url,
            "api_key": "ollama",  # Ollama doesn't need real key, but AutoGen requires this field
            "api_type": "openai"  # Ollama is OpenAI API compatible
        }],
        "temperature": temperature,
        "timeout": 300,
    }

# Model presets for different agent types
CODE_MODEL_CONFIG = get_ollama_config(
    model="qwen2.5-coder:7b",
    temperature=0.2  # Low temperature for deterministic code
)

PLANNING_MODEL_CONFIG = get_ollama_config(
    model="qwen2.5-coder:7b",
    temperature=0.7  # Higher temperature for creative planning
)

REVIEW_MODEL_CONFIG = get_ollama_config(
    model="qwen2.5-coder:7b",
    temperature=0.3  # Medium temperature for analytical review
)