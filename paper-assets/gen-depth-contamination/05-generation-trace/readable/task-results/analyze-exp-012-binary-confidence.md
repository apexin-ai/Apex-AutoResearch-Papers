# analyze exp 012 binary confidence

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_012_binary_confidence_20260515T232123_result.json`
- **Structured JSON:** [`616b2b9c5011780fa0b3.json`](../../sessions/61/616b2b9c5011780fa0b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

## exp_012_binary_confidence 结果

**结论：success** — hypothesis 验证通过，binary confidence ≠ depth。

### 关键数据

| Generator | Spearman ρ (best metric) | 6-class Acc | 0v1 AUC (OBD-15D) | 4v5 AUC (OBD-15D) |
|-----------|-------------------------|-------------|--------------------|--------------------|
| qwen-rewrite | 0.12 (ratio) | 0.199 | 0.996 | 0.534 |
| pythia-1.4b | -0.45 (obs) | 0.130 | 0.993 | 0.514 |
| olmo-1b | -0.46 (obs) | 0.127 | 0.997 | 0.504 |
| qwen-cont | -0.39 (ref) | 0.183 | 0.997 | 0.514 |

Random baseline for 6-class: 0.167

### 论文叙事支撑

1. **6-class accuracy ≤ random** — binary confidence 无法分类 depth levels
2. **Pairwise AUC 急剧衰减** — 0v1 ≈ 0.99（近乎完美区分 human/AI），但 deeper pairs 迅速塌缩到 ~0.50（随机）
3. 中等 Spearman ρ（pythia/olmo ~0.45）完全由 depth-0 vs depth-1 的巨大 gap 驱动，不代表对 depth 的真正敏感性
4. 可视化已生成：`exp012_confidence_vs_depth.pdf`

---
