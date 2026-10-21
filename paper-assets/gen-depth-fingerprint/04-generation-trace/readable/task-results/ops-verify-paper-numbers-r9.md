# ops verify paper numbers r9

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-paper-numbers-r9_20260516T130253_result.json`
- **Structured JSON:** [`b6179bee0fbc480e7435.json`](../../sessions/b6/b6179bee0fbc480e7435.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the evidence needed.

## Report

### 1. "16.9% depth retention loss by gen-4" (discussion.tex:27)

**Source file**: `/root/gen-depth-fingerprint/data/prompt_type_results.json`

**Actual data**: continuation `retention_d4_pct` = 83.1%, meaning loss = **16.9%** (= 100 - 83.1).

Calculation: d0=995, d4=827 → 827/995 = 0.8311 → loss = 16.89% ≈ 16.9%.

**Verdict: 数字匹配。** 来源是 `data/prompt_type_results.json` 的 `depth_decay.continuation` 字段。

---

### 2. "within-type CV F1 of 0.781 for continuation" (discussion.tex:28, limitations.tex:16)

**Source file**: `/root/gen-depth-fingerprint/data/prompt_type_results.json`

**Actual data**: `per_prompt_cv_f1.continuation.mean` = **0.7806**

论文写 0.781，实际值 0.7806 四舍五入到三位小数是 0.781。

**Verdict: 数字匹配。** 来源是 `data/prompt_type_results.json` 的 `per_prompt_cv_f1.continuation.mean` 字段。

---

**总结：两个数字均有实验来源，数值正确。**

---
