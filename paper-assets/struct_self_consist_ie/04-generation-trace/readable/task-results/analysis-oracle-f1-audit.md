# analysis oracle f1 audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle_f1_audit_20260518T212645_result.json`
- **Structured JSON:** [`c3f93739061e70e5303c.json`](../../sessions/c3/c3f93739061e70e5303c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three parts complete. Here's the summary:

---

## Part 1: 0.8150 来源追溯

**来源**: `output/exp_001_seed42_v2/run.log` (SciERC, T=1.0, seed=42, 16 samples)

**产出脚本**: `code/run_mvp_pilot.py` line 228-237

**根因**: 旧流程使用 `compute_ner_f1`（`evaluation.py:42`）进行 **micro-averaged corpus-level** F1 聚合——先把所有实例的 TP/FP/FN 相加，再算 F1。而 `unified_metrics.compute_entity_f1` 是 **per-instance** F1（逐实例算 F1 后取均值）。两者使用相同的 `(start, end, type)` 匹配逻辑，差异纯粹来自聚合方式。

## Part 2: 全量 Oracle F1 对比

74 个实验已重算，保存至 `output/unified_oracle_audit/oracle_f1_recalc_results.json`。

关键发现：
- **exp_001_seed42_v2**: old=0.8150, unified=0.8194, delta=**+0.44pp**（unified 反而更高）
- 多数 SciERC 实验偏差在 **±0.5pp** 以内
- **异常值**: `exp_003_wnut17`(-9.74pp), `exp_008_re`(+18pp, RE/NER subtask 混淆), `exp_011_ood`(-2~-4pp), `exp_entity_token_lp_pilot`(-4.33pp)

## Part 3: exp_026 温度消融 12 实验一致性

| Temp | Seed  | Greedy | Oracle | Degen% |
|------|-------|--------|--------|--------|
| 0.5  | 42    | 0.6490 | 0.7395 | 41.4%  |
| 0.5  | 123   | 0.6449 | 0.7352 | 45.6%  |
| 0.5  | 456   | 0.6463 | 0.7393 | 44.2%  |
| 0.8  | 42    | 0.6439 | 0.7690 | 23.8%  |
| 0.8  | 123   | 0.6433 | 0.7677 | 26.3%  |
| 0.8  | 456   | 0.6471 | 0.7710 | 25.5%  |
| 1.0  | 123   | 0.6440 | 0.7748 | 18.7%  |
| 1.0  | 42    | 0.6453 | 0.7753 | 20.0%  |
| 1.0  | 456   | 0.6456 | 0.7756 | 19.3%  |
| 1.2  | 42    | 0.6425 | 0.7888 | 14.9%  |
| 1.2  | 123   | 0.6419 | 0.7887 | 14.0%  |
| 1.2  | 456   | 0.6466 | 0.7853 | 13.2%  |

**内部一致性良好**：同温度 3 个 seed 的 oracle 偏差 < 0.5pp，趋势单调（T↑ → Oracle↑, Degen%↓）。

---
