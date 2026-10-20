# analysis exp 009b 008d walker s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009b_008d_walker_s2_20260514T184904_result.json`
- **Structured JSON:** [`d9a428064ce3c34b3a2b.json`](../../sessions/d9/d9a428064ce3c34b3a2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Conclusion: **success** (collapse NOT reproduced).

## 结果摘要

**exp_009b_008d_walker_s2 — Delusional critic collapse 未复现**

| Step | eval_return | value_mean | v/e | norm v/e |
|------|-------------|------------|-----|----------|
| 25K  | 141.12 | 25.14 | 17.8% | **2.05x** |
| 45K  | 141.04 | 75.59 | 53.6% | **1.62x** |
| 55K  | 172.33 | 98.28 | 57.0% | 1.41x |
| 65K  | 209.16 | 110.91 | 53.0% | 0.94x |
| 85K  | 236.49 | 83.86 | 35.5% | 0.51x |
| 105K | **267.93** | 67.27 | **25.1%** | **0.38x** |

**与 008d seed 1 完全相反的轨迹：**
- **008d (seed 1)**: v/e 加速 15.5%→166.6%, eval 崩塌 167→83 → collapse confirmed
- **009b (seed 2)**: v/e 峰值 57% 后自修正至 25.1%, eval 上升至 268 → **no collapse**

**与 009c (no dt_embed, seed 2) 的讽刺性对比：**
- 009c (无 dt_embedding): eval 148@105K（持续下降）
- 009b (有 dt_embedding): eval 268@105K（上升趋势）
- Seed 2 中**有** dt_embedding 的反而表现更好，与 C2 叙事完全相反

**对论文的影响：** trained dt_embedding → delusional critic 的因果链在 seed 间不稳健。008d 的 collapse 可能是 seed-specific 现象而非系统性因果关系。

---
