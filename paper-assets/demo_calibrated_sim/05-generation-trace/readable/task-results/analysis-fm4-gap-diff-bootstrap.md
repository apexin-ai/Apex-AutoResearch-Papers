# analysis fm4 gap diff bootstrap

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fm4-gap-diff-bootstrap_20260513T155612_result.json`
- **Structured JSON:** [`4a8516708412337c8a83.json`](../../sessions/4a/4a8516708412337c8a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FM4 gap-difference bootstrap 完成。结果：

| | Point Estimate | 95% CI | p-value (one-sided) | Significant? |
|---|---|---|---|---|
| **AAVE** | +0.155 | [-0.065, 0.360] | 0.081 | No |
| **Indian** | +0.161 | [-0.052, 0.366] | 0.069 | No |

**结论**：两个方言的 gap-difference 方向一致（DPO+BCP 确实反转了 BCP 的校准方向），点估计 ~0.16，但 95% CI 包含 0，one-sided p-value 在 0.07-0.08，**未达 α=0.05 显著水平**。

根本原因是 Base BCP 只有 1 run（n=19~20 per variant），样本量不足导致 CI 宽。如果 bcp7b-multirun-001（当前 ANALYZING 状态）的 3 runs 数据可用，pooled 后 base 侧 n 可从 ~20 提升到 ~80，CI 会大幅收窄。

已更新：
- Registry `bootstrap-ci-001` metrics 新增 `C2_fm4_gap_diff_aave` 和 `C2_fm4_gap_diff_indian`
- 结果写入 `/root/democalib/results/bootstrap_fm4_gap_diff_results.json` 并追加到 `bootstrap_ci_results.json`
- 脚本：`/root/democalib/scripts/bootstrap_fm4_gap_diff.py`

---
