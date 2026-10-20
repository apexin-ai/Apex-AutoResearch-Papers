# fix gold pipeline probe split

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gold-pipeline-probe-split_20260514T194423_result.json`
- **Structured JSON:** [`792de1a213ce54e25592.json`](../../sessions/79/792de1a213ce54e25592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项修复均已完成：

**Fix 1 — Probe 评估分 gold∩train / gold∩test**：
- `gold_all`: macro_f1=0.9612, n=15401
- `gold_in_train`: macro_f1=0.9708, n=10634
- `gold_in_test`: macro_f1=0.9404, n=4767
- 训练集/测试集差异约 3 个点，符合预期，无严重泄漏

**Fix 2 — 重新生成 gold_dryrun_results/**：
- RF: 0.9983 (之前 0.9994)，GB: 0.9972 — 均 <0.999，符合修复后预期
- results.json 和 report.md 已更新

---
