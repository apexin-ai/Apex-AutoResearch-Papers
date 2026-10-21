# cpu e3 mbr multiseed fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_e3_mbr_multiseed_fix_20260521T115507_result.json`
- **Structured JSON:** [`3f1abdf23baf4466a8a0.json`](../../sessions/3f/3f1abdf23baf4466a8a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**数据源验证**：exp_002 是旧 MF4 的 N=16 数据，CoNLL MBR 已改用 MF4v2 N=8 数据重算。

**已完成计算**（5 组）：SciERC ×3 seeds, CoNLL ×1, FewNERD ×1。**Pending**（4 组）：CoNLL seed123/456（未生成），FewNERD seed42/123（运行中）。

**核心发现**：MBR 在所有 5 组实验中均 ≤ Greedy（−0.06% ~ −0.77%）。MV 表现不一：SciERC seed123/456 和 CoNLL 上略优于 Greedy，其余略差。Oracle gap 8~12pp 说明 sample pool 有潜力，但 pairwise-F1 consensus 无法利用。

脚本已部署到两台服务器 `code/e3_mbr_multiseed.py`，待 FewNERD seed42/123 和 CoNLL seed123/456 数据就绪后可直接重跑补全。

---
