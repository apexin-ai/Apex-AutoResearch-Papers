# diagnose mvp v4 legacy s02

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_v4_legacy_s02_20260514T000552_result.json`
- **Structured JSON:** [`041cc335d65205746848.json`](../../sessions/04/041cc335d65205746848.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_v4_legacy_s02 诊断结果
- **状态**: SUCCESS (PASS)
- **退出原因**: 正常完成，50/50 problems 全部处理完毕
- **日志路径**: `/root/autodl-tmp/pacs/profiling_output_v4b.log`
- **输出目录**: `/root/autodl-tmp/pacs/profiling_output_v4b/`
- **结果文件**: `/root/autodl-tmp/pacs/profiling_output_v4b/profiling_results.json`

### Metrics (sparsity=0.2, importance masking)

**Interaction Index:**

| Phase | II mean | 95% CI |
|-------|---------|--------|
| high_sparsity | +21.2856 | [+0.0292, +63.1630] |
| mid_sparsity | +21.8743 | [+4.9863, +41.7850] |
| low_sparsity | +0.0000 | [0.0, 0.0] |

**Perplexity (dense → attn → kv → both):**
- high_sparsity: 1.15 → 1.32 → 104.42 → 63.41
- mid_sparsity: 1.12 → 1.29 → 324.16 → 170.47
- low_sparsity: 1.11 → 1.30 → 1.11 → 1.30

**Phase token counts:** high=25862 (511 seg), mid=27996 (391 seg), low=32349 (454 seg)

**Verdict**: PASS — ci_overlap_test passed (low vs mid CI non-overlapping at 0.2)

---

### 其他实验状态

| 实验 | PID | 状态 | 备注 |
|------|-----|------|------|
| s01 / v4a (cuda:0, sparsity=0.1) | 27689 | **running** (Rl, 45min) | 正在处理，尚无结果文件 |
| s03 / v4c (cuda:2, sparsity=0.3) | 28452 | **exited, completed** | Verdict: **FAIL** — II[high]=-224.5, CI 跨零 |
| random_r2 (cuda:3) | 32187 | **running** (S, 37min) | 输出目录尚空 |

---
