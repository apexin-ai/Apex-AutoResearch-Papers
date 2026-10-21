# ssh e1v2 signal routing redesign

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_e1v2-signal-routing-redesign_20260520T105527_result.json`
- **Structured JSON:** [`56ea82ae578dbc47f3eb.json`](../../sessions/56/56ea82ae578dbc47f3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## E1v2 结果

**RF (LOO) 精度 68.8%，比 E1 的 56.2% 提升 12.6pp — 去掉 oracle 特征反而更好。**

| Model | LOO Acc | 5-fold CV | Router dF1 | vs Always-LP |
|-------|---------|-----------|------------|-------------|
| GradientBoosting | 56.2% (9/16) | 55.0% ± 17.9% | +0.36pp | +0.21pp better |
| **RandomForest** | **68.8% (11/16)** | **68.3% ± 21.3%** | **+0.37pp** | +0.22pp better |

### E1 vs E1v2

| | E1 (RF, 12 features incl. oracle) | E1v2 (RF, 8 deploy-only features) |
|---|---|---|
| LOO Accuracy | 56.2% | **68.8%** |
| Router dF1 | +0.39pp | +0.37pp |
| 可部署 | ✗ (需 ground truth) | ✓ |

### Top features (RF)
1. **model_size×degeneracy** (0.245) — 交互特征是最重要的
2. degeneracy_rate (0.196)
3. regime×degeneracy (0.142)
4. vc_variance (0.099)
5. model_size×regime (0.087)

### Regime patterns
- **FT**: lp_selection (5) > theta2n (3) > none (2)
- **ZS**: 多数 none — SC 在 zero-shot 下收益小
- **FS**: 分散，无主导方法

### 局限
- 7/16 configs 有原始 samples.jsonl 可计算 lp_variance/vc_variance，其余 9 个用 regime 均值填充
- Router dF1 略低于 E1 (-0.02pp)，但在无 oracle 条件下这是预期内的

产出已保存到 `artifacts/e1v2_signal_routing/` 并注册。

---
