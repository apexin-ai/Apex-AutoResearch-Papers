# ssh pretrained fewnerd s42 mv

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pretrained_fewnerd_s42_mv_20260521T182914_result.json`
- **Structured JSON:** [`0eaf07b22c380530dfb2.json`](../../sessions/0e/0eaf07b22c380530dfb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果（gold-nonempty instances, n=32565）：

| 指标 | Pretrained (本次) | Finetuned 3-epoch (参考) |
|------|-------------------|--------------------------|
| greedy_f1 | **0.5384** | ~0.789 |
| mv_strict_f1 (>N/2) | **0.5788** | ~0.766 |
| mv_incl_f1 (≥N/2) | **0.5667** | — |
| oracle_f1 | **0.6508** | — |
| Δ_SC strict | **+4.03pp** | **-2.74pp** |
| degeneracy | **12.2%** | ~13% |
| α_crit_eff (strict) | **0.3065** | — |

关键发现：
- **Pretrained MV Δ = +4.03pp（正向提升）** vs Finetuned MV Δ = -2.74pp（负向退化），方向完全相反。MV 在 pretrained 模型上显著有效。
- Degeneracy 率几乎相同（12.2% vs ~13%），说明故事不是单纯的 "finetuning 增加了 degeneracy"，而更可能是 finetuning 改变了错误的相关性结构（degenerate samples 的 quality 或 diversity 性质不同）。

注意：report.json 中 greedy_f1=0.5121、oracle_f1=0.6175 包含了 5083 个 gold-empty 实例，recompute 脚本过滤了这些。需确认与 finetuned 对比时口径一致。

---
