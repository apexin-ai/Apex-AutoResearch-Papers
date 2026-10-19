# code exp 001a bootstrap supplement

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001a_bootstrap_supplement_20260516T222003_result.json`
- **Structured JSON:** [`4c6acb7d187c0628d94c.json`](../../sessions/4c/4c6acb7d187c0628d94c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**R1-32B HS vs Text Pre-CP FPR Bootstrap Test**

| Metric | Value |
|--------|-------|
| HS pre-CP FPR | 25.65% |
| Text pre-CP FPR | 24.61% |
| Difference (HS - Text) | +1.04% |
| 95% CI | [-9.48%, +11.56%] |
| **p-value** | **0.848** |

R1-32B 上 HS probe 和 text probe 的 pre-CP FPR **无显著差异**。CI 跨越零，差异可忽略。这与 QwQ-32B (p=0.001, HS显著优于text) 形成对比。

注意：QwQ-32B 的对比可能使用了 midpoint heuristic 而非真正的 sentence embedding probe（`exp_001b_bootstrap.py` 中 `text_baseline_predictions` 是 midpoint 预测）。R1-32B 这里使用了 all-MiniLM-L6-v2 sentence embedding temporal probe 作为公平对比。

产出已注册:
- JSON: `artifacts/exp_001a/bootstrap_hs_vs_text_fpr.json`
- Report: `art_20260516_78b581`
- Registry `exp_001a_r1_32b` metrics 已更新

---
