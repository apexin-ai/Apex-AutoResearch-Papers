# harvest eval grpo 25 results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_grpo_25_results_20260517T025859_result.json`
- **Structured JSON:** [`d820469b10cc898e2fde.json`](../../sessions/d8/d820469b10cc898e2fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的状态汇总：

---

### 1. eval_grpo_standard_25 (westd-11672) — **已完成**

| 指标 | 值 |
|------|------|
| **Accuracy** | **51.10% ± 1.38%** |
| n_correct / n_total | 674 / 1319 |
| EOS rate | 96.29% |
| Avg response length | 292.9 |
| Truncated | 49 / 1319 (3.7%) |
| 结果文件 | `eval_grpo_standard_25_n1319.json` |

---

### 2. eval_grpo_rasp_25 (westb-23072) — **仍在运行**

| 指标 | 值 |
|------|------|
| 进程 PID | 639423 (CPU 占用 102%, 运行 7h25m) |
| 当前进度 | ~967/1319 (**73.3%**) |
| 最近 checkpoint (950/1319) | acc=**52.74%**, eos_rate=92.53%, avg_len=440 |
| 输出文件 | `eval_grpo_rasp_25_n1319.json` (尚未生成) |
| 预计剩余 | ~2-3 小时 |

---

### 初步对比（25% sparsity, GSM8K greedy）

| 模型 | Accuracy | EOS rate | Avg len |
|------|----------|----------|---------|
| GRPO-Standard-25 | 51.10% | 96.29% | 293 |
| GRPO-RASP-25 (interim) | 52.74% | 92.53% | 440 |

RASP 在 accuracy 上暂时领先 ~1.6pp，但 EOS rate 更低 (92.5% vs 96.3%)，平均生成长度更长 (440 vs 293)，说明 RASP 模型生成更冗长、更多 truncation。这和 C1 (reward-accuracy decoupling) 的叙事一致：RASP 恢复的结构在 accuracy 上有效，但生成行为有差异。

RASP eval 预计再跑 2-3 小时完成，届时需要再来收割最终结果。

---
