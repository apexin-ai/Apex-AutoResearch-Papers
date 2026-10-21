# infra registry sync and cuda2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_registry-sync-and-cuda2_20260523T040452_result.json`
- **Structured JSON:** [`0c5e2332f32fa8f2a882.json`](../../sessions/0c/0c5e2332f32fa8f2a882.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部拿到了。

---

## 任务 1: 各 GPU 实际实验状态

### westd-16639（ProofWriter 全集 = 600 题）

| GPU | vLLM Port | 模型 | 实验 | 进度 | SC% | SICA% | Δ |
|-----|-----------|------|------|------|-----|-------|---|
| **0** | 8001 | **Qwen2.5-14B** | PW seed=456 | 436/600 (72.7%) | 74.08 | 72.94 | **-1.14pp** |
| **1** | 8006 | **LLaMA-3.1-8B** | PW seed=123 | 376/600 (62.7%) | 72.61 | 64.36 | **-8.25pp** |
| **2** | — | — | **IDLE** | — | — | — | — |
| **3** | 8005 | **Qwen2.5-14B** | PW seed=123 | 416/600 (69.3%) | 73.56 | 72.12 | **-1.44pp** |

- GPU 0 的 runner 是链式脚本：seed=456 完成后自动启动 **seed=789**
- 三个实验均活跃（日志最近几秒有 HTTP 200）
- 无 tmux session

### westd-14391

| GPU | vLLM Port | 模型 | 实验 | 进度 | SC% | SICA% | Δ |
|-----|-----------|------|------|------|-----|-------|---|
| **0** | 8000 | **LLaMA-3.1-8B** | PW seed=42 | 517/600 (86.2%) | 72.73 | 67.12 | **-5.61pp** |

- 用 `run_full_mvp.py`（不是 `run_cross_dataset_replication.py`），带 `--save-intermediates`
- 无 tmux session

### 回答关键疑问

1. **cuda:0** → Qwen2.5-14B PW seed=456（port 8001），完成后链式跑 seed=789
2. **cuda:1** → LLaMA-3.1-8B PW seed=123（port 8006）
3. **cuda:3** → **Qwen2.5-14B**（port 8005），不是 LLaMA。模型路径 = `Qwen2.5-14B-Instruct`，served-model-name = `qwen25-14b`

---

## 任务 2: cuda:2 可用性

| 项 | 状态 |
|----|------|
| GPU 2 | 完全空闲，0MiB / 97887MiB，0% util |
| Qwen2.5-7B-Instruct | **不在磁盘上** |
| 磁盘上的 Qwen | Qwen2.5-14B-Instruct, Qwen2.5-72B-Instruct-AWQ, Qwen3-14B |
| `/root/autodl-tmp/` 剩余空间 | **121GB**（350G 总，230G 已用）→ 足够下载 |

cuda:2 硬件可用，但需要先下载 Qwen2.5-7B-Instruct（~15GB）。空间充足。

---

## 需要注意

**所有 4 个在跑实验 SICA 均负于 SC**，LLaMA 尤其严重（-5.6 到 -8.3pp）。这些是中间结果，最终可能变化，但趋势一致。

---
