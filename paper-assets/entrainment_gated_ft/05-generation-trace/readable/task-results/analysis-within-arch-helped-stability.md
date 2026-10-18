# analysis within arch helped stability

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_within-arch-helped-stability_20260520T024536_result.json`
- **Structured JSON:** [`dcb0d380d525221454d6.json`](../../sessions/dc/dcb0d380d525221454d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到本地和服务器。核心发现：

**Within-architecture Jaccard ≈ 0.31–0.35**，显著高于跨架构的 ~0.10，但仍然远低于 1.0。

| 架构 | 平均 helped J | 平均 hurt J | 特点 |
|------|-------------|------------|------|
| GatedDeltaNet | 0.338 | 0.319 | 各 ratio 间最均匀 |
| RetNet | 0.333 | 0.321 | 与 GDN 类似 |
| HGRN2 | 0.373 | 0.291 | helped 最高，hurt 最低 |

关键观察：
- **Within-arch J (~0.33) >> Cross-arch J (~0.10)**：同一架构内不同 attention ratio 的 helped/hurt set 重叠度是跨架构的 3 倍多，但仍有 ~65% 的 examples 是 ratio-specific 的
- **相邻 ratio 没有更高 overlap**：h24-1 vs h12-1 的 J 和 h24-1 vs h3-1 的 J 差异很小（e.g., GDN helped: 0.345 vs 0.311），说明 helped/hurt set 不随 attention 量单调变化
- **HGRN2 的 helped set 更稳定**（J ≈ 0.37），但 hurt set 反而最不稳定（J ≈ 0.29）——说明 HGRN2 受 attention 帮助的 examples 比较一致，但受损的 examples 更 ratio-specific

---
