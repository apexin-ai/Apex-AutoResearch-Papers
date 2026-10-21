# fix bootstrap ci sgs full

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap-ci-sgs-full_20260516T184606_result.json`
- **Structured JSON:** [`de9dca44864421c7c917.json`](../../sessions/de/de9dca44864421c7c917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改汇总：

**修改的文件：**
1. `artifacts/bootstrap_cis/bootstrap_ci_summary.md`
2. `artifacts/_project/report/bootstrap_ci_summary.md`

**新建的文件：**
3. `artifacts/bootstrap_cis/bootstrap_cis.json`（含完整结构化数据）

**具体修正内容：**
- SGS_full `nve_peak`: 4.010 → **1.660**（35K+ window，出现在 95K）
- SGS_full exceedance rate: 1.000 → **0.250**（2/8 steps exceed 1.5×）
- Effect size 表 SGS_full nve_peak 对应更新为 1.660，Δ = −1.770
- 保留了 4.01× 作为 raw 值并注明 "pre-threshold noise, outside 35K+ diagnostic window"
- JSON 中包含 `nve_peak_raw`, `nve_peak_raw_step`, `nve_peak_note`, `nve_timeline_35K_plus`, `exceedance_count/total` 等字段

---
