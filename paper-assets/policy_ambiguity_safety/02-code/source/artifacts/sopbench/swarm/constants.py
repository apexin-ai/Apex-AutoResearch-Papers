# OpenAI model names
OPENAI_MODELS = [
    # GPT-5 variants
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    
    # GPT-4 variants
    "gpt-4o", # -> gpt-4o-2024-08-06
    "gpt-4o-2024-11-20",
    
    # GPT-4 Mini variants 
    "gpt-4o-mini", # -> gpt-4o-mini-2024-07-18
    
    # o1
    "o1", # -> o1-2024-12-17
    
    # o3-mini
    "o3-mini", # -> o3-mini-2025-01-31
    
    # o3
    "o3", "o3-low", "o3-medium", "o3-high", 
    
    # o3 mini
    "o3-mini", "o3-mini-low", "o3-mini-medium", "o3-mini-high",
    
    # o4 mini
    "o4-mini", "o4-mini-low", "o4-mini-medium", "o4-mini-high",
    
    # gpt-4.1
    "gpt-4.1-mini", "gpt-4.1",

    # gpt-5.4
    "gpt-5.4",
]

# Gemini models
GEMINI_MODELS = [
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    # gemini 2.0
    "gemini-2.0-flash-001",
    "gemini-2.0-flash",
    "gemini-2.0-flash-thinking-exp",
    "gemini-2.5-flash",
    "gemini-2.5-pro"
]

# Claude models
CLAUDE_MODELS = [
    "claude-3-5-sonnet-20241022",
    "claude-3-5-haiku-20241022",
    "claude-3-7-sonnet-20250219", 
    "claude-3-7-sonnet-20250219-thinking",
    "claude-sonnet-4-20250514",
]

# Fireworks models
FIREWORKS_MODELS = {
    "llama3.1-70b-it-fireworks": "accounts/fireworks/models/llama-v3p1-70b-instruct", # 0.9/M
    "qwen2.5-72b-it-fireworks": "accounts/fireworks/models/qwen2p5-72b-instruct", # 0.9/M
    "deepseek-v3": "accounts/fireworks/models/deepseek-v3", # 0.9/M
    "deepseek-r1": "accounts/fireworks/models/deepseek-r1", # 3.0/M
}

# 3B-32B Models
OSS_MODELS = {
    "llama3.3-70b-instruct": "meta-llama/Llama-3.3-70B-Instruct",
    "llama3.1-70b-instruct": "meta-llama/Llama-3.1-70B-Instruct",
    "qwen2.5-72b-instruct": "Qwen/Qwen2.5-72B-Instruct",
    "qwen2.5-3b-instruct": "Qwen/Qwen2.5-3B-Instruct",
    "qwen2.5-7b-instruct": "Qwen/Qwen2.5-7B-Instruct",
    "qwen2.5-14b-instruct": "Qwen/Qwen2.5-14B-Instruct",
    "qwen2.5-32b-instruct": "Qwen/Qwen2.5-32B-Instruct",
    "llama3.1-8b-instruct": "meta-llama/Llama-3.1-8B-Instruct",
    "llama3.2-3b-instruct": "meta-llama/Llama-3.2-3B-Instruct",
}

# Available Models
AVAILABLE_MODELS = {
    "vllm": [
        "qwen2.5-3b-instruct",
        "qwen2.5-7b-instruct",
        "qwen2.5-14b-instruct",
        "qwen2.5-32b-instruct",
        "llama3.1-8b-instruct",
        "llama3.2-3b-instruct",
    ],
    "fireworks": [
        "llama3.1-405b-instruct",
        "llama3.1-70b-instruct",
        "llama3.3-70b-instruct",
        "qwen2.5-72b-instruct",
        "mistral-8x22b-instruct",
        "qwen2.5-coder-32b-instruct",
        "deepseek-v3",
        "deepseek-r1",
    ],
    "gemini": [
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-2.0-flash-001",
        "gemini-2.0-flash",
        "gemini-2.0-flash-thinking-exp",
    ],
    "claude": [
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-7-sonnet-20250219", 
        "claude-3-7-sonnet-20250219-thinking",
    ],
    "openai": [
        "gpt-4o",
        "gpt-4o-2024-11-20",
        "gpt-4o-mini",
        "o1",
        "o3-mini",
        "gpt-4.1-mini",
        "gpt-4.1",
        "gpt-5.4",
    ]
}

# Model Class That Supports Function Calling
# Fireworks models: https://docs.fireworks.ai/guides/function-calling
FUNCTION_CALLING_MODELS = {
    "vllm": [],
    "fireworks": [
        "llama3.1-70b-it-fireworks",
        "qwen2.5-72b-it-fireworks",
    ],
    "gemini": [
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-2.0-flash-001",
        "gemini-2.0-flash",
        "gemini-2.0-flash-thinking-exp",
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.5-pro-preview-03-25",
        "gemini-2.5-flash-preview-04-17",
    ],
    "claude": [
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-7-sonnet-20250219", 
        "claude-3-7-sonnet-20250219-thinking",
        "claude-opus-4-20250514",
        "claude-sonnet-4-20250514",
        "claude-opus-4-20250514",
    ],
    "openai": [
        "gpt-5",
        "gpt-5-mini",
        "gpt-5-nano",
        "gpt-4o",
        "gpt-4o-2024-11-20",
        "gpt-4o-mini",
        "o1",
        "o3-mini",
        "o3", "o3-low", "o3-medium", "o3-high", 
        "o3-mini", "o3-mini-low", "o3-mini-medium", "o3-mini-high",
        "o4-mini", "o4-mini-low", "o4-mini-medium", "o4-mini-high",
        "gpt-4.1-mini",
        "gpt-4.1",
        "gpt-5.4",
    ]
}