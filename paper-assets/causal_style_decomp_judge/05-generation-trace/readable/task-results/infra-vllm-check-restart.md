# infra vllm check restart

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_vllm-check-restart_20260522T231152_result.json`
- **Structured JSON:** [`bf6cf2d0b2c8c061b13c.json`](../../sessions/bf/bf6cf2d0b2c8c061b13c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. vLLM 状态：全部存活

| 端口 | 模型 | GPU | 状态 |
|------|------|-----|------|
| 8000 | Qwen3-32B | GPU 0,1 (89GB/卡) | **正常** |
| 8003 | Llama-3.3-70B-Instruct | GPU 2,3 (88GB/卡) | **正常** |

4x NVIDIA RTX PRO 6000 Blackwell (98GB/卡)，GPU Util 0%（空闲等待请求）。

### 2. Benchmark 数据

已有数据文件：
- **AlpacaEval**: `benchmark_alpacaeval.jsonl`, `counterfactuals_alpacaeval.jsonl`, `verified_alpacaeval.jsonl`, `scored_alpacaeval_*.jsonl`, `pairwise_results_alpacaeval_*.jsonl`
- **MT-Bench**: `benchmark_mtbench.jsonl`, `counterfactuals_mtbench.jsonl`, `verified_mtbench.jsonl`, `scored_mtbench_*.jsonl`, `pairwise_results_mtbench_*.jsonl`
- **Cross-benchmark scored 数据** (大量已完成): `scored_*_formality.jsonl`, `scored_*_verbosity.jsonl`, `scored_*_register.jsonl` — 覆盖 Qwen32B / GPT-4o / Llama70B / Claude / Gemini Flash 多个 judge
- **Verified 数据**: `verified_*.jsonl` 覆盖 formality / verbosity / register / alpacaeval / mtbench

### 3. Pipeline 脚本接口

`pairwise_scoring.py` 使用 `AsyncOpenAI` 客户端，API key 传递方式：
- **CLI 参数**: `--api-key`
- **环境变量**: `OPENAI_API_KEY`
- **Base URL**: `--base-url`（默认 `http://47.94.22.126/v1`），也读 `OPENAI_BASE_URL` 环境变量
- **本地 vLLM 用法**: `--base-url http://localhost:8000/v1 --api-key dummy --model /root/autodl-tmp/models/Qwen3-32B/`

其他关键参数：`--axis` (formality/verbosity/tone/register), `--model`, `--max-concurrent`, `--disable-thinking`

### 4. 可立即跑的 cross-benchmark 配置

数据和 vLLM 都就绪，以下组合可直接执行：

| 输入数据 | Judge | 轴 | 端口 |
|----------|-------|----|------|
| `verified_alpacaeval.jsonl` | Qwen3-32B | formality/verbosity/register | localhost:8000 |
| `verified_mtbench.jsonl` | Qwen3-32B | formality/verbosity/register | localhost:8000 |
| `verified_alpacaeval.jsonl` | Llama-70B | formality/verbosity/register | localhost:8003 |
| `verified_mtbench.jsonl` | Llama-70B | formality/verbosity/register | localhost:8003 |
| 任何 `verified_*.jsonl` | 两个 judge | tone 轴 | 8000/8003 |

不需要重启任何服务，vLLM 双模型均在线。

---
