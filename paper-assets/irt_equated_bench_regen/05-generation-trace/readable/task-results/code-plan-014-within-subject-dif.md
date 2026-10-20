# code plan 014 within subject dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_014_within_subject_dif_20260520T222310_result.json`
- **Structured JSON:** [`58d27c3377b102aec1d8.json`](../../sessions/58/58d27c3377b102aec1d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。核心结论：

## 结果摘要

### Part 1: Within-Subject Temporal DIF

| Subject | N items | Within C% |
|---------|---------|-----------|
| business_ethics | 93 | 45.2% |
| human_aging | 203 | 33.0% |
| formal_logic | 109 | 39.4% |
| professional_medicine | 248 | 31.0% |
| high_school_statistics | 181 | 42.0% |
| **平均** | | **38.1%** |

### Part 2: Within vs Cross-Subject Matching

两种 matching 的 C% 差异很小（平均 Δ = -2.4pp），信号对 matching variable 选择不敏感。

### Part 3: SIBTEST

R 不可用，Python 也无 SIBTEST 实现（PyPI 上无 pysibtest 包）。

### 判断

**Within-subject C% = 38.1% → HIGH (>25%)**。

Temporal DIF 在隔离到单个 subject 后仍然很高，不是 between-subject 能力差异的伪影——2023→2024 的 temporal 效应渗透到每个内容领域内部。Bifactor 模型单独不够，需要：
1. 分析哪些 item 特征（难度水平）驱动 within-subject C%
2. 自行实现 SIBTEST（无现成包可用）
3. 基于 IRT 参数的 Lord's χ² per subject

---
