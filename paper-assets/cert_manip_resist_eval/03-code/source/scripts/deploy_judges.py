#!/usr/bin/env python3
# Deploy 4 vLLM judge model servers, each bound to one GPU.
# Usage: python scripts/deploy_judges.py [--model_dir /path/to/models]

import argparse
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import MODEL_REGISTRY, VLLM_GPU_MEMORY_UTILIZATION, VLLM_MAX_MODEL_LEN


def deploy_openai_api(model_id: str, model_path: str, gpu_id: int, port: int) -> subprocess.Popen:
    """Launch a vLLM OpenAI-compatible API server for one model."""
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", model_path,
        "--served-model-name", model_id,
        "--port", str(port),
        "--tensor-parallel-size", "1",
        "--gpu-memory-utilization", str(VLLM_GPU_MEMORY_UTILIZATION),
        "--max-model-len", str(VLLM_MAX_MODEL_LEN),
        "--quantization", "awq",
        "--trust-remote-code",
    ]
    env = {"CUDA_VISIBLE_DEVICES": str(gpu_id)}
    import os
    full_env = {**os.environ, **env}

    print(f"[deploy] Starting {model_id} on GPU {gpu_id}, port {port}")
    proc = subprocess.Popen(cmd, env=full_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc


def main():
    parser = argparse.ArgumentParser(description="Deploy vLLM judge servers")
    parser.add_argument("--model_dir", type=str, default=None, help="Override model directory prefix")
    parser.add_argument("--base_port", type=int, default=8000, help="Base port (incremented per model)")
    args = parser.parse_args()

    processes = []
    for i, (model_id, (model_path, gpu_id, family)) in enumerate(MODEL_REGISTRY.items()):
        if args.model_dir:
            model_name = Path(model_path).name
            model_path = str(Path(args.model_dir) / model_name)

        port = args.base_port + i
        proc = deploy_openai_api(model_id, model_path, gpu_id, port)
        processes.append((model_id, proc, port))
        time.sleep(2)

    print(f"\n[deploy] {len(processes)} servers launched:")
    for model_id, proc, port in processes:
        print(f"  {model_id}: PID={proc.pid}, port={port}")

    print("\nPress Ctrl+C to stop all servers.")
    try:
        while True:
            time.sleep(10)
            for model_id, proc, port in processes:
                if proc.poll() is not None:
                    print(f"[deploy] WARNING: {model_id} (port {port}) exited with code {proc.returncode}")
    except KeyboardInterrupt:
        print("\n[deploy] Shutting down...")
        for model_id, proc, port in processes:
            proc.terminate()
        for _, proc, _ in processes:
            proc.wait(timeout=10)


if __name__ == "__main__":
    main()
