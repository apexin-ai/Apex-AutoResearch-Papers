# analysis alpha sweep a050 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_s43_fp32_20260519T094833_result.json`
- **Structured JSON:** [`62f8e634f04e12a18f25.json`](../../sessions/62/62f8e634f04e12a18f25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 分析总结：alpha_sweep_a050_s43_fp32

**模型**: Pythia-410m, seed=43, α=0.50, fp32, 11 代（gen0-gen10）

### 关键 Metrics

| 指标 | gen0 | gen10 | drift% |
|------|------|-------|--------|
| token_entropy | 3.234 | 2.723 | **-15.81%** |
| ece | 0.011 | 0.084 | **+679.56%** |
| perplexity | 26.95 | 31.58 | +17.17% |
| distinct_1 | 0.093 | 0.066 | -29.0% |
| distinct_2 | 0.507 | 0.323 | -36.25% |
| distinct_3 | 0.835 | 0.565 | -32.38% |
| effective_rank | 46.61 | 58.47 | +25.44% |
| mauve | 0.030 | 0.023 | -23.54% |

### 因果检验

| 方法 | 结果 |
|------|------|
| perm_granger_fwd | **6/8** |
| perm_granger_rev | 0/8 |
| ty_granger_fwd | 5/8 |
| naive_xcorr_fwd | 8/8 |
| diff_xcorr_fwd | 6/8 |
| threshold_onset_fwd | 8/8 |
| consensus_k4 | **6/8** |
| mmct_wpair_fwd | **0.75** |

### Boundary Regime 判断

**PermG = 6/8，α=0.50 fp32 已明确跨过 step function 阈值。** 这与 pre-D080 fp16 数据中 α=0.50 PermG 不确定的结果形成对比。fp32 精度下，boundary regime 的因果信号显著增强：
- 6/8 pairs 通过 PermG 前向检验（BH FDR 校正后显著），反向 0/8 确认方向性
- consensus_k4 = 6/8，MMCT = 0.75，信号强度接近高 α 区间
- canary metrics（token_entropy、ece）对 downstream（distinct_1/2/3）的因果关系在多数方法下一致显著，mauve 对因果信号较弱（仅 naive_xcorr + threshold_onset 通过）

**Conclusion: success** — fp32 下 α=0.50 不再是 step function 下方的"安全区"，而是已产生强因果信号。这将 PermG step function 的有效下界从之前 fp16 估计的 ~0.50 下移，需结合 s42/s44 的结果进一步确认 boundary 的精确位置。

---
