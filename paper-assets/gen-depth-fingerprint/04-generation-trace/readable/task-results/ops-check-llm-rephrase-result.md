# ops check llm rephrase result

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-llm-rephrase-result_20260517T005718_result.json`
- **Structured JSON:** [`0fd6bf7ddea77bd75eef.json`](../../sessions/0f/0fd6bf7ddea77bd75eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验失败。**

**状态**：
- Rephrase 阶段成功完成（5000/5000 texts，avg 1.69 sentences replaced）
- 中间文件 `rephrased_texts.jsonl` 已保存（5000 行）
- 在第 4/6 步（特征提取）崩溃

**错误原因**：
```
File "run_llm_rephrase.py", line 205, in extract_features_batch
    tail_decay = float(np.polyfit(log_ranks, log_probs_tail, 1)[0])
TypeError: array type float16 is unsupported in linalg
```

Pythia-410M 在 float16 模式加载，`np.polyfit` 收到 float16 数组后调用 `np.linalg.lstsq` 报错，因为 numpy linalg 不支持 float16。

**修复方案**：在 `run_llm_rephrase.py:205` 附近，将传入 `np.polyfit` 的数组转为 float32：

```python
tail_decay = float(np.polyfit(log_ranks.astype(np.float32), log_probs_tail.astype(np.float32), 1)[0])
```

或者在更上游提取 log_probs 时统一 `.float()` 转换。

需要我修复代码并重新运行实验吗？

---
