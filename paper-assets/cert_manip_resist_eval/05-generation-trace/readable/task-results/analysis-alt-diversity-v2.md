# analysis alt diversity v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alt-diversity-v2_20260523T191948_result.json`
- **Structured JSON:** [`f8307d140eb7d2758e9d.json`](../../sessions/f8/f8307d140eb7d2758e9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V2 修复完成。结果对比：

| 指标 | V1 (旧) | V2 (修复后) |
|------|---------|-------------|
| **K_eff sig** | 8/12 | **12/12** |
| **K_eff dir** | 7+/1- | **12+/0-** |
| **K_eff β̄** | 0.164 | **0.430** |

Alt diversity measures 变化：
- **Q_statistic**: D 9/12 (6+/3-), ρ(K_eff)=0.599 — 与 K_eff 相关性最弱
- **Disagreement**: D 11/12 (11+/0-), ρ(K_eff)=0.934 — 高度一致
- **κ-diversity**: D 11/12 (11+/0-), ρ(K_eff)=0.978 — 与 K_eff 几乎等价

K_eff 12/12, 12+/0- 与 `table1_corrected.json` 完全一致。ρ(κ, K_eff) = 0.978 稳定。JSON 已保存至 `docs/paper/data/alt_diversity_corrected.json`。

---
