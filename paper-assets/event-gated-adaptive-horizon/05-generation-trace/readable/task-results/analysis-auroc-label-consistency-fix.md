# analysis auroc label consistency fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_auroc-label-consistency-fix_20260522T044310_result.json`
- **Structured JSON:** [`69042f3d9f7851d5abfe.json`](../../sessions/69/69042f3d9f7851d5abfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**标签修复**: 008e_v3_s2 在 n=29 分析中从 CIVO 改为 non-CIVO (IRD)。n=16 分析无需改动（已正确标记）。

**更新后 AUROC**:

| 分析 | AUROC | 95% CI | θ=1.5× 准确率 |
|------|-------|--------|---------------|
| n=16 | 0.969（不变） | [69.8%, 99.8%] | 15/16 = 93.8% |
| n=29 | **0.953**（原 0.971，Δ=−0.018） | [0.867, 1.000] | 26/29 = 89.7% |

**n=29 修正后 Confusion Matrix (θ=1.5×)**: TP=12, FP=3, FN=0, TN=14

**3 个 FP**:
- `025_obs_sgs_s2` (NVE=1.73) — obs-decoder SGS 副作用，非 CIVO
- `028_rave_ceil15` (NVE=2.23) — RAVE anchor pollution，非 CIVO
- `008e_v3_s2` (NVE=3.78) — IRD，eval 崩溃导致 NVE 被动上升

**标签一致性**: 025_obs_sgs_s2 和 028_rave_ceil15 仅存在于 n=29（SGS/RAVE 实验晚于 n=16），不存在跨分析不一致。008e_v3_s2 现在在所有分析（n=8/n=12/n=16/n=29）中统一为 non-CIVO。

报告已注册：`artifacts/_project/report/auroc_label_fix_report.md`

---
