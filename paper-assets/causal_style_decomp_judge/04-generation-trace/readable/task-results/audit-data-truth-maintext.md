# audit data truth maintext

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-truth-maintext_20260525T194155_result.json`
- **Structured JSON:** [`9c1628406d4c52c74c37.json`](../../sessions/9c/9c1628406d4c52c74c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。37 个数字逐一对账，结果：

**33 个已验证** — 可追溯到 table1_verified.csv、nli_gate_ablation.json、construct_divergence_analysis.json、verbosity_bidir_nli.jsonl、scored.jsonl 等原始数据文件。

**2 个问题：**

1. **GPT-4o BT = 63.0% (intro:18)** — 中等严重度。nli_threshold_sweep 给出 bt=0.6228 (62.3%)，而论文报 .630。差异源于 bootstrap_10k_holm.py 使用 `alpha=0.01`，但论文声称用 "default α=10⁻⁶"。建议重跑脚本保存 output，并修正 experiments.tex 中 alpha 描述。

2. **ΔBERTScore < 0.02 (method:24)** — 低严重度。无汇总数据文件验证，但原始 bertscore_cf 字段存在于各 verified_*.jsonl 中，可重算。

**1 个外部引用**（"76–92%" from citations，不在审计范围）。

所有跨文件引用在论文内部保持一致。

---
