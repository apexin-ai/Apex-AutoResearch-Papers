# fix n500 pipeline d063 d064

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_n500_pipeline_d063_d064_20260515T045046_result.json`
- **Structured JSON:** [`18cbf80f747a9391362a.json`](../../sessions/18/18cbf80f747a9391362a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，三项变更已全部生效：

**D063** — random 条件不再有二元判断，改为 `significance` 字段（`***`/`**`/`*`/`ns`），LaTeX 和 CSV 均包含新列

**D064** — `dz_reliable` 布尔字段已加入（CI 宽度 > 0.5 或高 sparsity 下 CI 不对称比 > 3:1 → `false`）。Deepseek `s020_vs_s025` 被标记为不可靠（CI 宽度 0.507），LaTeX 中显示 `†`

**Rank-biserial** — `rank_biserial_r` 已加入 within-importance d_z 和 imp-vs-rand 两个分析块的 JSON/CSV/LaTeX/console 输出

---
