# code m1 bootstrap ci prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m1-bootstrap-ci-prep_20260514T030631_result.json`
- **Structured JSON:** [`8d143bd8f93da3563eb9.json`](../../sessions/8d/8d143bd8f93da3563eb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**脚本**: `/root/autodl-tmp/pacs/analysis/bootstrap_phase_gradient.py`

**Dry-run 结果** (s=0.15, importance + random):

| 指标 | Importance | Random |
|---|---|---|
| Gradient (median_low/median_high) | **14.27** [11.97, 17.42] | **1.17** [0.93, 1.60] |
| Cohen's d (low vs high) | 0.71 | 0.01 |
| MW-U p (low vs high) | 2.98e-116 | 0.352 (ns) |
| Imp vs Rnd gradient p | < 0.001 *** | |

**关键发现**: Importance masking 下 low-sparsity phase 的 II 是 high-sparsity 的 ~14×，CI 远离 1；random masking gradient ~1（无相位依赖）。差异 p < 0.001，phase gradient 统计显著。

**技术说明**: 因 profiling_results.json 不保存 per-segment 原始 II 值，脚本使用 log-normal 参数化重建（精确匹配存储的 mean 和 median），然后做 bootstrap resample。

---
