# analysis check deberta tiebreaking fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-deberta-tiebreaking-fix_20260522T145113_result.json`
- **Structured JSON:** [`d7289e17cd48da8f5c39.json`](../../sessions/d7/d7289e17cd48da8f5c39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，结果如下：

### 1. eval_finetuned_nli.py 当前 CLASSES 定义

**L30**: `CLASSES = ["True", "False", "Unknown"]` — **未排序，原样未改。**

### 2. 是否已修复

**未修复。** 仍然是 `["True", "False", "Unknown"]`，不是字母序 `["False", "True", "Unknown"]`。

当前 tiebreaking 行为：L66 `max(CLASSES, key=lambda x: votes.get(x, 0))` 在票数相同时，`max` 返回迭代顺序中最后一个最大值，即 "Unknown" > "False" > "True"。而 D061 canonical tiebreaking 要求字母序（"False" 优先），需要改为 `sorted(...)` 或直接写 `["False", "True", "Unknown"]`。

L241/243 的 combo voting 也有同样问题。

### 3. finetune_deberta_pw.py 是否有类似问题

**无同类问题。** 该文件不使用 `CLASSES` 列表，标签映射是硬编码的 dict：
- `PW_TO_NLI = {"True": 2, "False": 0, "Unknown": 1}`  
- `NLI_TO_PW = {2: "True", 0: "False", 1: "Unknown"}`

这些是 NLI label index 映射，不涉及 tiebreaking 顺序，不需要修改。

---
