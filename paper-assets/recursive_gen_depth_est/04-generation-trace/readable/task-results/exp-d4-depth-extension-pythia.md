# exp d4 depth extension pythia

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d4_depth_extension_pythia_20260518T185442_result.json`
- **Structured JSON:** [`389f34fd450c7b010702.json`](../../sessions/38/389f34fd450c7b010702.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Pythia-1.4B nucleus d4 extension 结果：

| 指标 | Pythia-1.4B | GPT-2 XL (对比) |
|------|------------|-----------------|
| **d3v4 AUC** | 0.7887 | 0.7273 |
| **5-class acc** | 71.33% [70.88, 71.73] | 74.03% [73.90, 74.17] |

**Per-class recall**: d0=99.38%, d1=81.48%, d2=58.62%, d3=49.02%, d4=68.14%

**Feature trends** (均单调递减，符合预期):
- p90_ppl: 483.74 → 61.38 → 29.68 → 18.15 → **12.49**
- var_surprisal: 6.50 → 2.49 → 1.86 → 1.51 → **1.29**
- mean_ppl: d4=31877.82 (非单调，与 GPT-2 XL 类似的异常)

**Pairwise AUCs**: d0v1=0.9955, d1v2=0.8507, d2v3=0.7435, **d3v4=0.7887**

产出已保存到 `results/d4_extension_pythia/`:
- `depth_4.jsonl`
- `features_d4.jsonl`
- `d4_extension_results.json`

Pythia 的 d3v4 AUC (0.7887) 高于 GPT-2 XL (0.7273)，说明 Pythia d3→d4 的区分度更大。5-class accuracy 略低 (71.33% vs 74.03%)，主要因为 d2/d3 混淆更严重（d2 recall 仅 58.62%，d3 仅 49.02%）。

---
