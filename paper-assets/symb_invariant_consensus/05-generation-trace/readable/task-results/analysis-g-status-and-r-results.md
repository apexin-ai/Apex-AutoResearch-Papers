# analysis g status and r results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-status-and-r-results_20260520T111606_result.json`
- **Structured JSON:** [`16ddd3fd443c1eebca26.json`](../../sessions/16/16ddd3fd443c1eebca26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## G 状态 — westd-16639

**状态: RUNNING**

| 指标 | 值 |
|------|-----|
| PID | 307169（原 384984 已死，新进程 18:15 启动） |
| 模型 | Mistral-7B-Instruct-v0.3 |
| 当前策略 | conservative |
| 进度 | **60/204** (29.4%) |
| 当前准确率 | 63.3% (38/60) |
| avg_trunc | 4.1%, matched=99% |
| 速度 | ~0.02 prob/s |
| ETA | ~8655s (~2.4h) |

注意：同一台机器上还有 `direction_q_premise_mutation.py` (PID 314822) 也在跑（刚启动于 19:15），以及 4 个 vLLM server 分别在 GPU 0-3 上。

---

## R 结果 — westd-25068 (deberta-large-mnli)

### 核心数据

| 策略 | 准确率 | Correct/Total | Delta vs SC |
|------|--------|---------------|-------------|
| **SC baseline** | **54.41%** | 111/204 | — |
| **SICA baseline** | **59.31%** | — | +4.90% |
| NLI standalone | 49.51% | 101/204 | -4.90% |
| **Combo w=1** | **57.84%** | 118/204 | **+3.43%** |
| **Combo w=3** | **58.82%** | 120/204 | **+4.41%** |
| Intersection (agree) | **68.48%** | 63/92 | — |

### Verifier 分析（exp_r2）

- Agreement rate: 45.1% (92/204 agree, 112 disagree)
- **Agree 时准确率: 68.48%**（远高于任一单独系统）
- Disagree breakdown:
  - DeBERTa 对 SC 错: **38** 题
  - SC 对 DeBERTa 错: **48** 题
  - 两个都错: **26** 题

### Per-label 分析

| Label | N | NLI Acc | SC Acc | NLI 优势 |
|-------|---|---------|--------|----------|
| True | 72 | 59.72% | 55.56% | +4.16% |
| **False** | 63 | **71.43%** | **38.10%** | **+33.33%** |
| Unknown | 69 | 18.84% | 68.12% | -49.28% |

**关键发现**: NLI 在 False 类上碾压 SC（71.4% vs 38.1%），但在 Unknown 类上严重弱势（18.8% vs 68.1%）。Combo 策略取长补短，w=3 达 58.82%，接近 SICA 的 59.31%。

### R large vs R small

两个目录使用**同一模型** (`deberta-large-mnli`)，数据完全一致。`direction_r_nli_large` 结构按实验分组（exp_r1/r2/r3），`direction_r_nli_small` 带 summary 格式。

---
