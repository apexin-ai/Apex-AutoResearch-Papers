# analysis alpha sweep a060 s42 fp32 v4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a060_s42_fp32_v4_20260520T114641_result.json`
- **Structured JSON:** [`c1ee87ef91c38ac431a3.json`](../../sessions/c1/c1ee87ef91c38ac431a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

## alpha_sweep_a060_s42_fp32_v4 分析摘要

**训练**: EXIT_CODE=0, 11 generations 全部完成，无 W&B run。

**PermG_fwd = 0/8** — 非单调 dip 确认。尽管 degradation 幅度（entropy -28.5%, ppl +92.3%）接近 α=0.75，PermG 在 FDR 校正后无一显著。ece→distinct_1 (raw p=0.034) 和 ece→distinct_2 (raw p=0.047) 在 raw 水平略低于 0.05，但 BH FDR 校正后不显著。

**5-method 汇总**:

| Method | Forward |
|--------|---------|
| PermG (FDR) | **0/8** |
| diff_xcorr (FDR) | 6/8 |
| naive_xcorr (D111) | 2/8 |
| threshold_onset_3σ | 0/8 |
| TY Granger | 0/8 |
| **K≥3** | **0/8** |

**Dose-response 非单调性**: α=0.50→6/8, **α=0.60→0/8**, α=0.75→6/8。α=0.60 处 downstream 退化是渐进平滑的，无 3σ spike，canary-downstream 时间领先关系不可检测。

**Registry** 已更新 (conclusion=success, metrics 含完整 drift 和 lead-lag 数据)。**Artifact** 已注册（report + JSON）。

**下一步建议**: 需要 s43/s44 seeds 确认该 dip 非 seed-specific artifact。

---
