# cpu seed comparison data prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_seed_comparison_data_prep_20260516T052004_result.json`
- **Structured JSON:** [`a9d5aeacfb39b08df5af.json`](../../sessions/a9/a9d5aeacfb39b08df5af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成：

- **服务器**: `/root/autodl-tmp/eval_results/d076_seed_summary.json` — 8 条记录的机器可读汇总
- **本地**: `artifacts/d076_seed_status.md` — 完整状态表

**核心发现**：

| | 已完成 | 运行中 |
|---|---|---|
| CED | s43, s45 | s42, s44 |
| flat-NLI | s44, s45 | s42, s43 |

**需要关注的问题**：CED s43/s45 只有 `metrics.json`（无 `metrics_v2.json`），而 `seed_comparison.py` 会从 `metrics.json` 中删除 `ign_f1`。这意味着即使 CED 有数据，paired t-test 也拿不到 `ign_f1`。需要：
1. 对 CED s43/s45 跑 ign_f1 recomputation 生成 `metrics_v2.json`，或
2. 修改 `seed_comparison.py` 的 strip 逻辑，允许 D076 合规 eval 的 `metrics.json` 保留 `ign_f1`

---
