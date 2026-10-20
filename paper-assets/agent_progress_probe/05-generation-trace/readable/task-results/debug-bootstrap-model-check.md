# debug bootstrap model check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_bootstrap-model-check_20260515T085542_result.json`
- **Structured JSON:** [`3bcfc5043a38d9fea3a3.json`](../../sessions/3b/3bcfc5043a38d9fea3a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gold_set/model_consistency_report.md`。

核心结论：

**0.802 vs 0.760 的根因是训练数据泄露。** `gold_bootstrap_ci.py` 没有从训练集中排除 gold windows（至少 39 个 gold windows 在训练集中），导致分数虚高。次因是 bootstrap 脚本缺少 OH trajectory 索引（63/199 gold windows 来自 OH，特征是垃圾值）。

**两个数字都不是论文原始模型的结果。** 两个脚本均使用 `learning_rate=0.1`，但论文的 cross-agent GB 使用 `learning_rate=0.05`（见 `src/analysis/bootstrap_ci_crossagent.py:100`）。且不存在保存的 GB checkpoint——每次都重新训练。

**论文模型在 gold set 上的正确 macro-F1 尚未得出**，需将 lr 改为 0.05 并用 leakage-fixed 的 evaluate_gold_set.py 重新跑一次。

---
