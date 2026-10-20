# analysis alpha sweep a035 s42 fp32 mmct

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a035_s42_fp32_mmct_20260519T190341_result.json`
- **Structured JSON:** [`5ac69e8c2309c320e755.json`](../../sessions/5a/5ac69e8c2309c320e755.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D105 MMCT 5-Method Analysis: alpha_sweep_a035_s42_fp32

### 实验配置
- Model: Pythia-410M, seed=42, α=0.35, fp32, WikiText-103
- Generations: 11 (gen_0–gen_10), EXIT_CODE=0
- Server: westd-17855

---

### 方法级汇总

| Method | Sig/Total |
|---|---|
| Naive xcorr | 8/8 |
| Diff xcorr (FDR) | 4/8 |
| Threshold onset | 8/8 |
| **PermG fwd (FDR)** | **0/8** |
| PermG rev (FDR) | 0/8 |
| TY Granger | 4/8 |
| **K≥4 consensus** | **2/8** |
| K≥3 consensus | 6/8 |
| MMCT detection rate | 0.25 |

---

### Pair 级详情

| Pair | Naive | DiffX | Thresh | PermG | TY | Votes |
|---|---|---|---|---|---|---|
| token_entropy→distinct_1 | Y | Y | Y(c=1→d=2) | n (p=0.054) | Y (χ²=80.8) | **4** |
| token_entropy→distinct_2 | Y | Y | Y(c=1→d=2) | n (p=0.069) | n | 3 |
| token_entropy→distinct_3 | Y | n | Y(c=1→d=2) | n (p=0.056) | n | 2 |
| token_entropy→mauve | Y | n | Y(c=1→d=8) | n (p=0.130) | Y (χ²=982.6, df=1) | 3 |
| ece→distinct_1 | Y | Y | Y(c=1→d=2) | n (p=0.054) | Y | **4** |
| ece→distinct_2 | Y | Y | Y(c=1→d=2) | n (p=0.062) | n | 3 |
| ece→distinct_3 | Y | n | Y(c=1→d=2) | n (p=0.060) | n | 2 |
| ece→mauve | Y | n | Y(c=1→d=8) | n (p=0.131) | Y (d_max=2, df=1) | 3 |

PermG fwd p-values 全部 0.054–0.131，无一达到 FDR 显著。token_entropy→mauve 的 TY chi²=982.6 但 df_resid=1（C003 约束下不可用）。

---

### Drift 表 (gen0→gen10)

| Metric | gen0 | gen10 | Drift% |
|---|---|---|---|
| token_entropy | 3.234 | 2.635 | **-18.53%** |
| ece | 0.0108 | 0.0812 | **+651.26%** |
| perplexity | 26.95 | 26.61 | -1.27% |
| distinct_1 | 0.098 | 0.0623 | **-36.38%** |
| distinct_2 | 0.514 | 0.260 | **-49.45%** |
| distinct_3 | 0.813 | 0.406 | **-50.04%** |
| effective_rank | 46.61 | 56.96 | +22.21% |
| mauve | 0.0311 | 0.0256 | -17.78% |

---

### Onset Boundary 对比

| α | PermG fwd | K≥4 | K≥3 | 判定 |
|---|---|---|---|---|
| 0.05 | 0/8 | 0/8 | — | blind zone |
| 0.10 | 0/8 | 0/8–2/8 | — | blind zone |
| 0.25 | 0/8 | 0/8 | — | blind zone |
| **0.35** | **0/8** | **2/8** | **6/8** | **blind zone** |
| 0.40 | 0/8 | 1/8 | 6/8 | blind zone |
| **0.50** | **6/8** | **6/8** | — | **detected** |
| 0.60 | 3/8 | 7/8 | — | detected (非单调) |
| 0.75 | 6/8 | 6/8 | — | detected |

---

### 结论

**PermG=0/8 确认 α=0.35 仍在 blind zone 内。** 结合 α=0.40 (PermG=0/8) 和 α=0.50 (PermG=6/8)，onset boundary 收窄至 **[0.40, 0.50]**。

值得注意：α=0.35 的 diversity drift 幅度很大（d1=-36.4%, d2=-49.5%, d3=-50.0%），与 α=0.50 的 drift（d1=-29.2%）相当甚至更大，但 PermG 完全无信号。这进一步确认 blind zone 的核心特征——**diversity collapse 在进行，但 Granger 因果结构不可检测**。

PermG p-values 集中在 0.054–0.062 区间（6/8 pairs），处于 borderline 状态，暗示 α=0.35 可能接近 onset 下界但仍未越过。

Registry 已更新为 status=DONE, conclusion=success。

---
