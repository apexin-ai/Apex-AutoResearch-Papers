# analysis exp065 dt emb cosine

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp065-dt-emb-cosine_20260524T204916_result.json`
- **Structured JSON:** [`e08ec6a70b955d24657d.json`](../../sessions/e0/e08ec6a70b955d24657d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_065 完成。

**结果汇总**:

| 实验 | cos(dt1, dt2) | 变化趋势 |
|------|--------------|----------|
| exp_008d_s3 (trained, walker) | -0.87 → -0.70 | 25k 已强负相关，75k 略减 |
| exp_010b_s0 (trained, cheetah) | -0.90 → -0.84 | 同上 |
| exp_059_s5 (trained, walker) | -0.94 → -0.86 | 同上 |
| exp_057_s2 (frozen, walker) | -0.15 恒定 | 5个 checkpoint 完全一致 |
| exp_058_s1 (frozen, cheetah) | +0.07 恒定 | 5个 checkpoint 完全一致 |

**结论**: cosine sim 强负 → dt_embedding 学到了显著不同的表征（dt=1 和 dt=2 在嵌入空间中近似反方向）。CIVO 来自 dt=2 表征本身的偏差，而非微小差异被放大。frozen 对照组确认冻结有效。

产出文件（服务器 `logdir/exp_065_dt_emb_cosine/`）:
- `results.json` — 完整数值结果
- `cosine_sim_evolution.png` — 训练过程演化图
- `pairwise_heatmap.png` — 8×8 dt 全对 cosine 矩阵

---
