# analysis alpha sweep a070 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a070_s42_fp32_20260521T054959_result.json`
- **Structured JSON:** [`f11e239a12df50175d5d.json`](../../sessions/f1/f11e239a12df50175d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## alpha_sweep_a070_s42_fp32 — 5-method 分析结果

| 方法 | Forward | Reverse |
|------|---------|---------|
| PermG (FDR) | **5/8** | 0/8 |
| DiffXCorr (FDR) | 6/8 | 6/8 |
| ThresholdOnset (3σ) | 0/8 | — |
| TY Granger | 1/8 | — |

**K≥3 robust pairs: 3/8**
- `token_entropy→distinct_1` (naive, diff, ty)
- `ece→distinct_1` (naive, diff, perm)
- `ece→distinct_2` (naive, diff, perm)

**Drift**: ECE +1773%, perplexity +152%, distinct_1/2/3 -27~35%, token_entropy -29%, mauve flat (-0.7%)

**结论: success** — PermG 从 α=0.55-0.65 的 0/8 恢复到 α=0.70 的 5/8，确认 sync collapse dip 边界在 **[0.65, 0.70)**。更新后的 dip profile：

| α | PermG | 状态 |
|---|-------|------|
| 0.50 | 5/8 | detection |
| 0.55 | 0/8 | dip 开始 |
| 0.60 | 0/8 | dip |
| 0.65 | 0/8 | dip 结束 |
| **0.70** | **5/8** | **恢复** |
| 0.75 | 6/8 | detection |

Mauve pairs 在所有 α 下均无信号（drift 接近 0%），符合预期。

---
