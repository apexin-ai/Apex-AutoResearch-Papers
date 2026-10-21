# ops fill cuda2 immediate

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cuda2-immediate_20260516T201504_result.json`
- **Structured JSON:** [`39208015d404cf8ccacb.json`](../../sessions/39/39208015d404cf8ccacb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. cuda:2 分配任务

**PID 853489** — `compute_signals.py` Llama-3.2-3B d025, 顺序执行 mmlu → arc_challenge → gsm8k（all signals）

当前状态：S1 embedding (mmlu) 进行中，42% batch encoding，~75 it/s

### 2. 完整 6 卡状态

| GPU | VRAM | Util | PID | Task |
|-----|------|------|-----|------|
| 0 | 8081 MiB | 74% | 825638 | eval d005_aligned (mmlu/gsm8k/arc/humaneval) |
| 1 | 6967 MiB | 61% | 830115 | signals d000 mmlu |
| **2** | **569 MiB** | **11%** | **853489** | **signals d025 mmlu→arc→gsm8k (NEW)** |
| 3 | 12171 MiB | 74% | 822390 | eval d025_aligned (mmlu/gsm8k/arc/humaneval) |
| 4 | 7421 MiB | 59% | 842929 | signals d005 mmlu |
| 5 | 8313 MiB | 74% | 831033 | eval d100_aligned (mmlu/gsm8k/arc/humaneval) |

备注：
- GPU 2 当前 VRAM 低是因为 S1 用 MiniLM-L6-v2 (tiny model)；后续 S2-S4 加载 3B 模型时会升至 ~7-8GB
- d025_aligned eval 已完成 3/4 benchmarks (mmlu+arc+gsm8k done, humaneval 在跑)，同时 GPU 3 也在继续跑 eval
- 日志路径：`/root/autodl-tmp/logs/signals_llama_d025_all.log`

---
