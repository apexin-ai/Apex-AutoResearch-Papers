# analysis exp 010 convergence divergence bridge

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-010-convergence-divergence-bridge_20260519T150134_result.json`
- **Structured JSON:** [`16da70842ecf2733b48c.json`](../../sessions/16/16da70842ecf2733b48c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-010 完成。核心结果：

**A. Aggregate Convergence** — Cross-arch std 单调下降 5 倍：
| Variant | Attn ratio | Cross-arch σ |
|---------|-----------|-------------|
| pure | 0 | 0.0240 |
| h24-1 | 1/25 | 0.0162 |
| h12-1 | 1/13 | 0.0136 |
| h6-1 | 1/7 | 0.0061 |
| h3-1 | 1/4 | 0.0049 |

**B. Per-example Divergence** — Jaccard 在所有 ratio 上保持极低且平坦：
- J_helped: 0.092–0.100（~10% overlap）
- J_hurt: 0.081–0.099（~9% overlap）
- Net asymmetry 反而随 ratio 递增（0.013 → 0.040）

**C. Co-evolution** — Spearman 方向正确但 n=4/5 不足以达到统计显著：
- 5-point: std vs J_helped r=−0.70 (p=0.23), std vs J_hurt r=−0.80 (p=0.13)

**关键发现**：比 "co-evolution" 更强的是 **paradoxical coexistence**——aggregate gap 关闭了 80%（σ 从 0.024→0.005），但 per-example Jaccard 始终 ~0.10，说明三个架构在每个 ratio 上都帮助/伤害了几乎完全不同的 sample 集合。Net asymmetry 递增意味着架构之间的 net effect 方向差异随 attention 增多而加大（HGRN2 一直是净正效应，GDN/RetNet 一直是净负效应）。

输出文件：
- CSV: `analysis/exp010_bridge_results.csv`
- JSON: `analysis/exp010_bridge_summary.json`

---
