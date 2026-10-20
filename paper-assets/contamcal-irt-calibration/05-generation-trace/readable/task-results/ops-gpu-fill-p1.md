# ops gpu fill p1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-fill-p1_20260516T162720_result.json`
- **Structured JSON:** [`7454e1a401614ae74bbb.json`](../../sessions/74/7454e1a401614ae74bbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ALL 6 GPUs 已满载。

## 状态汇报

| GPU | 任务 | PID | 运行时间 | 显存 | 预计剩余 |
|-----|------|-----|---------|------|---------|
| cuda:0 | Llama-3.2-3B d005 SFT | 804570 | 57min | 16.3/24.6 GB | ~1-2h |
| cuda:1 | Llama-3.2-3B d000 eval (gsm8k,arc,humaneval aligned) | 807025 | 54min | 6.9/24.6 GB | ~30-60min |
| cuda:2 | **NEW: 1.5B-Instruct GSM8K signals** | 815287 | 刚启动 | 加载中 | ~1.5-2h |
| cuda:3 | Llama-3.2-3B d025 SFT | 801766 | 1h21min | 17.8/24.6 GB | ~30-60min |
| cuda:4 | 1.5B-Instruct MMLU signals (selfcritique chunking) | 810809 | 39min | 3.9/24.6 GB | ~1-2h |
| cuda:5 | Llama-3.2-3B d100 SFT | 804791 | 57min | 20.6/24.6 GB | ~1-2h |

**新提交任务：**
- cuda:2 → `1.5B-Instruct GSM8K signals --signal all`（P1-1 优先级，tmux session: `signals_15b_gsm8k`）
  - 已启动，正在计算 s1_embedding（将续算 minkpp + selfcritique）

**已完成确认：**
- PID 797754 (0.5B-Instruct eval/signals on cuda:2): 已完成退出。exp008 输出完整（mmlu/gsm8k/arc_challenge 各 4 个 json，含 merged）

**下一波空闲 GPU 分配计划：**
1. cuda:1 释放后 → Llama d005 eval（如 d005 SFT 也完成）或 Llama d000 signals
2. cuda:3 释放后 → Llama d025 eval
3. cuda:0/5 释放后 → Llama d005/d100 eval

---
