# data exception subcomponent

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_exception_subcomponent_20260522T041316_result.json`
- **Structured JSON:** [`13aedd33d5e947f178d2.json`](../../sessions/13/13aedd33d5e947f178d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据生成完成。汇总报告：

## 产出

### 文件列表
```
/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/
├── exc_type_only_train.jsonl      (4720 行)
├── exc_type_only_test.jsonl       (1190 行)
├── exc_stacktrace_only_train.jsonl (4720 行)
├── exc_stacktrace_only_test.jsonl  (1190 行)
├── exc_message_only_train.jsonl   (4720 行)
└── exc_message_only_test.jsonl    (1190 行)
```

### 数据统计

|  | Train | Test |
|---|---|---|
| 总样本 | 4720 | 1190 |
| fail | 1613 | 339 |
| pass | 3107 | 851 |
| 含 `[ERROR]` 行（被拆分） | 1391 | 277 |
| fail 但无 trace（`[No trace available]`，保持原样） | 230 | 70 |
| pass 无异常（`[No exception data]`，保持原样） | 3099 | 843 |

注：train 实际 4720 行，非此前估计的 3530。

### 解析成功率
- Train: 4299/4299 error lines parsed (100%)，1391/1391 样本完全解析
- Test: 847/847 error lines parsed (100%)，277/277 样本完全解析

### 平均 trace 长度（字符，仅含 `[ERROR]` 的样本）

| 条件 | Train | Test |
|---|---|---|
| original | 3571 | 3537 |
| exc_type_only | 130 (−96%) | 131 |
| exc_stacktrace_only | 3462 (−3%) | 3427 |
| exc_message_only | 91 (−97%) | 94 |

### 三个条件的变换逻辑
原始格式：`[ERROR] ValueError at line 2: too many values to unpack (expected 2) | locals: ...`

1. **exc_type_only** → `[ERROR] ValueError: too many values to unpack (expected 2)` （保留异常类型+消息，去掉行号和 locals）
2. **exc_stacktrace_only** → `[ERROR] at line 2 | locals: ...` （保留行号+locals，去掉异常类型和消息）
3. **exc_message_only** → `too many values to unpack (expected 2)` （仅保留消息文本；无消息的如 AssertionError 用 `[AssertionError]` 占位）

脚本位于 `/root/trace-verdict-study/data/create_exception_subcomponents.py`。

---
