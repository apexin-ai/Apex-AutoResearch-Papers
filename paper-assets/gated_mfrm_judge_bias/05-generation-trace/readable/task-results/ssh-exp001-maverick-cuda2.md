# ssh exp001 maverick cuda2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_maverick_cuda2_20260522T025849_result.json`
- **Structured JSON:** [`396b7b4444be1acfdae7.json`](../../sessions/39/396b7b4444be1acfdae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报：Llama 4 Maverick 无法部署在单卡 cuda:2 上

### 当前服务器状态

| GPU | 进程 | VRAM | 利用率 |
|-----|-------|------|--------|
| 0 | `run_exp009.py --part both` | 73.6GB / 96GB | 68% |
| 1 | `run_exp012.py` | 73.7GB / 96GB | 64% |
| 2 | vLLM (Llama-3.3-70B AWQ) → port 8001 | 90.1GB / 96GB | 100% |
| 3 | vLLM (可能 Qwen2.5-72B AWQ) → port 8002 | 88.1GB / 96GB | 0% |

- Arena-Hard 已用 llama-3.3-70b judge 收集 **41 条** judgment（数据已保留）
- 磁盘：`/root/autodl-tmp/` 剩余 171GB
- 本地无 Maverick 模型

### Maverick 尺寸问题

Llama 4 Maverick 是 MoE 模型（400B total, 128 experts, 17B active）：

| 精度 | VRAM 需求 | 最少 GPU 数（96GB卡） |
|------|-----------|---------------------|
| BF16 | ~800GB | 9 卡 |
| FP8 | ~400GB | 5 卡 |
| INT4/AWQ | ~224GB | **3 卡** |
| 1.78-bit GGUF | ~122GB | 2 卡（质量严重下降，vLLM 不支持 GGUF） |

**单卡 96GB 完全不可能。** 即使最激进的合理量化（AWQ/W4A16）也需要 224GB，至少 3 张卡。

### 可选方案

1. **TP=3（GPU 2+3 + 停一个实验腾出 GPU 0 或 1）** — 3×96GB=288GB，可跑 AWQ。代价是停掉 exp009 或 exp012 之一 + 停掉一个现有 vLLM judge
2. **TP=4（停掉全部，4 卡全给 Maverick）** — 384GB，FP8 也够。代价最大
3. **放弃本地部署，走 API** — Together AI / Fireworks / Groq 都有 Maverick endpoint，无需本地 GPU。延迟会增加但不影响 judge 数据收集
4. **保持现状用 Llama-3.3-70B** — 已在跑，数据正在收集，不需要任何改动

请确认要走哪个方案。如果选方案 1，需要告知可以停哪个实验。

---
