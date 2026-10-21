# analysis penalty sensitivity recompute

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_penalty-sensitivity-recompute_20260519T190209_result.json`
- **Structured JSON:** [`c48982919f489c4f76ee.json`](../../sessions/c4/c48982919f489c4f76ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P=100 全部验证通过。完整结果：

### Penalty Sensitivity Table (245 episodes, B=10,000 bootstrap)

| P | DAF(%) | 95% CI | Δ_full | Δ_nd | r | p-value | D/I/N |
|---|--------|--------|--------|------|---|---------|-------|
| 0 | 7.4 | [−39.4, 82.5] | 3.07 | 2.84 | −0.47 | 1.45e-01 | 36/5/204 |
| 1 | 14.8 | [−28.6, 89.6] | 3.33 | 2.84 | −0.44 | 1.78e-01 | 86/9/150 |
| 5 | 35.4 | [−1.8, 92.7] | 4.39 | 2.84 | −0.29 | 3.82e-01 | 86/9/150 |
| 10 | 50.4 | [18.5, 93.3] | 5.72 | 2.84 | −0.08 | 8.13e-01 | 86/9/150 |
| 25 | 70.7 | [48.0, 96.3] | 9.70 | 2.84 | 0.51 | 1.08e-01 | 86/9/150 |
| 50 | 82.6 | [67.2, 98.2] | 16.33 | 2.84 | 0.86 | 5.89e-04 | 86/9/150 |
| **100** | **90.4** | **[81.1, 99.0]** | **29.60** | **2.84** | **0.97** | **8.09e-07** | **86/9/150** |
| 200 | 94.9 | [89.9, 99.5] | 56.13 | 2.84 | 0.99 | 1.07e-09 | 86/9/150 |
| 500 | 97.9 | [95.7, 99.8] | 135.72 | 2.84 | 1.00 | 2.11e-13 | 86/9/150 |

### P=100 验证：全部 PASS
- DAF=90.4% ✓, r=0.97 ✓, Δ_full=29.60 ✓, D/I/N=86/9/150 ✓, Δ_nd=2.84 ✓

### 数据说明
- **数据文件**: `results/baseline_245eps/episode_details.jsonl`，筛选 `condition=="always-deterministic"` 得 245 episodes
- **格式**: 每行含 `internal_final`/`det_final`（两种策略的终端分数），death 表现为 score=−100
- **统计**: 105 次 internal death, 40 次 det death, 135 episodes both alive
- **D/I/N 在 P≥1 时不变**（86/9/150），因为 P≥1 的 penalty 不改变非死亡 episodes 的相对排序；P=0 时变为 36/5/204（死亡 episodes 的 raw score 都是 0，大量变为 tie）

### 产出文件
- 脚本: `scripts/recompute_penalty_sensitivity.py`
- JSON 结果: `results/penalty_sensitivity_recomputed.json`

---
