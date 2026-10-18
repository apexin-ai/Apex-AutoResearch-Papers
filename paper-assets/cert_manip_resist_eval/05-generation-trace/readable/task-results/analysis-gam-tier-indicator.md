# analysis gam tier indicator

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gam-tier-indicator_20260522T190014_result.json`
- **Structured JSON:** [`35b6d4e1c128b0296073.json`](../../sessions/35/35b6d4e1c128b0296073.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

| Method | η_max FDR sig (/12) | K_eff FDR sig (/12) | K_eff sig+ | K_eff sig− |
|---|---|---|---|---|
| Canonical OLS | 11/12 | 8/12 | 7 | 1 |
| + Tier indicators | 10/12 | 5/12 | 4 | 1 |
| GAM (nonlinear) | 12/12 | 12/12 | 6 | 6 |

关键发现：

1. **Tier indicators** 吸收了部分 K_eff 效应（8→5 sig），η_max 也略降（11→10），说明 tier-level confounding 确实存在。但 K_eff 仍在 5/12 conditions 显著（4+/1−），表明控制 tier 后 K_eff 的独立效应仍部分保留。

2. **GAM** 结果非常强：K_eff 在 12/12 conditions 全部显著，η_max 也是 12/12。但方向性变为 6+/6−，说明 GAM 捕捉到的是 K_eff 的非线性 partial effect 显著（即 K_eff 和 ASR 之间存在显著的非线性关系），而非单调正向关系。

3. Canonical OLS 的 K_eff 7+/1− 与预期吻合。

JSON 已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/gam_tier_analysis.json`。

---
