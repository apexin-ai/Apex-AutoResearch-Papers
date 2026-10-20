# analysis exp cheetah 008a s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_cheetah_008a_s2_20260527T230828_result.json`
- **Structured JSON:** [`9e6c50411746d46ba9ab.json`](../../sessions/9e/9e6c50411746d46ba9ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success.

## exp_cheetah_008a_s2 分析摘要

| 指标 | s0 | s1 | **s2** |
|------|-----|-----|--------|
| eval_return_105K | 366.19 | 281.24 | **457.4** |
| value_mean_105K | 164.58 | 164.29 | **188.6** |
| NVE_105K | 0.449 | 0.584 | **0.412** |
| civo_alert | 0 | 0 | **0** |

**附加指标 (s2)**:
- eval_return_peak = 589.7 @ step 95K
- gate_dt_mean = 2.0, gate_dt_2_frac = 1.0 (固定 dt=2 确认生效)
- EMA_005 = 139.9, EMA_095 = 204.3
- model_loss = 1.8, kl = 1.8, fps = 11.3

**Conclusion: success**

NVE_105K = 0.412，远低于 2.0 阈值，无 CIVO。三个 seed (s0=0.449, s1=0.584, s2=0.412) 一致显示 value suppression — 未暴露过 dt>1 的 dt_emb 在 gate_fixed_dt=2 下不会产生 value overestimation。C3 cross-env rebuttal reserve 证据完整。

---
