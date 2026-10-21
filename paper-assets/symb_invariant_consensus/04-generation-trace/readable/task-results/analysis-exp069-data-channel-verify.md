# analysis exp069 data channel verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp069-data-channel-verify_20260519T125446_result.json`
- **Structured JSON:** [`8ff10cc7f0f534ce348f.json`](../../sessions/8f/8ff10cc7f0f534ce348f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息齐全，以下是分析报告。

---

## 报告：StrategyQA 通道对 LogiQA 数据的兼容性

### 1. StrategyQA 通道的 prompt 模板

**不适用** — LogiQA 数据实际上没有走 StrategyQA 通道。

LogiQA 数据自带 `"dataset": "logiqa"` 字段，`setdefault("dataset", "strategyqa")` (第68行) **不会覆盖**已有值。因此 `run_full_mvp.py` 第264行的路由走的是 `logiqa` 分支：

```python
elif dataset == "logiqa":
    extractor.domain = "logic"
    pipeline.trace_generator.domain = "multichoice"
```

### 2. 实际使用的 prompt 和答案解析

| 组件 | domain | prompt 模板 | 答案解析 |
|------|--------|-------------|----------|
| trace_generator | `multichoice` | `MULTICHOICE_SOLVE_PROMPT`: "Answer the following multiple-choice question step by step...put your final answer letter in \\boxed{}, e.g. \\boxed{A}." | `extract_boxed_answer` → fallback `extract_choice_answer`（支持 A/B/C/D）|
| constraint_extractor | `logic` | `LOGIC_EXTRACTION_PROMPT`: 面向 ProofWriter 风格（facts/rules/derived, True/False/Unknown） | 提取约束结构，不影响最终 answer |

### 3. 答案归一化

pipeline.py 第67行：
```python
if problem.get("dataset", "math") in ("proofwriter", "folio", "strategyqa"):
    t["answer"] = normalize_logic_answer(t["answer"])
```
`"logiqa"` **不在此列表中** → `normalize_logic_answer` 不会被调用。这是正确的行为——该函数会把答案映射到 True/False/Unknown，对 A/B/C/D 字母答案是破坏性的。

### 4. 答案比对

`is_equiv("A", "D")` → `normalize_answer` 做 LaTeX 清洗后字符串比较 → 对单字母答案等价于精确匹配。**正确。**

### 5. LogiQA 数据格式

```json
{
  "id": "logiqa_000",
  "problem": "Context: ... \n\nQuestion: ...\n\nA. ...\nB. ...\nC. ...\nD. ...",
  "answer": "D",
  "dataset": "logiqa",
  "choices": ["A. ...", "B. ...", "C. ...", "D. ..."],
  "context": "..."
}
```

### 结论：**兼容，结果有效**

关键路径全部正确：
- **数据路由**：✓ `"dataset": "logiqa"` 未被覆盖，走专用 `logiqa` 分支
- **Prompt 模板**：✓ trace_generator 用 `MULTICHOICE_SOLVE_PROMPT`（多选题格式，\\boxed{A}）
- **答案提取**：✓ 使用 `extract_choice_answer`（正则匹配 A/B/C/D）
- **答案归一化**：✓ 不走 `normalize_logic_answer`（不会把字母映射成 True/False）
- **答案比对**：✓ `is_equiv` 字符串精确匹配，适用于字母答案

**唯一隐患**：constraint_extractor 用的是 `LOGIC_EXTRACTION_PROMPT`（为 ProofWriter 设计，期望 True/False/Unknown 和 fact/rule/derived 约束类型），对 LogiQA 的分析推理类问题不太适配。约束提取质量可能较低，但**不会导致答案系统性错误**——最终答案选择基于 trace_generator 的答案，约束只影响 SICA 的加权打分。

**不需要用 `run_logiqa.py` 重跑。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "id": "logiqa_000",
    "problem": "Context: ... \n\nQuestion: ...\n\nA. ...\nB. ...\nC. ...\nD. ...",
    "answer": "D",
    "dataset": "logiqa",
    "choices": [
      "A. ...",
      "B. ...",
      "C. ...",
      "D. ..."
    ],
    "context": "..."
  }
}
```

</details>

---
