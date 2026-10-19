# infra qwen en probe v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen_en_probe_v2_20260521T173449_result.json`
- **Structured JSON:** [`de50b3be0c856d6b2f5b.json`](../../sessions/de/de50b3be0c856d6b2f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[Qwen3-8B EN→EN 探针结果]
Peak: 70.2% (layer 19)
Binomial p: 0.0 (< machine epsilon)
Permutation p: 0.000 (0/1000 permutations exceeded observed acc)
Gate: CONDITIONAL (70% > 50% chance, but < 80% threshold)

每层 accuracy:
Layer  0: 56.7%
Layer  1: 58.8%
Layer  2: 59.7%
Layer  3: 60.5%
Layer  4: 60.1%
Layer  5: 63.0%
Layer  6: 63.0%
Layer  7: 60.1%
Layer  8: 60.9%
Layer  9: 65.6%
Layer 10: 63.9%
Layer 11: 65.1%
Layer 12: 66.8%
Layer 13: 69.3%
Layer 14: 66.8%
Layer 15: 68.1%
Layer 16: 67.2%
Layer 17: 68.9%
Layer 18: 69.3%
Layer 19: 70.2%  ← peak
Layer 20: 68.9%
Layer 21: 66.4%
Layer 22: 69.3%
Layer 23: 69.3%
Layer 24: 64.3%
Layer 25: 65.6%
Layer 26: 65.6%
Layer 27: 62.6%
Layer 28: 63.5%
Layer 29: 66.4%
Layer 30: 65.6%
Layer 31: 68.1%
Layer 32: 65.1%
Layer 33: 63.9%
Layer 34: 63.0%
Layer 35: 61.3%

输出文件:
- data/qwen3/probe_results.json
- data/qwen3/probe_accuracy_by_layer.png
- logs/probe_qwen_en_v2.log
```

修复 left-padding bug 后从 63% 提升到 70.2%（+7%），统计显著性极强（binomial p ≈ 0, permutation p = 0.000）。信号集中在 layers 13-23 的中间层，符合 mechanistic interpretability 中概念表征在中间层形成的预期。但 70% 未到 80% gate，判定 **CONDITIONAL**。

---
