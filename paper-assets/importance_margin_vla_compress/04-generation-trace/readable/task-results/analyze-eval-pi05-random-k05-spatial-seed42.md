# analyze eval pi05 random k05 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_spatial_seed42_20260521T204833_result.json`
- **Structured JSON:** [`b4fc255d883167d96d74.json`](../../sessions/b4/b4fc255d883167d96d74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**π0.5 Random k=0.5 Spatial seed42 结果：71.6% SR**（baseline 97.2%，保留 73.7%）

Cross-suite 对比：
- Object: random 69.4% vs L2norm 33.4% → random 大幅领先 (+36pp)
- Spatial: random 71.6% → 待 L2norm Spatial 完成后对比

注意 Spatial 上 random 的方差较大：最高 88%（T0/T2）、最低 38%（T5），涉及精确空间关系的任务（on top of、in drawer）明显更难。

---
