# analysis seed comparison prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed-comparison-prep_20260516T004221_result.json`
- **Structured JSON:** [`dcb48eedb102ade09a0b.json`](../../sessions/dc/dcb48eedb102ade09a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**seed_comparison.py** — 可正常运行，输出对比表到 `eval_results/seed_comparison.{md,json}`。

**当前 eval 完成情况：**

| Method | 已完成 seeds | 待完成 |
|--------|-------------|--------|
| CED RSFT | s42, s43, s44 (3/4) | s45 (训练中) |
| flat-NLI RSFT | s42, s43 (2/4) | s44, s45 (eval 运行中) |

**关键指标（metrics_v2.json）：**

| | CED (3-seed mean) | flat-NLI (2-seed mean) | Delta |
|--|--|--|--|
| rel_f1 | **0.4610** | 0.4531 | CED +0.0079 |
| evi_f1 | 0.8124 | 0.8100 | CED +0.0024 |
| edcr | 0.6449 | 0.6468 | fNLI +0.0019 |

汇总已写入 `/root/autodl-tmp/eval_results/seed_status_summary.md`。

---
