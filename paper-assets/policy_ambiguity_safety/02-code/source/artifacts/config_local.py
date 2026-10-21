"""Configuration for local open-source model inference.

Model registry, generation parameters, and vLLM server defaults.
"""

MODEL_REGISTRY = {
    "Qwen/Qwen3-32B-AWQ": {
        "family": "qwen3",
        "hf_id": "Qwen/Qwen3-32B-AWQ",
        "tool_call_support": "native",
        "vllm_tool_parser": "hermes",
        "quantization": "awq",
        "recommended_gpus": "1xRTX-PRO-6000-48G (~18GB VRAM)",
        "vllm_extra_args": {"quantization": "awq"},
    },
    "Qwen/Qwen3-8B": {
        "family": "qwen3",
        "hf_id": "Qwen/Qwen3-8B",
        "tool_call_support": "native",
        "vllm_tool_parser": "hermes",
        "recommended_gpus": "1xRTX-PRO-6000-48G (~16GB VRAM, bf16)",
        "vllm_extra_args": {},
    },
    "meta-llama/Llama-4-Scout-17B-16E-Instruct-AWQ": {
        "family": "llama4",
        "hf_id": "meta-llama/Llama-4-Scout-17B-16E-Instruct-AWQ",
        "tool_call_support": "native",
        "vllm_tool_parser": "llama3_json",
        "quantization": "awq",
        "recommended_gpus": "1xRTX-PRO-6000-48G (~20GB VRAM)",
        "vllm_extra_args": {"quantization": "awq"},
    },
}

DEFAULT_EXPERIMENT_MODELS = [
    "Qwen/Qwen3-8B",
    "Qwen/Qwen3-32B-AWQ",
]

DEFAULT_GENERATION_PARAMS = {
    "temperature": 0.6,
    "top_p": 0.95,
    "max_tokens": 4096,
}

VLLM_DEFAULT_PORT = 8000
