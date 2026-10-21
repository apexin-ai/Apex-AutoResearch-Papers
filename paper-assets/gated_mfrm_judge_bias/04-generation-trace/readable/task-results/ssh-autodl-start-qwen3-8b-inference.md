# ssh autodl start qwen3 8b inference

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_start_qwen3_8b_inference_20260522T104113_result.json`
- **Structured JSON:** [`6af966caf0f1ad930be4.json`](../../sessions/6a/6af966caf0f1ad930be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实际情况与预期不符：**

1. **Qwen3-8B 不存在** — `/root/autodl-tmp/models/Qwen/Qwen3-8B/` 路径不存在，HF cache 中也没有
2. **gemma-2-9b-it 没有在下载** — 没有相关进程
3. **唯一在下载的模型** 是 Mistral-Large-Instruct-2411-AWQ (PID 179635，从 11:32 开始，已运行 ~7.5 小时)

**服务器当前状态：**
- 已有模型：Llama-3.3-70B-AWQ, Qwen2.5-72B-AWQ, Mistral-Large-2407-AWQ
- 4 GPU 全被占用：
  - GPU 0: exp009 (74GB used, ~24GB free)
  - GPU 1: Mistral vLLM server (port 8003)
  - GPU 2: Llama vLLM server (port 8001)  
  - GPU 3: Qwen2.5-72B vLLM server (port 8002)
- `gen-vllm` session 正在跑 `generate_vllm_online.py --all`（Llama 已完成，Qwen2.5-72B 接近完成，Mistral 很慢）
- 9 个 judge tmux session 也在运行

**需要确认：**
- 是否要先下载 Qwen3-8B 再推理？（BF16 约 16GB，可以塞进 GPU 0 剩余的 24GB）
- 还是你说的是 **另一台服务器** (autodl-8gpu) 而不是 rtx6000-4x？你在消息开头提到的是 "SSH 到 autodl-8gpu 服务器"。

---
