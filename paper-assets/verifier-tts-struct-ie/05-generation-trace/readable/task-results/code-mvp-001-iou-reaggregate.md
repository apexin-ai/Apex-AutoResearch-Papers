# code mvp 001 iou reaggregate

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001-iou-reaggregate_20260511T184705_result.json`
- **Structured JSON:** [`c0343ee0f100d7d5b477.json`](../../sessions/c0/c0343ee0f100d7d5b477.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

聚合完成。结果如下：

## F1 矩阵 (micro_f1 × 100)

| N | greedy | exact_sc | iou_sc_tau03 | iou_sc_tau05 | iou_sc_tau07 | weighted_vote | oracle | random |
|---|--------|----------|-------------|-------------|-------------|---------------|--------|--------|
| 1 | 42.05 | — | — | — | — | — | — | — |
| 4 | — | 41.91±0.26 | 41.84±0.20 | 41.82±0.40 | 41.89±0.36 | 41.91±0.37 | 45.92±0.42 | 41.29±0.72 |
| 8 | — | 42.22±0.63 | 42.24±0.72 | 42.21±0.52 | 42.21±0.73 | 42.52±0.32 | 47.45±0.25 | 41.79±0.58 |
| 16 | — | 41.34±0.32 | 41.46±0.36 | 41.51±0.26 | 41.34±0.42 | 42.23±0.38 | 48.54±0.36 | 41.83±0.86 |

## Pass/Fail 判断

**FAIL** — iou_self_consistency@N≥8 未超过 greedy ≥ 1.0 F1 点。

- 最佳 IoU SC: N=8, tau=0.3 → 42.24 vs greedy 42.05 = **+0.19**（远不到 1.0）
- N=16 所有 tau 均低于 greedy（最高 41.51 vs 42.05）
- IoU SC 与 exact SC 几乎无差异（最大差 0.17），说明 span 重叠匹配在当前数据上帮助极小

## 关键发现

- exact SC 和 IoU SC 表现几乎相同：投票分裂的主因不是 "word embeddings" vs "word embedding" 这类 span 边界差异，而是候选间 entity 集合高度多样化
- Oracle 随 N 稳步增长（45.92→47.45→48.54），说明好答案存在于候选中，但当前 SC 选不出来
- weighted_vote@N=8 (42.52) 是最好的非 oracle 策略

## 产出

- 修改后的脚本: `/root/projects/verifier-tts-struct-ie/scripts/aggregate.py`
- 结果文件: `/root/projects/verifier-tts-struct-ie/results/final_results_iou.json`

---
