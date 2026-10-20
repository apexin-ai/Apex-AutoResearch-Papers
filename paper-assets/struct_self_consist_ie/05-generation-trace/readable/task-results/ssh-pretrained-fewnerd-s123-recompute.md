# ssh pretrained fewnerd s123 recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pretrained_fewnerd_s123_recompute_20260521T182610_result.json`
- **Structured JSON:** [`38a284676b2da953778a.json`](../../sessions/38/38a284676b2da953778a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Recompute 完成。结果汇总：

### Pretrained Qwen2.5-7B (FewNERD, N=8, T=1.0, seed=123)

| 指标 | Pretrained | Finetuned 3-epoch | 对比 |
|------|-----------|-------------------|------|
| greedy_f1 | **0.5381** | 0.664 | -12.59pp |
| mv_strict_f1 (>N/2) | **0.5783** | — | — |
| mv_incl_f1 (≥N/2) | **0.5658** | — | — |
| oracle_f1 | **0.6520** | — | — |
| Δ_SC strict | **+4.02pp** | -2.74pp | pretrained SC gain 大幅优于 finetuned |
| degeneracy | **11.2%** | ~13% | pretrained 略低 |
| α_crit_eff (strict) | **0.4580** | — | — |
| α_crit_eff (incl) | **0.4442** | — | — |
| gold-nonempty | 32,565 / 37,648 | — | — |

关键发现：
- Pretrained 模型 greedy_f1 比 finetuned 低约 12.6pp，但 **SC 增益 +4.02pp 远大于 finetuned 的 -2.74pp**
- degeneracy 11.2%，比 finetuned (~13%) 更低——pretrained 模型采样多样性更好
- α_crit_eff ≈ 0.458，MV 在 pretrained 上的信号显著

---
