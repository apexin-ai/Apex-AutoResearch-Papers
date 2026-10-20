# code plan 023 item characterization

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_023_item_characterization_20260521T055425_result.json`
- **Structured JSON:** [`ebf924d0e9855a9c9d79.json`](../../sessions/eb/ebf924d0e9855a9c9d79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心发现：

**Difficulty**: DIF-C items 更难（proportion correct 0.409 vs 0.460，d = −0.247），DIF-C 率在中等难度（decile 3）峰值 47.5%，最易 items（decile 10）仅 8.4%。

**Discrimination**: DIF-C items 区分度更高（d = 0.230），Q4（高区分度）DIF-C 率 40.6%，Q1（低区分度）仅 24.7%。

**Domain**: 四大领域 DIF-C 率无显著差异（30.5%–32.3%，χ² p = 0.32）。Subject 层面有变异——business_ethics 最高 48.4%，computer_security 最低 20.7%。

**Direction**: 56.1% reference-favoring（2023 模型更好）vs 43.9% focal-favoring（2024 模型更好），不平衡显著（binomial p = 2.35e-14）。

**Difficulty × Direction 交互**（最关键）: Spearman ρ = −0.597。难的 DIF-C items 绝大多数 focal-favoring（decile 1: 88.7%），易的绝大多数 reference-favoring（decile 10: 96.2%）。解释：2024 模型在难题上进步，但在简单题上优势消失。

---
