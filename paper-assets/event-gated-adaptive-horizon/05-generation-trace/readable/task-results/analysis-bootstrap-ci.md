# analysis bootstrap ci

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci_20260516T194558_result.json`
- **Structured JSON:** [`2228babeb6fb66d2e4d4.json`](../../sessions/22/2228babeb6fb66d2e4d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Condition | n | NVE mean | NVE 95% CI | Collapse rate | Collapse CI |
|-----------|---|----------|-----------|---------------|-------------|
| trained_dt_emb | 4 | 5.61 | [1.86, 11.46] | 75% | [0.30, 0.95] |
| no_dt_emb | 3 | 0.91 | [0.82, 0.97] | 0% | [0.00, 0.56] |
| full_sgs | 2 | 1.19 | [0.72, 1.66] | 50% | [0.10, 0.91] |

- **Cross-env classification**: 7/7 correct (100%) at threshold 1.5×, CI=[1.0, 1.0]
- **Effect size**: Cohen's d = 1.0 (large), mean difference = 4.7×
- **Key finding**: trained_dt_emb CI lower bound (1.86) > no_dt_emb CI upper bound (0.97) — 完全不重叠，统计分离明确

注意事项：
- no_dt_emb 中 009c 的 NVE 值是基于 "normalized v/e < 1.5x" 定性描述估算的 (0.82)
- full_sgs 只有 n=2（018 有配置错误，018v2 是修正版），CI 很宽
- 008d seed 0 的 NVE=1.67 是下界（实验在 55K 步被终止）

---
