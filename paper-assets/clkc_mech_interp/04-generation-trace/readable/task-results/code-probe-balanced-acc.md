# code probe balanced acc

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe_balanced_acc_20260521T195241_result.json`
- **Structured JSON:** [`39e847b6e5218a116272.json`](../../sessions/39/39e847b6e5218a116272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
[代码修改]
- class_weight='balanced': ✓
- balanced_accuracy_score: ✓
- f1_score: ✓

[Qwen 探针结果]
=== EN→EN ===
Accuracy: 75.0% | Balanced Acc: 75.0% | F1: 0.7500
Peak layer: 24, Binomial p: 0.000000, Permutation p: 0.0

=== ZH→ZH ===
Accuracy: 63.0% | Balanced Acc: 63.0% | F1: 0.6271
Peak layer: 21, Binomial p: 0.000035, Permutation p: 0.0

=== EN→ZH ===
Accuracy: 63.5% | Balanced Acc: 63.5% | F1: 0.6449
Peak layer: 22, Binomial p: 0.000020, Permutation p: 0.0

=== ZH→EN ===
Accuracy: 62.5% | Balanced Acc: 62.5% | F1: 0.6087
Peak layer: 19, Binomial p: 0.000742, Permutation p: 0.01

Gate: PASS
```

`class_weight='balanced'` 后 Accuracy 和 Balanced Accuracy 完全一致（说明分类器不再偏向多数类），所有方向 permutation p ≤ 0.01。跨语言迁移 EN→ZH 63.5% / ZH→EN 62.5% 的 balanced accuracy 远高于 50% chance，信号可靠。

---
