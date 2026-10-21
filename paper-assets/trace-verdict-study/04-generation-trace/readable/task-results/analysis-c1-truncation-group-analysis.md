# analysis c1 truncation group analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1_truncation_group_analysis_20260515T225641_result.json`
- **Structured JSON:** [`a97109a0eccb8cf8cdaa.json`](../../sessions/a9/a97109a0eccb8cf8cdaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果如下：

```
=== DeepSeek VOTA: Training Truncation Group Analysis ===
(Inference without truncation, overall accuracy = 84.45%)

Group A (train-truncated, >1976 content tok): N=1091, accuracy=83.04%, 95% CI [80.75%, 85.24%]
Group B (train-intact, ≤1976 content tok):    N=99,   accuracy=100.00%, 95% CI [100%, 100%]
Difference: 16.96pp, Fisher exact p < 1e-6

Per-class breakdown:
  Truncated - pass: N=822, accuracy=100% (perfect)
  Truncated - fail: N=269, accuracy=31.23% (185 errors, all errors come from here)
  Intact - pass:    N=29,  accuracy=100%
  Intact - fail:    N=70,  accuracy=100%
```

关键发现：
- 未被截断的 99 个样本 **100% 准确率**（pass 和 fail 全对）
- 被截断的 1091 个样本总体 83.04%，但 pass 类全对，**所有 185 个错误集中在截断组的 fail 类**（fail recall 仅 31.2%）
- 模型对截断样本学到了 pass 偏置——训练时截断丢失了输入末尾的 question suffix，但 pass 类的标签信号仍可从代码结构中学到；fail 类则需要完整的 trace+question 才能准确判断

---
