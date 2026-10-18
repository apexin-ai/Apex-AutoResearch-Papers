# analysis vif partial corr

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vif-partial-corr_20260522T235642_result.json`
- **Structured JSON:** [`2bd4bdb7b0faf8aa0cb1.json`](../../sessions/2b/2bd4bdb7b0faf8aa0cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json`。

**VIF 结果**:
- Mean VIF = 2.98，范围 [1.23, 7.03]
- 所有 MMLU conditions VIF < 3.1（共线性低）；ARC 的 score_manipulation (7.03) 和 position_bias (6.53) 偏高但均 < 10（可接受阈值）

**Partial Correlation 结果**:
- η_max 控制 K_eff 后：mean partial r = 0.305，9/12 conditions 中 η_max 的独立贡献更大
- K_eff 控制 η_max 后：mean partial r = 0.116
- η_max 在 MMLU 上尤其显著（partial r 0.30–0.60），K_eff 仅在 arc_challenge×position_bias (r=0.27) 和 arc_challenge×prompt_injection (r=0.21) 中贡献更大

---
