# ops d134 s47 pr verify s48 status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-s47-pr-verify-s48-status_20260518T174743_result.json`
- **Structured JSON:** [`acb4febc9a6802bbca25.json`](../../sessions/ac/acb4febc9a6802bbca25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. s47 eval_results.json (summary)

| 指标 | 值 |
|---|---|
| n_problems | 100 |
| **n_proved** | **89** |
| **prove_rate** | **0.89** |
| mean_isr | 0.0857 |
| isr_std | 0.1259 |
| median_isr | 0.0 |
| proved_only_mean_isr | 0.0963 |

### 2. s47 classify.json

| 指标 | 值 |
|---|---|
| n_proved | 89 |
| h7_total_count | 0 |
| h1_strict_count | 79 (88.76%) |
| h8_conjunction_collapse | 4 (4.49%) |
| conclusion_in_premise | 79 (88.76%) |
| content_independent | 4 (4.49%) |
| **genuine_count** | **6 (6.74%)** |

### 3. s47 真实最终 eval PR

**eval PR = 89/100 = 89%**，来源：`eval_results.json` 的 `prove_rate: 0.89`。

训练日志的 `prove_rate=0.629` 是训练集上最后一个 batch 的 moving average（`Final reward stats: prove_rate: 0.62875`），不是 eval 指标。eval 在 held-out 的 `proofwriter_fol_100.jsonl` 上跑的结果是 89%，这是论文应该用的数字。

### 4. s48 训练进度

| 指标 | 值 |
|---|---|
| 当前 step | **50/500** (10%) |
| 速度 | ~9 s/step |
| 已用时间 | ~8 min |
| 预估剩余 | **~68 min (~1h8m)** |
| GPU 占用 | PID 121901, 84688 MiB |
| 当前 prove_rate | 0.0~0.125（早期阶段，尚未起飞） |

---
