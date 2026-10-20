# fix exp006 baselines w1w2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp006_baselines_w1w2_20260514T035056_result.json`
- **Structured JSON:** [`d9a32de8437cbae4221b.json`](../../sessions/d9/d9a32de8437cbae4221b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。全部 7 个 baseline 正常运行，输出表包含 `Cov50`, `Cov80`, `Cov95` 三列。

**修改总结：**

1. **W1 — 三级 CI coverage**：
   - `utils.py`：新增 `wilson_ci_levels()`, `bootstrap_ci_levels()`, `posterior_ci_levels()` 三个多级 CI 辅助函数；`make_result()` 改为接收 ci dict（含 `ci_50/80/95_lower/upper` 6 个 key）
   - Stan 方法（`vanilla_4pl.py`, `single_signal_2pl_gamma.py`）：从后验样本提取 25/75、10/90、2.5/97.5 分位数
   - Bootstrap 方法（`linear_regression.py`, `dcr_fuzzy.py`, `emperor_mitigation.py`）：从 bootstrap 分布提取对应分位数
   - Wilson 方法（`remove_rescore.py`, `raw_scores.py`）：分别以 alpha=0.50/0.20/0.05 计算三级 Wilson CI
   - `run_all_baselines.py`：`compute_metrics()` 新增 `coverage_50` / `coverage_80`，输出表增加两列

2. **W2 — DCR 注释**：在 `dcr_fuzzy.py` 的 `calibrate()` 开头加了 adaptation 说明注释

---
