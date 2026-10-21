# analysis transformer baseline perexample

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transformer-baseline-perexample_20260520T011942_result.json`
- **Structured JSON:** [`3631331ddcdf4a030b4c.json`](../../sessions/36/3631331ddcdf4a030b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存至 `/root/entrainment_gated_ft/transformer_baseline_analysis.json`。

## 核心发现

**Transformer accuracy: 48.09%**（反而低于所有 recurrent/hybrid 模型）

### h3-1 是否向 Transformer 靠拢？

| 架构 | pure J(vs Trans) | h3-1 J(vs Trans) | delta |
|------|:-:|:-:|:-:|
| GDN | 0.6447 | 0.6494 | +0.0047 |
| RetNet | 0.6789 | 0.6941 | **+0.0152** |
| HGRN2 | 0.6718 | 0.7008 | **+0.0290** |

**三个架构的 h3-1 correct set 均比 pure 更接近 Transformer**，效应强度 HGRN2 > RetNet > GDN。Agreement rate 同样呈现一致趋势（HGRN2-h3-1 达到最高的 0.825）。

### 解读

- Attention 层的加入确实使 hybrid 的 per-example 行为向 Transformer 收敛，支持 "attention entrainment" 假设
- HGRN2 对 attention 最敏感（delta 最大），GDN 最不敏感（可能因为 GDN 的 gating 机制本身已部分模拟了 attention 的功能）
- 值得注意的是 Transformer 本身 accuracy 最低，说明 hybrid 不是简单"变弱到和 Transformer 一样"，而是在保持/提升 accuracy 的同时 correct set 组成趋同

---
