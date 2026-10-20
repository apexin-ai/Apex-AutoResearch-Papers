# eval test set distribution

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_test_set_distribution_20260514T083830_result.json`
- **Structured JSON:** [`55440a73b4862f3905c2.json`](../../sessions/55/55440a73b4862f3905c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Split 分布检查：

| Split | Total | Progress | Stagnation | Unique Instances | Conf Dist |
|-------|-------|----------|------------|------------------|-----------|
| Train | 10,634 | 6,740 (63.4%) | 3,894 (36.6%) | 1,386 | {2: 10130, 3: 504} |
| Val | 2,943 | 1,476 (50.2%) | 1,467 (49.8%) | 297 | {2: 2699, 3: 244} |
| Test | 1,824 | 1,339 (73.4%) | 485 (26.6%) | 297 | {2: 1780, 3: 44} |

**结论：分布存在显著偏差。**

- **类别比例不一致**：Train 63.4% progress，Val 50.2%，Test 73.4%。三个 split 的 progress 比例差距超过 20 个百分点，Val 接近均衡而 Test 严重偏向 progress。
- **原因**：按 instance_id 分组切分，不同 instance 的 progress/stagnation window 数量不同，导致样本级类别比例在 split 间不均匀。
- **conf=3 分布也不均**：Train 有 504 个 conf=3 样本，Val 244 个，Test 仅 44 个。
- **建议**：如果需要公平评估，应在切分后对 train 做类别重采样（或加 class weight），并注意 test 上的指标会因类别不均衡而偏高（accuracy 虚高）。评估时应关注 balanced accuracy、F1 或各类别的 precision/recall，而非 raw accuracy。

---
