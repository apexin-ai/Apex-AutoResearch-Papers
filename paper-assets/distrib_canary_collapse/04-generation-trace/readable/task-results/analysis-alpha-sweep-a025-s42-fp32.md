# analysis alpha sweep a025 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_s42_fp32_20260519T121714_result.json`
- **Structured JSON:** [`a96241e5843d1fc4b98c.json`](../../sessions/a9/a96241e5843d1fc4b98c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果汇总：

## alpha_sweep_a025_s42_fp32 结果

| 指标 | 值 |
|------|-----|
| **PermG fwd** | **0/8** |
| **PermG rev** | **0/8** |
| **K≥4** | **0/8** |
| **MMCT** | **0/8** (detection_rate=0.0) |
| d1 drift | **-39.15%** |
| d2 drift | -54.75% |
| d3 drift | -56.98% |
| mauve drift | -41.86% |
| entropy drift | -4.79% |
| ppl drift | -18.09% |
| eff_rank drift | -3.78% |

**Hypothesis validated = true**: PermG=0/8，α=0.25 确实低于 phase transition 阈值。

**值得注意的发现**：
- d1_drift = -39.15%，远超 α=0.50 的 -28.7%。多样性坍缩在 α=0.25 已经显著发生，但缺乏 Granger-detectable 的 lead-lag 因果结构。
- token_entropy→distinct_1 的 raw PermG p=0.007，但 FDR 校正后 p=0.053（borderline miss）。这暗示过渡点可能就在 α=0.25 附近。
- 所有 pair 最高 consensus votes = 3（差一票到 K≥4 threshold）。

**更新后的 dose-response map**：

| α | PermG | K≥4 | MMCT | d1 drift |
|---|-------|-----|------|----------|
| 0.05 | 0/8 | 0/8 | 0/8 | -24.9% |
| 0.10 | 0/8 | 0/8 | 0/8 | -23.0% |
| **0.25** | **0/8** | **0/8** | **0/8** | **-39.2%** |
| 0.50 | 6/8 | 6/8 | 0.75 | -28.7% |
| 0.60 | 3/8 | 7/8 | 7/8 | -28.2% |
| 1.00 | ~75% | ~6.5/8 | ~6.5/8 | -28.3% |

Phase transition 区间从 [0.10, 0.50] 收窄至 **[0.25, 0.50]**（PermG 角度）。

---
