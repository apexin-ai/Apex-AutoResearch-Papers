# ops cleanup registry fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-registry-fill_20260516T192343_result.json`
- **Structured JSON:** [`066becb05610dc144ef3.json`](../../sessions/06/066becb05610dc144ef3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Kill 后 GPU 状态

| GPU | 状态 | PID | 任务 |
|-----|------|-----|------|
| 0 | 占用 | 825638 | eval: Llama d005_s42 (mmlu/gsm8k/arc/humaneval) |
| 1 | 占用 | 830115 | signals: Llama d000_s42 mmlu |
| 2 | 占用 | 839655 | signals: Llama d000_s42 gsm8k — **不在 kill 列表中，未释放** |
| 3 | 占用 | 822390 | eval: Llama d025_s42 (mmlu/gsm8k/arc/humaneval) |
| 4 | **空闲** | — | — |
| 5 | 占用 | 831033 | eval: Llama d100_s42 (mmlu/gsm8k/arc/humaneval) |

### 2. Llama eval 完成状态

三个 eval **都未完成**，仅产出 `mmlu_results.json`，正在继续跑后续 benchmark：

| Dosage | mmlu | gsm8k | arc_challenge | humaneval | .done |
|--------|------|-------|---------------|-----------|-------|
| d005 | done | running (GPU 0) | pending | pending | NO |
| d025 | done | running (GPU 3) | pending | pending | NO |
| d100 | done | running (GPU 5) | pending | pending | NO |

参考：已完成的 d000 eval 包含 7 个文件（mmlu/gsm8k/arc_challenge/humaneval_results + correctness_matrix + eval_results + item_responses + .done）。

### 3. Signals 启动

**无法启动** — 三个 Llama eval 均未完成，不满足启动条件。

GPU 4 当前空闲，等 eval 完成后可用。需要指示：是否在 GPU 4 上启动其他任务（如 d000 的 arc_challenge signals），还是保留等 eval 先完成？

---
