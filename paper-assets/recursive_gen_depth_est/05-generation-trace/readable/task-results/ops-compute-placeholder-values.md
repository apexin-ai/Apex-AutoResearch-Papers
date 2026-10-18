# ops compute placeholder values

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_compute-placeholder-values_20260515T233122_result.json`
- **Structured JSON:** [`515aedf0ba2b4baeb458.json`](../../sessions/51/515aedf0ba2b4baeb458.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。

**结果：**

| Placeholder | 位置 | 值 |
|---|---|---|
| d0-excluded 3-class range | abstract.tex L5 | **58.8%–82.6%** |
| cross-strategy d1-d3 accuracy | generalization.tex L95 | **45.9%** |

**关键发现：** cross-strategy LOO 的 4-class mean accuracy 是 59.1%，但排除 d0 后降至 45.9%——d0 的近乎完美分类（recall ≈ 100%）大幅拉高了整体数字。d1-d3 间的区分在跨策略泛化场景下相当困难，最差的 fold（pythia_topk50）仅 35.4%，接近 3-class 随机基线（33.3%）。

产出已写入 `artifacts/placeholder_values.json` 并注册，`memory.md` 已更新供 Paper Agent 使用。

---
