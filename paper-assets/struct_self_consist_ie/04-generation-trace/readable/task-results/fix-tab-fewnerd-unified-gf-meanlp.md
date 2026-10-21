# fix tab fewnerd unified gf meanlp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tab_fewnerd_unified_gf_meanlp_20260518T042835_result.json`
- **Structured JSON:** [`5ab202fe8b1815d72d5f.json`](../../sessions/5a/5ab202fe8b1815d72d5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All computations and code updates are done. Here's the report:

## 重算结果

### Few-NERD mean_LP ρ (gold-filtered n=32565)
- max_LP ρ (旧): 0.421 (验证通过: 0.420671)
- mean_LP ρ (新): **0.221**
- 其他指标不变 (greedy=0.749, headroom=12.4pp, degen=13.8%, LP Δ=+1.35pp)

### CoNLL gold-filtered 全套 (mean_LP)
| 指标 | 旧论文值 | 新 gf 值 | 差异 |
|------|---------|----------|------|
| n | 2756 | 2756 | 同 |
| greedy | .908 | .909 | +0.1pp |
| oracle | — | .948 | 新增 |
| headroom | 4.0pp | 3.97pp | -0.03pp |
| degen% | 47.4% | 59.2% | +11.8pp (F1-based定义) |
| LP ρ | .316 | .311 | -0.005 |
| LP Δ | n.s. | -1.07pp | 确认为负 |

### 三数据集完整新旧对比表
| Dataset | n | greedy | oracle | headroom | degen% | LP ρ | LP Δ |
|---------|---|--------|--------|----------|--------|------|------|
| SciERC (旧) | 551 | .614 | .752 | 13.8pp | 17.8% | .205 | +0.42pp |
| SciERC (新) | 529 | .644 | .776 | 13.2pp | 17.8% | .205 | +0.61pp |
| Few-NERD (旧) | 32565 | .748 | — | 12.4pp | 13.8% | .421 | +1.36pp |
| Few-NERD (新) | 32565 | .749 | .873 | 12.4pp | 13.8% | **.221** | +1.35pp |
| CoNLL (旧) | 2756 | .908 | — | 4.0pp | 47.4% | .316 | n.s. |
| CoNLL (新) | 2756 | .909 | .948 | 3.97pp | 59.2% | **.311** | **-1.07pp** |

### analyze_fewnerd_results.py 更新
- 已更新: **YES**
- 更新内容:
  - `SCIERC_REF`: 更新为 gold-filtered n=529, greedy=0.644, oracle=0.776, headroom=13.2, lp_rho=0.205, lp_delta=0.61
  - `CONLL_REF`: 新增，n=2756, greedy=0.9088, oracle=0.9485, headroom=3.97, degen=59.2, lp_rho=0.311, lp_delta=-1.07
  - LP 信号的 Spearman ρ 计算改为 `instance_mean_lp`（mean_LP 定义），其他信号保持 max
  - 跨数据集对比表新增 CoNLL 行
  - 两处 source comment 标注日期 2026-05-18

**注意**: CoNLL degen% 从 47.4% 升至 59.2%，差异源于定义不同（新值为 F1-based: 所有 N=8 sample F1 完全相同；旧值可能为 entity key_sets 一致性定义）。CoNLL LP Δ = -1.07pp，确认 LP selection 在该数据集上无正向效果。

---
