# fix exp 012 cleanup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_012_cleanup_20260521T225611_result.json`
- **Structured JSON:** [`8dba3bdd2618bc4f0366.json`](../../sessions/8d/8dba3bdd2618bc4f0366.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 1. 删除旧 CSV
`error_propagation.csv` 和 `summary.csv` 已删除。目录剩余：`cn_degradation.png`、`error_propagation.png`、`run_exp012.py`。

### 2. Docstring 修改
全文件仅 2 处匹配，均在 `generate_exp012_data` 的 docstring 中：

- **`run_exp012.py:43`** — `bimodal e (Beta mixture), s ~ N(0, 0.8).` → `bimodal e: 30% high-exposure items uniform(0.7, 1.0),`
- **`run_exp012.py:44`** — `Confounding: e correlated with -b, s correlated with -d, both via rho.` → `70% low-exposure items uniform(0.0, 0.2), s ~ N(0, 0.8).`
- **`run_exp012.py:45`** — 新增 `Confounding: s correlated with -d via rho.`（保留原有的 s-d confounding 说明）

无 "Beta(2,5)"、"Beta(5,2)"、"rank-matching" 的匹配。逻辑代码未修改。

---
