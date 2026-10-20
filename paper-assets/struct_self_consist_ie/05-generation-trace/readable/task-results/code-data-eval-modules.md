# code data eval modules

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_eval_modules_20260514T042533_result.json`
- **Structured JSON:** [`5a602eabc67edb9bafe3.json`](../../sessions/5a/5a602eabc67edb9bafe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模块已创建并验证 import 无报错：

- **`data_utils.py`** — SciERC 加载与解析（token index → char offset 转换）、ACE05 接口预留（`NotImplementedError`）、JSONL 读写、数据集划分
- **`evaluation.py`** — NER strict match、EAE argument match、per-instance F1、Spearman 相关性、`generate_evaluation_report` 汇总（greedy F1 / oracle best-of-N / consistency-F1 correlation）

---
