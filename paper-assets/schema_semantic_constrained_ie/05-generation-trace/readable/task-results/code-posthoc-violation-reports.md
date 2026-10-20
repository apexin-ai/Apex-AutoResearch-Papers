# code posthoc violation reports

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_posthoc_violation_reports_20260518T111917_result.json`
- **Structured JSON:** [`8b60e363cc3cf0f68046.json`](../../sessions/8b/8b60e363cc3cf0f68046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

## Unconstrained + Post-hoc 汇总

### Violation Report

| Model | Docs | Parse Fail | Events | Args | EV | RoV | AC | CF | RoV+AC Rate |
|-------|------|------------|--------|------|----|-----|----|----|-------------|
| **Llama** | 226 | 20 | 2189 | 3 | 0% | 0% | 0% | 0% | 0.0000 |
| **Qwen** | 218 | 28 | 2291 | 23 | 0% | 0% | 0% | 0% | 0.0000 |
| **Mistral** | 194 | 52 | 1507 | 0 | 0% | 0% | 0% | 0% | 0.0000 |

所有 violation rate 均为 **0%**，post-hoc 修正完全消除了 schema 违规。

### F1 Scores

| Model | Trigger P | Trigger R | **Trigger F1** | Arg P | Arg R | **Arg F1** | Parse Fail |
|-------|-----------|-----------|----------------|-------|-------|------------|------------|
| **Llama** | 0.0667 | 0.0551 | **0.0604** | 0.0000 | 0.0000 | **0.0000** | 20 |
| **Qwen** | 0.1468 | 0.1289 | **0.1373** | 0.0870 | 0.0005 | **0.0010** | 28 |
| **Mistral** | 0.0351 | 0.0268 | **0.0304** | 0.0000 | 0.0000 | **0.0000** | 52 |

关键发现：post-hoc 修正成功将 violation 清零，但 F1 极低（Entity pred 全为 0，Argument 几乎为 0），说明 unconstrained 输出的结构化质量本身很差，post-hoc 只能修正 schema 合规性，无法挽救结构化抽取质量。

---
