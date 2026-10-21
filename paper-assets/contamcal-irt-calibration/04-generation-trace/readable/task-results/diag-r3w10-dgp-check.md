# diag r3w10 dgp check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_r3w10-dgp-check_20260521T005828_result.json`
- **Structured JSON:** [`aac6c7e7f7f927bb2e93.json`](../../sessions/aa/aac6c7e7f7f927bb2e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。状态和产出已更新到 registry。

## 结果摘要

**状态**: DONE, conclusion = **negative**（假设被拒绝）

**核心发现**: Linear gamma 模型在 threshold DGP 下**不产生系统性 attenuation**，与假设相反：

| DGP | Attenuation ratio (γ̂/γ_true) | 方向 |
|-----|------|------|
| **Linear** | 0.84–1.07（多数 <1） | 轻微**低估** γ |
| **Threshold** | 0.94–1.24（多数 >1） | 轻微**高估** γ |

**覆盖率退化**: Threshold DGP 下，J 增大时 95% CI coverage 显著下降——J=500, γ=2.0 时仅 0.70，J=500, γ=3.0 时仅 0.70。说明模型虽然点估计方向不是 attenuation，但不确定性被低估。

**结论**: Linear model 在 threshold DGP 下不是 gamma_hat < gamma_true 的 attenuation 模式，而是 gamma_hat ≥ gamma_true 的轻微过估计。假设"linear misspecification 导致 attenuation"不成立。但 coverage 退化表明 misspecification 仍然有实际影响——置信区间过窄，可靠性下降。

---
