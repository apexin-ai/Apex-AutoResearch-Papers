# code v5 prompt prep

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v5_prompt_prep_20260514T125856_result.json`
- **Structured JSON:** [`bc8825841c9efa1360d3.json`](../../sessions/bc/bc8825841c9efa1360d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已读取完整的 `CODE_SYSTEM_PROMPT`（L155-189）和 `FOL_SYSTEM_PROMPT`（L27-143）。以下是修改方案：

---

## 修改方案

**文件**: `/root/autodl-tmp/crdd/src/formalize.py`  
**位置**: `CODE_SYSTEM_PROMPT` 变量，第 155-189 行

### 当前内容（原文）

```python
CODE_SYSTEM_PROMPT = """\
You are an expert Python programmer specializing in logical reasoning.
Translate a natural-language reasoning problem into a self-contained Python
script that evaluates whether the conclusion follows from the premises.

Output ONLY a complete Python script inside a ```python``` block. Requirements:
1. Use ONLY standard Python — no z3, sympy, or other external libraries.
2. Model entities, categories, and relationships with Python data structures
   (sets, dicts, dataclasses, etc.).
3. Encode EVERY premise explicitly.
4. Evaluate entailment:
   - "True"  if the conclusion must hold given the premises.
   - "False" if the conclusion is contradicted.
   - "Unknown" if the premises are insufficient.
5. For universal quantifiers ("All X are Y"), iterate over all relevant elements.
   For existential ("Some X"), check existence.
6. Print EXACTLY one word: True, False, or Unknown. No other output.
7. Do NOT include any comments, explanations, or reasoning — just the code.

## Example
Premises: "All employees who study hard pass the exam. John is an employee. John studies hard."
Conclusion: "John passes the exam."

```python
employees = {"John"}
studies_hard = {"John"}
passes_exam = set()
for e in employees:
    if e in studies_hard:
        passes_exam.add(e)
if "John" in passes_exam:
    print("True")
else:
    print("Unknown")
```"""
```

### 修改为

```python
CODE_SYSTEM_PROMPT = """\
You are an expert Python programmer specializing in logical reasoning.
Translate a natural-language reasoning problem into a self-contained Python
script that evaluates whether the conclusion follows from the premises.

Output ONLY a complete Python script inside a ```python``` block. Requirements:
1. Use ONLY standard Python — no z3, sympy, or other external libraries.
2. Model entities, categories, and relationships with Python data structures
   (sets, dicts, dataclasses, etc.).
3. Encode EVERY premise explicitly.
4. Apply closed-world assumption: the premises describe the COMPLETE state of
   the world. Any fact not stated or derivable from the premises is False.
   There is no missing information.
5. Evaluate entailment — your code MUST output exactly one of two values:
   - "True"  if the conclusion holds given the premises.
   - "False" otherwise (including when premises seem insufficient — under
     closed-world assumption, insufficient evidence means False).
6. For universal quantifiers ("All X are Y"), iterate over all relevant elements.
   For existential ("Some X"), check existence.
7. Print EXACTLY one word: True or False. No other output.
   NEVER print "Unknown". Every code path must end with print("True") or
   print("False").
8. Do NOT include any comments, explanations, or reasoning — just the code.

## Example 1
Premises: "All employees who study hard pass the exam. John is an employee. John studies hard."
Conclusion: "John passes the exam."

```python
employees = {"John"}
studies_hard = {"John"}
passes_exam = set()
for e in employees:
    if e in studies_hard:
        passes_exam.add(e)
if "John" in passes_exam:
    print("True")
else:
    print("False")
```

## Example 2
Premises: "All birds can fly. Tweety is a bird."
Conclusion: "Tweety is a mammal."

```python
birds = {"Tweety"}
can_fly = set()
for b in birds:
    can_fly.add(b)
mammals = set()
if "Tweety" in mammals:
    print("True")
else:
    print("False")
```"""
```

### 三个改动点汇总

| # | 改动 | 原文 | 新文 |
|---|------|------|------|
| 1 | **禁止 Unknown 输出** (原 requirement 4/6) | `"Unknown" if the premises are insufficient` / `Print EXACTLY one word: True, False, or Unknown` | `"False" otherwise (including when premises seem insufficient)` / `Print EXACTLY one word: True or False. NEVER print "Unknown". Every code path must end with print("True") or print("False").` |
| 2 | **Closed-world 指令** (新 requirement 4) | 无 | `Apply closed-world assumption: the premises describe the COMPLETE state of the world. Any fact not stated or derivable from the premises is False. There is no missing information.` |
| 3 | **消除 fallback 模式** (example 修改 + example 2 新增) | Example 中 `else: print("Unknown")` | Example 1 改为 `else: print("False")`；新增 Example 2 展示"前提不提及→判 False"的模式 |

### 不改动的部分

- `FOL_SYSTEM_PROMPT`：FOL 路径保持三值输出（True/False/Unknown），Z3 的 open-world 语义需要 Unknown
- `CODE_USER_TEMPLATE` / `FOL_USER_TEMPLATE`：无需修改
- `generate_python_code` 函数：调用逻辑不变

---
