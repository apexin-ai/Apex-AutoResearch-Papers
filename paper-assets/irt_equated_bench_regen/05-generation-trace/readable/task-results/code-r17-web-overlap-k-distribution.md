# code r17 web overlap k distribution

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_web_overlap_k_distribution_20260523T120838_result.json`
- **Structured JSON:** [`62883aea1626cef0026f.json`](../../sessions/62/62883aea1626cef0026f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结果概要：**

- 57 个 subject 全部有标注数据，其中 **54 个** 检出 contamination（prevalence > 0%），仅 3 个为 0%（high_school_european_history, high_school_us_history, moral_scenarios）
- Prevalence 分布：mean 38.4%, median 39.8%, 范围 [0%, 76.4%]，标准差 20.8%
- 16 个 subject 超过 50%，41 个超过 25%，50 个超过 10%
- **k 参数约束**：经验上界 k ≤ 54，contamination 跨 subject 分布极广泛，支持在模拟中使用高 k 值（k ≥ 30）

输出文件：
- `artifacts/r17_evidence/web_overlap_k_distribution.py` — 分析脚本
- `artifacts/r17_evidence/web_overlap_k_distribution.md` — 完整报告

---
