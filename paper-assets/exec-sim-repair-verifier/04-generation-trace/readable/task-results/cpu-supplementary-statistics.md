# cpu supplementary statistics

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_supplementary-statistics_20260521T054458_result.json`
- **Structured JSON:** [`40f8b92241e8475aedc7.json`](../../sessions/40/40f8b92241e8475aedc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行完成，输出已写入 `artifacts/supplementary_statistics.txt`。

关键发现：

**Bootstrap CI**: Qwen3-8B CLS 非常稳定（85.11 ± 0.63），DeepSeek CLS 含 outlier 时 CI 极宽（[74.93, 86.15]），去掉 outlier 后收窄到 [82.61, 86.15]。

**Cohen's d**: CLS vs TRAJ 所有比较均为 large effect（d > 0.8）。Qwen3-8B 的 d=5.015 极大，说明 CLS 对 TRAJ 在 repo-level 上优势显著且一致。CLS vs CWM 的 point difference 约 +20 pp，但 CWM 只有 1 个 seed 无法算 d。

**Power Analysis**: Qwen3-8B CLS vs TRAJ power=0.94（n=3 已够用）。DeepSeek CLS vs TRAJ power 仅 0.11（含 outlier）/ 0.09（去 outlier），因为 seed 间差异方向不一致，paired effect 被高方差淹没。DeepSeek 需要约 12-20 seeds 才能达到 power=0.80。

---
