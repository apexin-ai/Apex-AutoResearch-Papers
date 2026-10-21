# code fix format prompt

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-format-prompt_20260514T164753_result.json`
- **Structured JSON:** [`6138a85de1ae269c0179.json`](../../sessions/61/6138a85de1ae269c0179.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。结果汇总：

### Prompt 修改前后对比

**修改前** (no_trace 为例):
```
Given the following code:
{solution}

Does this code pass all tests? Answer: 
```

**修改后** (三个条件统一包含 test code):
```
Given the following code:
{solution}

Test code:
{test_code}

Does this code pass all tests? Answer: 
```

vota 和 full_trace 条件在 test code 后追加各自的 execution trace 块。

### Label token 检查
- `'pass'` → token `[6385]` (单 token)
- `'fail'` → token `[18403]` (单 token)
- **不需要调整 `max_new_tokens`**，当前设置没问题。

### 截断率统计
已内置到脚本中，格式化 raw_traces.jsonl 时会自动用 tokenizer 统计各条件的 avg/p50/p95/max token 数和 >2048 截断率。当前 raw_traces.jsonl 尚未生成，待数据生成后运行即可获得。

### test_code 来源
`generate_data.py` 输出的 raw_traces.jsonl 不含 `test_code` 字段，`format_training_data.py` 会自动从 HumanEval/MBPP 数据集加载并构建 `{problem_id: test_code}` 映射表作为 fallback。

---
