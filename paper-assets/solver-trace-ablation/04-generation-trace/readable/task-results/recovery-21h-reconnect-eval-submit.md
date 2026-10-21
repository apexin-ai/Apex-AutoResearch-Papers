# recovery 21h reconnect eval submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_21h-reconnect-eval-submit_20260516T065414_result.json`
- **Structured JSON:** [`72cb2849a9b088cbab18.json`](../../sessions/72/72cb2849a9b088cbab18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both GPUs fully loaded and producing training steps. Here's the structured report:

---

## 恢复报告

### 1. sweep-isr-b02-s44 (ISR β=0.2, seed=44)

| 项目 | 值 |
|------|-----|
| 状态 | **DONE — success** |
| 训练 | 500/500 steps 完成, checkpoint-500 已保存 |
| eval_prove_rate | 94% (94/100) |
| eval_mean_isr | 0.9058 (median=1.0) |
| **Taxonomy** | **H7a=100%, genuine=0%** |
| 结论 | ISR=1.0 mode collapse 复现 (与 s42/s43 一致)。模型学会 single-premise P→P tautology hacking |

### 2. plan018-additive-random-b01-s45-r3 (Random β=0.1, seed=45)

| 项目 | 值 |
|------|-----|
| 状态 | **DONE — failed** |
| 训练 | 400/500 steps, 磁盘满崩溃 |
| checkpoint | checkpoint-400 corrupt (2/4 shards), checkpoint-350 已删除 |
| 结论 | 需要完整重训（无可用 checkpoint） |

### 3. 已提交新实验

| exp_id | GPU | PID | Config | seed |
|--------|-----|-----|--------|------|
| sweep-exec-only-s45 | cuda:1 | 728319 | grpo_exec_only.yaml | 45 |
| sweep-exec-only-s46 | cuda:0 | 728245 | grpo_exec_only.yaml | 46 |

两个均为 exec-only baseline, 500 steps, Qwen3-4B. 预计 ~1h 完成。

### 4. 当前资源状态

| 资源 | 状态 |
|------|------|
| GPU 0 | 77.1/97.9 GB, 89% util (s46 训练中) |
| GPU 1 | 79.5/97.9 GB, 88% util (s45 训练中) |
| 磁盘 | 182G/250G used, **69G free** (73%) |

### 待办
- plan018-random-b01-s45-r3 需重跑 (r4)，等当前批次完成后提交
- sweep-isr-b02-s44 的 s44 数据确认 β=0.2 ISR 在所有 3 个 seed (42/43/44) 上均 mode collapse 到 100% H7a

---
