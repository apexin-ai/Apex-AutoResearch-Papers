# analysis alpha sweep a050 s44 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_s44_fp32_20260519T094823_result.json`
- **Structured JSON:** [`af4785e7d6ae9be3d50c.json`](../../sessions/af/af4785e7d6ae9be3d50c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 分析总结：alpha_sweep_a050_s44_fp32

**模型/配置**: Pythia-410m, α=0.50, seed=44, fp32, 10 generations, wikitext103_5k

### 关键 metrics（gen0 → gen10）

| 指标 | gen0 | gen10 | drift% |
|---|---|---|---|
| token_entropy | 3.234 | 2.697 | **-16.61%** |
| ece | 0.0108 | 0.0874 | **+709.03%** |
| perplexity | 26.95 | 31.42 | +16.61% |
| distinct_1 | 0.0915 | 0.066 | -27.93% |
| distinct_2 | 0.500 | 0.327 | -34.64% |
| distinct_3 | 0.829 | 0.575 | -30.60% |
| effective_rank | 46.6 | 58.3 | +25.06% |
| mauve | 0.0275 | 0.0237 | -13.88% |

### 因果检验结果

| 方法 | 结果 |
|---|---|
| naive_xcorr_fwd | **8/8** |
| diff_xcorr_fwd | **8/8** |
| threshold_onset_fwd | **8/8** |
| perm_granger_fwd | **6/8** |
| perm_granger_rev | 0/8 |
| ty_granger_fwd | 4/8（C003: α≤0.50 下 TY 不可靠，不作为支撑证据） |
| consensus_k4 | **6/8** |
| mmct_wpair_fwd | **0.75** |

### 结论：**success**

α=0.50 fp32 s44 结果出乎意料：PermG = 6/8，consensus = 6/8，MMCT = 0.75。这表明在 fp32 精度下，α=0.50 boundary regime **已跨过 step function 阈值**，canary lead-lag 信号清晰可检测。与 boundary regime 下"PermG 可能为 0"的保守预期不同，s44 显示该区域因果信号实际上是稳健的。Reverse PermG = 0/8 确认方向性正确（entropy leads diversity，非反向）。

这对 step function 边界定位有重要意义：fp32 下 α=0.50 不再是"不确定区域"，而是可检测区域的下界。需要结合 s42/s43 的结果确认 3-seed 一致性。

---
