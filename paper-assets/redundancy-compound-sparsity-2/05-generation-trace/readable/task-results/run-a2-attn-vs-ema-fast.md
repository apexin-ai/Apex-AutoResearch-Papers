# run a2 attn vs ema fast

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_a2_attn_vs_ema_fast_20260512T155234_result.json`
- **Structured JSON:** [`feeb4188ae400c108abe.json`](../../sessions/fe/feeb4188ae400c108abe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出就绪。

## A2 结果汇报

**Verdict: complementary** — EMA centroid similarity 与 attention score 捕获的是不同信号，二者互补。

### 关键数字

| 指标 | 值 |
|------|------|
| Mean Pearson r | **0.126** |
| Mean Spearman ρ | **-0.163** |
| \|相关性\| | 全部 < 0.5 |

### 分层模式

- **早期层 (0-4)**: 两个信号**负相关**，Layer 3 最强 (ρ=-0.45)。EMA 认为重要的位置，attention 反而不重视。
- **中间层 (5-40)**: Pearson 弱正 (~0.15)，Spearman 弱负 (~-0.15 到 -0.32)。Pearson/Spearman 方向不一致说明关系是非线性的。
- **尾部层 (41-47)**: Spearman 趋近 0（不显著），两个信号几乎正交。

### 解读

Pearson 微正 + Spearman 负 = 两个信号在极端值上有某种正相关，但在 position ranking 上是反向的。这意味着 EMA 和 attention 提供了**互补的 eviction 信号**，结合两者有可能比单独使用任何一个做更好的 KV cache eviction。

### 产出文件
- `/root/carc/results/a2_attn_vs_ema.json`
- `/root/carc/figures/a2_per_layer_correlation.png`
- `/root/carc/figures/a2_per_layer_correlation.pdf`
- `/root/carc/figures/a2_scatter_layers.png`

---
