# ssh fewnerd n32 unified recompute v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewnerd_n32_unified_recompute_v2_20260522T105810_result.json`
- **Structured JSON:** [`b66bc5ad6fcd23038ea6.json`](../../sessions/b6/b66bc5ad6fcd23038ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇总：

---

## FewNERD N=32 Unified Baseline Recompute

**数据来源（均为 gold-non-empty 过滤后，recompute_alpha_crit_unified.py v4 strict MV）：**

### N=8 (3 seeds)
| Seed | Dir | greedy_f1 | mv_strict_f1 | Δ_own |
|------|-----|-----------|-------------|-------|
| 42 | `fewnerd_mf4v2_seed42_v4` | 0.7909 | 0.7583 | -3.27pp |
| 123 | `fewnerd_mf4v2_seed123_v3` | 0.7911 | 0.7648 | -2.63pp |
| 456 | `fewnerd_mf4v2_seed456_v3` | 0.7910 | 0.7686 | -2.24pp |
| **Mean** | | **0.7910** | **0.7639** | **-2.71pp** |

### N=32 (seed42)
| | 值 | 来源 |
|---|---|---|
| N=8 unified greedy F1 | **0.7909** | `fewnerd_mf4v2_seed42_v4`, recompute gold-non-empty |
| N=32 own greedy F1 | 0.7914 | `fewnerd_n32_seed42`, recompute gold-non-empty |
| N=32 MV strict F1 | **0.7818** | `fewnerd_n32_seed42`, recompute gold-non-empty |
| N=32 Δ (vs own greedy 0.7914) | **-0.96pp** | 0.7818 - 0.7914 |
| N=32 Δ (vs unified N=8 greedy 0.7909) | **-0.91pp** | 0.7818 - 0.7909 |

### 收敛趋势
```
N=8  Δ = -2.74pp (paper, 3-seed avg)
N=16 Δ = -1.65pp (paper, 3-seed avg)
N=32 Δ = -0.91pp (unified, single seed)
```

N 每翻倍，MV 负 Δ 大约减半，趋势收敛明朗。

### 注意事项
- N=32 的 own greedy (0.7914) 略高于 N=8 greedy (0.7909)，说明 N=32 实验使用了不同（稍好的）checkpoint，这也是统一 baseline 的意义所在
- N=16 seed42 实验 (`fewnerd_7b_n16_seed42`) 的 greedy_f1 = 0.7983，明显偏高，与 N=8 实验不同模型体系；seed123/456 的 N=16 greedy 在 0.7909-0.7916 范围，更一致
- N=32 只有 1 个 seed，无法算标准差

---
