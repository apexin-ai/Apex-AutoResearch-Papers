# diag eval 05B metrics collection

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_05B_metrics_collection_20260514T150728_result.json`
- **Structured JSON:** [`265e48a7e1073ef7151b.json`](../../sessions/26/265e48a7e1073ef7151b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d005 legacy metrics 已写入。汇总如下：

---

## 目录状态

| 目录 | 状态 |
|------|------|
| `Qwen2.5-0.5B_d100_s42_aligned/` | **空目录** — PID 389866 仍在 GPU 2 运行中 |
| `Qwen2.5-0.5B_d005_s42/` | 完整（3 文件：eval_results.json, correctness_matrix.json, item_responses.json） |
| `Qwen2.5-0.5B_d005_s42_aligned/` | **完整**（同样 3 文件，已有结果） |

## GPU 2 状态

PID 389866 在 GPU 2 运行，占用 3686MiB，正在执行 d100 aligned eval（mmlu gsm8k arc_challenge humaneval）。**未消失。**

## 指标汇总

### d005 legacy（已写入 registry `exp_001_eval_05B_d005`）

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.2929 | 4113/14042 |
| GSM8K | 0.3601 | 475/1319 |
| ARC-Challenge | 0.2858 | 335/1172 |
| HumanEval pass@1 | 0.0793 | 13/164 |

### d005 aligned（`Qwen2.5-0.5B_d005_s42_aligned/` — registry 无对应条目）

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.3255 | 4570/14042 |
| GSM8K | 0.3624 | 478/1319 |
| ARC-Challenge | 0.3285 | 385/1172 |
| HumanEval pass@1 | 0.0793 | 13/164 |

### d100 aligned

无结果（eval 仍在运行，输出目录为空）。

---

**注意**：d005 aligned 结果已存在但 registry 中没有独立条目（可能属于 `exp_001_eval_05B_aligned_batch` 的范围）。是否需要为其创建/更新 registry 条目？

---
