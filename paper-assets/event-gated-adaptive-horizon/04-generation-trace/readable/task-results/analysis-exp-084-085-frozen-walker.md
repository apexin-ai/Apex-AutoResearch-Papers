# analysis exp 084 085 frozen walker

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_084_085_frozen_walker_20260525T193328_result.json`
- **Structured JSON:** [`99a7f6fb65ee89a1ec7d.json`](../../sessions/99/99a7f6fb65ee89a1ec7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个实验均已更新至 DONE (success)，报告已注册。

## 结果总结

| | exp_084 (s0) | exp_085 (s1) | 对比: 训练dt_emb (009e) |
|--|--|--|--|
| eval_final | 281.5 | 69.3 | 82.8 (collapse) |
| eval_peak | 334.1 @ 95K | 281.5 @ 65K | 167.2 @ 25K |
| ve_ratio_peak | 0.9 @ 75K (瞬态) | 1.2 @ 85K (瞬态) | 1.67 @ 55K (持续上升) |
| ve_ratio_final | 0.2 | 0.8 | 1.03 |
| NVE_median (末5点) | **0.5x** | **0.5x** | **4.13x** |
| civo/alert | 0.0 (全程) | 0.0 (全程) | 触发 |
| value_mean趋势 | 下降 (77→62) | 稳定 (~55) | 上升 (膨胀) |
| nve_classification | **no_civo** | **no_civo** | onset_collapse |

**关键诊断**: 两个 frozen 实验的 ve_ratio 尖峰均由 eval 波动（分母）驱动，而非 value 膨胀（分子）。value_mean 全程稳定/下降，这与 CIVO 的系统性 value 过估机制完全相反。

**结论**: Hypothesis 得到验证 — frozen dt_embedding 不触发 CIVO。dt_emb 的**训练**（梯度流经 embedding 层）是 CIVO 发生的必要条件，而非 embedding 的存在本身。这与 exp_042（210K steps frozen Walker）、exp_087（frozen Cheetah s1）形成 3 实验 × 2 环境 × 多 seed 的一致结论。

---
