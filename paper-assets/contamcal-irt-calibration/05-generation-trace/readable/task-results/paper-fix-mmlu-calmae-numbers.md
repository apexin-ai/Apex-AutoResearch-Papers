# paper fix mmlu calmae numbers

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_mmlu_calmae_numbers_20260517T041104_result.json`
- **Structured JSON:** [`6a4488d9264227565745.json`](../../sessions/6a/6a4488d9264227565745.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

These are all logs/old reports — not paper source files. No further edits needed.

**变更摘要：**

| 文件 | 行 | 变更 |
|------|-----|------|
| `artifacts/paper_draft/experiments.tex` | 132 | calMAE: 0.017→0.008, 增加 "$N=18$ after excluding degenerate Llama models" |
| `artifacts/paper_draft/experiments.tex` | 193 | calMAE: 0.017→0.008, ΔMAE: 0.028→0.030, 增加 "$N=18$" |
| `writing_plan.yaml` | 136 | N=20→18, calMAE=0.017→0.008, ΔMAE=0.028→0.030 |
| `writing_plan.yaml` | 174 | MMLU 0.017→0.008 |

ARC 和 GSM8K 数字未变。`paper/sections/` 目录下的 md 文件不含旧值，无需修改。

---
