# code exp16 precision recall

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-precision-recall_20260520T060847_result.json`
- **Structured JSON:** [`6587ef9754f006e882dc.json`](../../sessions/65/6587ef9754f006e882dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

**Important note:** DD OOD contains only jailbreak samples (80 attack conversations, 0 benign). The confusion matrix row for class 0 is `[0, 0]` in all files, meaning **precision is trivially 1.000 for all models** (no benign samples → no false positives possible). The discriminative metric is **recall** (jailbreak detection rate).

---

```
exp16 DD OOD Precision/Recall 分解:

注意: DD OOD 仅含 jailbreak 样本 (n=80), 无 benign 样本
      Precision 均为 1.000 (trivial, 无 FP 可能)
      核心对比指标为 Recall (= detection rate)

9-class:
  seed42:  P=1.000  R=0.613  F1=0.760  (TP=49, FN=31)
  seed123: P=1.000  R=0.938  F1=0.968  (TP=75, FN=5)
  seed456: P=1.000  R=0.675  F1=0.806  (TP=54, FN=26)
  mean:    P=1.000±0.000  R=0.742±0.141  F1=0.844±0.089

vanilla:
  seed42:  P=1.000  R=0.025  F1=0.049  (TP=2, FN=78)
  seed123: P=1.000  R=0.038  F1=0.072  (TP=3, FN=77)
  seed456: P=1.000  R=0.213  F1=0.351  (TP=17, FN=63)
  mean:    P=1.000±0.000  R=0.092±0.086  F1=0.157±0.137
```

**论文要点：** 对于 "relative ranking" vs "absolute deployability" 的论述：
- 9-class recall (0.742) 远高于 vanilla (0.092)，relative ranking 清晰
- 但 9-class 的 seed variance 很大（0.613–0.938），且 seed42 只有 61.3% recall，说明 absolute deployability 仍有提升空间
- 由于 DD OOD 无 benign 样本，precision 对比需看 mixed_test 或其他含 benign 的测试集

如需 mixed_test 上的 precision/recall 分解来补充 deployability 论述，可以继续提取。

---
