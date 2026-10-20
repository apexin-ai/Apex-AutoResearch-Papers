# ops checkpoint check reeval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint-check-reeval_20260515T005331_result.json`
- **Structured JSON:** [`33593d8efe3f0b52f086.json`](../../sessions/33/33593d8efe3f0b52f086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 已释放（仅 GPU 1 有训练进程 51297）。

---

## 汇报

### 1. Checkpoint 存活

| Experiment | 路径 | 状态 |
|---|---|---|
| exp1_isr_b03_s43 | — | **MISSING**（目录不存在） |
| exp1_isr_b03_s44_r2 | `/root/autodl-tmp/outputs/exp1_isr_b03_s44_r2/checkpoint-500` | **EXISTS** |
| exp1_random_b03_s43 | — | **MISSING**（目录不存在） |
| exp1_random_b03_s44_r2 | `/root/autodl-tmp/outputs/exp1_random_b03_s44_r2/checkpoint-50` | **训练中**（step 78/500） |

### 2. exp1_random_b03_s44_r2 训练状态

- PID 51297 存活，GPU 1 占用 80318 MiB，utilization 90%
- 当前 step 78/500，仅 checkpoint-50
- 预计还需较长时间完成

### 3. 磁盘/GPU 状态

- 根分区：30G，已用 9.1G (31%) ✓
- autodl-tmp：250G，已用 82G (33%) ✓
- GPU 0：空闲
- GPU 1：PID 51297 训练中

### 4. Eval 结果（使用 proofwriter_fol_100.jsonl）

**仅 exp1_isr_b03_s44_r2/checkpoint-500 可 eval**，其余 checkpoint 不存在或训练未完成。

| 指标 | 值 |
|---|---|
| **Prove Rate (PR)** | 95.0% (95/100) |
| **Mean ISR** | 0.705 ± 0.172 |
| **Proved-only ISR** | 0.7421 |
| **Median ISR** | 0.750 |
| **H7 strict** | **100.0%** (95/95) |
| **H1 strict** | 0.0% (0/95) |
| **H7+H1** | **100.0%** (95/95) |
| **Single premise** | 100.0% (95/95) |
| **ISR=1.0** | 0.0% |
| **genuine reasoning** | **0.0%** |

**结论**：100% H7 — 模型完全退化为 "单前提 = 结论" 的 shortcut 策略。ISR 恒定 0.75 是因为 STA 中 conclusion_quantifier 组件始终冗余（4 components 中 3 个 necessary）。没有真正的推理。

**待完成**：
- exp1_isr_b03_s43、exp1_random_b03_s43 的 checkpoint 已丢失，无法 re-eval
- exp1_random_b03_s44_r2 需等训练完成（step 78/500）后再 eval

---
