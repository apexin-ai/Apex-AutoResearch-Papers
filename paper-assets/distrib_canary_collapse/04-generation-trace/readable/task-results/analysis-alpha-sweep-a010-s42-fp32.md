# analysis alpha sweep a010 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a010_s42_fp32_20260519T093334_result.json`
- **Structured JSON:** [`6c4ec12c0dbc6befe230.json`](../../sessions/6c/6c4ec12c0dbc6befe230.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已获取。

## alpha_sweep_a010_s42_fp32 分析结果

### 核心指标
- token_entropy_drift: **-4.59%**
- distinct_1_drift: **-23.80%**
- distinct_2_drift: **-27.15%**
- distinct_3_drift: **-19.36%**
- perplexity_drift: **-18.94%**
- perm_granger_fwd: **0/8**
- perm_granger_rev: **0/8**
- ty_granger_fwd: **3/8**
- threshold_onset_fwd: **5/8**
- consensus_k4: **2/8**
- MMCT wpair: **2/8 (detection_rate=0.25)**

### 与 s43 对比

| 指标 | s42 fp32 | s43 fp32 | 差异 |
|------|----------|----------|------|
| token_entropy_drift | -4.59% | -4.49% | -0.10pp |
| distinct_1_drift | -23.80% | -22.08% | -1.72pp |
| distinct_2_drift | -27.15% | -23.47% | -3.68pp |
| distinct_3_drift | -19.36% | -16.39% | -2.97pp |
| perplexity_drift | -18.94% | -18.04% | -0.90pp |
| perm_granger_fwd | 0/8 | 0/8 | **一致** |
| perm_granger_rev | 0/8 | 0/8 | **一致** |
| ty_granger_fwd | 3/8 | 6/8 | 跨seed不稳定(符合C003) |
| threshold_onset_fwd | 5/8 | 4/8 | 近似一致 |
| consensus_k4 | 2/8 | 0/8 | 均极低 |

### 结论

- **blind_zone 跨 seed 稳定：是。** PermG 两个 seed 均为 0/8，精度无关（fp32 与 bf16 结果一致）。consensus_k4 两个 seed 均极低（0-2/8），D075 claim 成立。
- **drift 量级一致：** d1 drift s42=-23.80% vs s43=-22.08%，同量级，s42 略深但在合理 seed 波动范围内。所有 diversity drift 一致显示 α=0.10 下退化显著但因果检测失败。
- **TY Granger 跨 seed 不稳定（3/8 vs 6/8）**，再次确认 C003 约束——TY 在低 α 下不可作为支撑证据。
- **异常：无。** EXIT_CODE=0，gen_0 到 gen_10 全部完成，无 NaN/OOM。
- **W&B：** list_wandb_runs API 参数异常，未能查询。本地结果完整。
- **建议 conclusion: success** — 实验达成预期目的，跨 seed 验证了 α=0.10 为 blind zone。

---
