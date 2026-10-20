"""HF repo ID → local path mapping for gated or pre-downloaded models.

If a model's repo ID appears here, the local path is used instead of
downloading from HuggingFace. Models not in this map fall back to the
repo ID (requires network access or HF token for gated models).
"""

MODEL_PATH_MAP: dict[str, str] = {
    "meta-llama/Llama-3.1-8B-Instruct": (
        "meta-llama/Llama-3.1-8B-Instruct"
        "Meta-Llama-3___1-8B-Instruct"
    ),
    "google/gemma-2-9b-it": (
        "google/gemma-2-9b-it"
    ),
    "mistralai/Mistral-7B-Instruct-v0.3": (
        "mistralai/Mistral-7B-Instruct-v0.3"
    ),
    "Qwen/Qwen3-8B": (
        "Qwen/Qwen3-8B"
    ),
    "01-ai/Yi-1.5-9B-Chat": (
        "01-ai/Yi-1.5-9B-Chat"
    ),
    "allenai/OLMo-2-1124-7B-Instruct": (
        "allenai/OLMo-2-1124-7B-Instruct"
    ),
    "internlm/internlm2_5-7b-chat": (
        "internlm/internlm2_5-7b-chat"
    ),
    "deepseek-ai/deepseek-llm-7b-chat": (
        "deepseek-ai/deepseek-llm-7b-chat"
    ),
    "Qwen/Qwen2.5-3B-Instruct": (
        "Qwen/Qwen2.5-3B-Instruct"
    ),
    "Qwen/Qwen2.5-7B-Instruct": (
        "Qwen/Qwen2.5-7B-Instruct"
    ),
    "Qwen/Qwen2.5-72B-Instruct": (
        "Qwen/Qwen2.5-72B-Instruct"
    ),
}

MODEL_DISPLAY_NAMES: dict[str, str] = {
    # HF repo IDs
    "meta-llama/Llama-3.1-8B-Instruct": "Llama-3.1-8B",
    "google/gemma-2-9b-it": "Gemma-2-9B",
    "mistralai/Mistral-7B-Instruct-v0.3": "Mistral-7B-v0.3",
    "Qwen/Qwen3-8B": "Qwen3-8B",
    # Directory names (from local paths)
    "Meta-Llama-3___1-8B-Instruct": "Llama-3.1-8B",
    "gemma-2-9b-it": "Gemma-2-9B",
    "Mistral-7B-Instruct-v0___3": "Mistral-7B-v0.3",
    "Qwen3-8B": "Qwen3-8B",
    # Lowercase variants (from cross_model CSV)
    "llama-3.1-8b-instruct": "Llama-3.1-8B",
    "mistral-7b-instruct-v0.3": "Mistral-7B-v0.3",
    "qwen3-8b": "Qwen3-8B",
    # Full local paths
    "meta-llama/Llama-3.1-8B-Instruct": "Llama-3.1-8B",
    "google/gemma-2-9b-it": "Gemma-2-9B",
    "mistralai/Mistral-7B-Instruct-v0.3": "Mistral-7B-v0.3",
    "Qwen/Qwen3-8B": "Qwen3-8B",
    # LLM-Research prefixed directory names
    "LLM-Research/Meta-Llama-3___1-8B-Instruct": "Llama-3.1-8B",
    "LLM-Research/gemma-2-9b-it": "Gemma-2-9B",
    "LLM-Research/Mistral-7B-Instruct-v0___3": "Mistral-7B-v0.3",
    # Yi-1.5
    "01-ai/Yi-1.5-9B-Chat": "Yi-1.5-9B",
    "Yi-1___5-9B-Chat": "Yi-1.5-9B",
    "01ai/Yi-1___5-9B-Chat": "Yi-1.5-9B",
    "yi-1.5-9b-chat": "Yi-1.5-9B",
    "01-ai/Yi-1.5-9B-Chat": "Yi-1.5-9B",
    # OLMo-2
    "allenai/OLMo-2-1124-7B-Instruct": "OLMo-2-7B",
    "OLMo-2-1124-7B-Instruct": "OLMo-2-7B",
    "olmo-2-1124-7b-instruct": "OLMo-2-7B",
    "allenai/OLMo-2-1124-7B-Instruct": "OLMo-2-7B",
    # InternLM2.5
    "internlm/internlm2_5-7b-chat": "InternLM2.5-7B",
    "internlm2_5-7b-chat": "InternLM2.5-7B",
    "Shanghai_AI_Laboratory/internlm2_5-7b-chat": "InternLM2.5-7B",
    "internlm2.5-7b-chat": "InternLM2.5-7B",
    "internlm/internlm2_5-7b-chat": "InternLM2.5-7B",
    # DeepSeek
    "deepseek-ai/deepseek-llm-7b-chat": "DeepSeek-7B",
    "deepseek-llm-7b-chat": "DeepSeek-7B",
    "deepseek-ai/deepseek-llm-7b-chat": "DeepSeek-7B",
    # Qwen2.5-3B
    "Qwen/Qwen2.5-3B-Instruct": "Qwen2.5-3B",
    "Qwen2___5-3B-Instruct": "Qwen2.5-3B",
    "qwen2.5-3b-instruct": "Qwen2.5-3B",
    "Qwen/Qwen2.5-3B-Instruct": "Qwen2.5-3B",
    # Qwen2.5-7B
    "Qwen/Qwen2.5-7B-Instruct": "Qwen2.5-7B",
    "Qwen2___5-7B-Instruct": "Qwen2.5-7B",
    "qwen2.5-7b-instruct": "Qwen2.5-7B",
    "Qwen/Qwen2.5-7B-Instruct": "Qwen2.5-7B",
    # Qwen2.5-72B
    "Qwen/Qwen2.5-72B-Instruct": "Qwen2.5-72B",
    "Qwen2___5-72B-Instruct": "Qwen2.5-72B",
    "qwen2.5-72b-instruct": "Qwen2.5-72B",
    "Qwen/Qwen2.5-72B-Instruct": "Qwen2.5-72B",
}


def resolve_model_path(repo_id: str) -> str:
    """Return local path if available, otherwise the original repo ID."""
    return MODEL_PATH_MAP.get(repo_id, repo_id)


def normalize_model_name(name: str) -> str:
    """Map any model name variant to its canonical display name."""
    return MODEL_DISPLAY_NAMES.get(name, name)
