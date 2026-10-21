# infra llama en probe v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama_en_probe_v2_20260521T173441_result.json`
- **Structured JSON:** [`3da592799eab71346521.json`](../../sessions/3d/3da592799eab71346521.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[Llama EN→EN 探针结果]
Peak: 77.6% (layer 28)
Binomial p: 0.0 (< 1e-6)
Permutation p: 0.000 (0/1000)
Gate: CONDITIONAL (< 80% 但统计显著)

每层 accuracy:
Layer  0: 63.6%
Layer  1: 65.1%
Layer  2: 69.1%
Layer  3: 65.8%
Layer  4: 63.6%
Layer  5: 69.9%
Layer  6: 68.8%
Layer  7: 71.0%
Layer  8: 69.5%
Layer  9: 71.0%
Layer 10: 74.6%
Layer 11: 72.8%
Layer 12: 72.8%
Layer 13: 76.1%
Layer 14: 72.8%
Layer 15: 76.1%
Layer 16: 76.8%
Layer 17: 75.0%
Layer 18: 73.9%
Layer 19: 75.7%
Layer 20: 74.6%
Layer 21: 75.7%
Layer 22: 76.5%
Layer 23: 73.2%
Layer 24: 74.6%
Layer 25: 72.1%
Layer 26: 76.5%
Layer 27: 74.3%
Layer 28: 77.6%  ← peak
Layer 29: 76.5%
Layer 30: 77.2%
Layer 31: 76.8%
```

输出文件：
- `data/llama31/probe_results.json`
- `data/llama31/probe_accuracy_by_layer.png`

相比 buggy Qwen 的 63%，修复后 Llama 提升到 77.6%（+14.6pp）。所有层 binomial p < 1e-5，permutation p = 0.000。信号高度显著但未过 80% gate，判定 **CONDITIONAL**。accuracy 从 layer 10 起稳定在 72-78% 的高原，peak 在 layer 28（中后层），符合语义特征在深层编码的预期模式。

---
