# analysis exp 057 nve verification

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_057_nve_verification_20260524T015018_result.json`
- **Structured JSON:** [`53e9156d1174eba98f25.json`](../../sessions/53/53e9156d1174eba98f25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整验证结果。

---

## NVE 验证结果

### 1. NVE 精确定义（论文原文）

**methodology.tex:38:**
> $\text{NVE}_t = (v/e)_{\text{config},t} \;/\; (v/e)_{\text{baseline},t}$

其中 $v/e$ = critic mean imagined value / mean evaluation return。

**appendix.tex:267 (normalization convention):**
> Walker NVE is normalized against the 4-seed mean baseline (seeds 1–4, each run to 505K+ steps).

### 2. exp_057 在 115K 的 baseline ve_ratio

**exp_009a (seed 2) 实测值 @115K:**
- eval_return = 804.79, value_mean = 574.93
- **ve_ratio = 0.7144**

**4-seed mean baseline @105K** (论文 Table baseline_seeds):
| Seed | ve@105K |
|------|---------|
| s1 | 0.656 |
| s2 | 0.742 |
| s3 | 0.664 |
| s4 | 0.624 |
| **Mean** | **0.6715** |

@115K 各 seed 的 ve 继续上升（converging toward 0.69-0.72），4-seed mean @115K ≈ **0.68**（保守估计）。

### 3. exp_057 精确 NVE

exp_057 @115K: `civo/ve_ratio = 1.2826`（已通过 value_mean=40.47 / eval_return=31.56 = 1.283 验证）

| Baseline | Baseline ve@115K | NVE | 判定 |
|----------|-----------------|-----|------|
| exp_009a (same seed 2) | 0.7144 | **1.795** | > 1.5x |
| exp_001 s1 only (@105K) | 0.656 | **1.955** | > 1.5x |
| 4-seed mean (estimated @115K) | ~0.68 | **~1.89** | > 1.5x |

### 4. 判断

**NVE > 1.5x 确认。** 无论用哪种 baseline 归一化方式，exp_057 在 115K 的 NVE 都在 **1.79–1.96** 范围，显著超过 1.5x 阈值。Registry 中 `nve_classification: "no_civo"` **不准确**。

Reviewer 的估算（baseline ≈ 0.65, NVE ≈ 1.97）与 exp_001 s1 baseline 吻合（0.656 → NVE = 1.955）。

### 5. 全部 3 个 Walker frozen seeds NVE 汇总

| Seed | 实验 | ve_ratio peak | Peak step | Baseline ve (同步) | NVE peak | > 1.5x? | 最终状态 |
|------|------|---------------|-----------|-------------------|----------|---------|---------|
| s0 | exp_042 | — | — | — | **0.194** (registry) | No | Clean |
| s1 | exp_047 | 1.099@75K | 95K (NVE peak) | 0.632 (s1@95K) | **1.71** | **Yes** | Transient → 0.56 |
| s2 | exp_057 | 1.283@115K | 115K | 0.7144 (s2@115K) | **1.795** | **Yes** | Transient → 0.177 |

此外 exp_057 在 35K–65K 区间也持续 > 1.5x（使用 same-seed baseline）：
- 35K: NVE = 0.495/0.306 = 1.62
- 45K: NVE = 0.615/0.363 = 1.69
- 55K: NVE = 0.747/0.475 = 1.57
- 65K: NVE = 0.715/0.474 = 1.51

### 6. 需要调整的论文措辞

**问题 1 — analysis.tex:8:**
> "at most a transient spike (1/3 frozen Walker, 0/2 frozen Cheetah)"

应改为 **2/3 frozen Walker**。exp_047 (s1, NVE=1.71) 和 exp_057 (s2, NVE=1.80) 都超过 1.5x。

**问题 2 — Registry `nve_classification`:**
exp_057 的 `nve_classification: "no_civo"` 应改为 `"transient_civo"` 或至少标注 NVE > 1.5x。

**问题 3 — exp_057 registry note:**
> "s0=0.19, s1=1.71, s2=1.28 — all clean/transient"

混淆了 NVE（s0, s1）和 raw ve_ratio（s2）。s2 的 NVE 实际为 ~1.80，不是 1.28。应统一为 NVE 值：**s0=0.19, s1=1.71, s2=1.80**。

**问题 4 — 论文 n=29 NVE 分析:**
如果 frozen 实验被纳入 n=29 数据集且 exp_057 被标为 negative，AUROC/accuracy 数值需重新计算。

---
