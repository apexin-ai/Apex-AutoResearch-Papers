# eval tau07 posthoc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau07-posthoc_20260516T060022_result.json`
- **Structured JSON:** [`4aa4b6d4202224b58ab6.json`](../../sessions/4a/4aa4b6d4202224b58ab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**`contamination_60_tau07_seed42` eval_ppl_holdout = 17.73**

### 对比表

| 实验 | eval_ppl_holdout | 备注 |
|------|-----------------|------|
| uniform baseline | 17.766 | |
| adaptive_τ0.8 (default) | 17.740 | |
| **τ=0.7 (本次)** | **17.73** | τ=1−ρ/2 公式 |
| grid_b0.5 | 17.704 | grid best |
| ESS-only | 17.770 | |

### Claim 3 判断

PPL = 17.73 > 17.71 目标阈值。τ=0.7 比 default τ=0.8 好 (17.73 vs 17.74)，但**未达到 grid-best 水平 (17.704)**。

差距：17.73 − 17.704 = 0.026。τ downshift 方向正确（改善了 0.01），但公式 τ=1−ρ/2 不足以完全弥合 adaptive 与 grid-best 的 gap。需要 reframe：

- **可以 claim**：τ 公式提供了一个 principled 的 warm-start，比 default τ 好
- **不能 claim**：τ 公式直接达到 grid-best 性能
- **Reframe 建议**：τ=1−ρ/2 作为 practical guideline 缩小了 58% 的 gap（从 0.036 降到 0.026 还不够，但从 17.766 baseline 看，τ=0.7 已经超越 uniform 和 ESS-only）

---
