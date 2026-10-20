"""
跨表征分歧诊断 pipeline 配置。
API 参数、执行设定、路径、数据集配置、计费。
"""

import os
from pathlib import Path

# --- API ---
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/v1")
API_KEY = [REDACTED]"OPENROUTER_API_KEY", "dummy")
MODEL_NAME = os.getenv("MODEL_NAME", "/root/autodl-tmp/models/Qwen3-32B-AWQ")

# --- 计费（USD per token，本地推理默认为 0，OpenRouter 通过环境变量覆盖） ---
PRICE_PER_INPUT_TOKEN = float(os.getenv("PRICE_INPUT", "0"))
PRICE_PER_OUTPUT_TOKEN = float(os.getenv("PRICE_OUTPUT", "0"))

# --- 执行 ---
EXEC_TIMEOUT = 30        # 代码执行超时（秒）
API_MAX_RETRIES = 3
API_RETRY_DELAY = 5      # 重试间隔（秒）
API_TIMEOUT = 120         # API 调用超时（秒）
MAX_REPAIR_ROUNDS = 2

# --- 路径 ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = Path(__file__).resolve().parent
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# --- 数据 ---
FOLIO_DATASET = "yale-nlp/FOLIO"
FOLIO_SPLIT = "validation"
