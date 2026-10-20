# code exp 016 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_016_v2_20260514T152644_result.json`
- **Structured JSON:** [`b398ac4996c667b5c1ed.json`](../../sessions/b3/b398ac4996c667b5c1ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-016 v2 完成。结果汇总：

### NER Conditional (529 inst, N=32)
| 指标 | 值 |
|---|---|
| Signal vs F1 最强 | SJ ρ=0.4412 |
| 最佳线性组合 | SJ+VC α=0.55, ρ=0.4552 |
| Ensemble AUROC | 0.714 (best single: SJ 0.717) |
| Selection F1 | logprob 0.6505 > ensemble 0.6475 > sj 0.6471 > **greedy 0.6442** > vc 0.6347 |

### RE Conditional (397 inst, N=16)
| 指标 | 值 |
|---|---|
| Signal vs F1 最强 | VC ρ=0.3849 |
| 最佳线性组合 | logprob+VC α=0.25, ρ=0.3936 |
| Ensemble AUROC | 0.692 (best single: VC 0.702) |
| Selection F1 | **ensemble 0.4227** > logprob 0.4097 > **greedy 0.4030** > sj 0.3973 |

### RE Full (551 inst, N=16) — 亮点
| Ensemble AUROC | **0.861** (single best: VC 0.825) |

关键发现：
- NER: N=32 后 SJ 成为最强单信号（v1 中 VC 最强），SJ+VC 组合 ρ=0.50
- RE: VC 主导，ensemble AUROC 在 full 配置下达到 0.861
- Selection: logprob_best 在 NER 上最强，ensemble_best 在 RE 上最强（+0.020 over greedy）
- 输出路径: `output/exp_016_v2/`（correlation_matrix.json, linear_combo_grid.json, logistic_ensemble.json, selection_f1_comparison.json, summary.csv）

---
