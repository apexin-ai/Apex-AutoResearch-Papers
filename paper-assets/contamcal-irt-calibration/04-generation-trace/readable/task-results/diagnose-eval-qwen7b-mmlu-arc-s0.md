# diagnose eval qwen7b mmlu arc s0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_qwen7b_mmlu_arc_s0_20260521T000639_result.json`
- **Structured JSON:** [`abad9d0edc294eb64657.json`](../../sessions/ab/abad9d0edc294eb64657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**MMLU Results (Qwen-7B s0):**

| Dosage | Accuracy |
|--------|----------|
| d000   | 66.32%   |
| d005   | 64.68%   |
| d025   | 65.67%   |
| d050   | 65.78%   |
| d100   | 65.29%   |

**ARC-Challenge Results (Qwen-7B s0):**

| Dosage | Accuracy |
|--------|----------|
| d000   | 87.20%   |
| d005   | 85.32%   |
| d025   | 84.47%   |
| d050   | 85.58%   |
| d100   | running (184/1172, ~3.5min left) |

ARC d100 正在跑最后一个 dosage，约3.5分钟后完成。结果已写入 `artifacts/eval_qwen7b_mmlu_arc_s0/eval_results_summary.md`。

注意：`eval_results.json` 会被后运行的 benchmark 覆盖——MMLU 真实结果在 `mmlu_results.json`，ARC 在 `arc_challenge_results.json`。

---
