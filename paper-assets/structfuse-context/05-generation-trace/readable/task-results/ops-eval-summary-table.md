# ops eval summary table

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-summary-table_20260515T230410_result.json`
- **Structured JSON:** [`b4fc1e4d8dbd14d2e30e.json`](../../sessions/b4/b4fc1e4d8dbd14d2e30e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/m2_eval_summary.md`。

核心发现：
- **Qwen random mean R@1 = 0.5697**，是目前最强 baseline；embedding mean = 0.5774 但仅 2 seeds，Δ 几乎为零（−0.0008）
- **Pilot 阶段的 embed 优势在 full scale 消失**，StarCoder 尤其明显（pilot +0.0156 → full −0.0232）
- 18 个 subrun 完成 8 个，运行中 2 个，待跑 8 个
- 总体覆盖率 44%，random 两个模型均已完成，embedding/dataflow 缺口较大

---
