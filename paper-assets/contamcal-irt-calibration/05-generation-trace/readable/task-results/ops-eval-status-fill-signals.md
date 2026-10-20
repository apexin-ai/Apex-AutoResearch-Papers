# ops eval status fill signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-status-fill-signals_20260516T194912_result.json`
- **Structured JSON:** [`ab947a1d4c0045363108.json`](../../sessions/ab/ab947a1d4c0045363108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**Eval 进度**：d005/d025/d100 均只完成了 MMLU，gsm8k/arc/humaneval 仍在跑。无 .done 文件。

**Signals 进度**：
- d000: arc+gsm8k 已完成，mmlu 正在 GPU 1 计算
- d005: mmlu 刚开始（GPU 4），arc+gsm8k 需等 eval 完成

**当前 GPU 映射**：

| GPU | PID | 任务 | 显存 | 状态 |
|-----|-----|------|------|------|
| 0 | 825638 | eval d005 (mmlu✓, gsm8k/arc/humaneval 进行中) | 8081 MiB | Running |
| 1 | 830115 | signals d000 mmlu | 6903 MiB | Running |
| 2 | — | 空闲 | 0 MiB | Free |
| 3 | 822390 | eval d025 (mmlu✓, gsm8k/arc/humaneval 进行中) | 8313 MiB | Running |
| 4 | 842929 | signals d005 mmlu | 8281 MiB | Running |
| 5 | 831033 | eval d100 (mmlu✓, gsm8k/arc/humaneval 进行中) | 8313 MiB | Running |

**结论**：3 个 eval 均未完成，无法启动新的 arc/gsm8k signals。GPU 2 空闲待命。需等 eval 完成后再启动 signals。

---
