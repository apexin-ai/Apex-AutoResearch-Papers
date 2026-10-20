# code original 6gen softfilter

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_original-6gen-softfilter_20260516T121507_result.json`
- **Structured JSON:** [`9a4443a5e4b1601a6153.json`](../../sessions/9a/9a4443a5e4b1601a6153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出乎预期——过滤率远非"极低"：

```
Generator         | Total | Filtered |   Rate |  d0 |  d1 |  d2 |  d3 |  d4
--------------------------------------------------------------------------------
Pythia-2.8B       |  4609 |     1683 | 36.52% |   0 |  91 | 406 | 558 | 628
Pythia-1B         |  4555 |     2022 | 44.39% |   0 | 173 | 543 | 640 | 666
OLMo-2-1B        |  4713 |     1913 | 40.59% |   0 | 130 | 456 | 626 | 701
Qwen3-0.6B       |  4538 |     2059 | 45.37% |   0 | 232 | 588 | 613 | 626
Qwen3-1.7B       |  4617 |     2050 | 44.40% |   0 | 144 | 576 | 662 | 668
Qwen3-8B         |  4497 |     1382 | 30.73% |   0 |  84 | 348 | 465 | 485
```

过滤率 30-45%，远高于预期。规律明显：
- **d0 = 0**（全部通过，符合预期——原始种子文本无退化）
- **d1→d4 单调递增**——递归生成深度越大，重复 4-gram 积累越多

这不是模型退化(degenerate looping)，而是递归 re-generation 天然会与上游文本共享短语导致的高 repeated_4gram_ratio。阈值 0.5 对这类数据可能过于激进，或需要区分"循环退化"和"正常短语复现"。

结果已保存至 `/root/gen-depth-fingerprint/results/original_6gen_filter_stats.json`。

---
