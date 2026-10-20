# ops cuda5 ready check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda5-ready-check_20260514T095100_result.json`
- **Structured JSON:** [`ddae5f6d8b6a9d1dfa08.json`](../../sessions/dd/ddae5f6d8b6a9d1dfa08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:5 已释放**，eval 于 17:32 完成。

**Qwen2.5-3B raw eval 结果：**

| Benchmark | Score |
|-----------|-------|
| GSM8K | 60.50% (798/1319) |
| HumanEval | 0.00% (0/164) |

HumanEval pass@1 = 0 是因为 base model 生成的全是 `"Here's the completed Python function:\n\n```python"` 这类自然语言前缀，没有直接输出可执行代码，导致全部解析失败。这是 base model（非 instruct）在 HumanEval 上的典型表现——不影响 contamination calibration 实验的有效性，因为我们关注的是 item-level response pattern 而非绝对分数。

---
