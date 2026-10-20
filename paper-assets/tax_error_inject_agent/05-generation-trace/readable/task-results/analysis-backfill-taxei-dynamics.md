# analysis backfill taxei dynamics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_backfill-taxei-dynamics_20260515T024707_result.json`
- **Structured JSON:** [`87acda0bf8400b200b8a.json`](../../sessions/87/87acda0bf8400b200b8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册完成。

**总结**：
- 从 `/root/autodl-tmp/tax_error_inject_agent/output/` 下找到了 taxei_10 和 taxei_25 的成功训练记录（非空的 `checkpoints/` 目录是 OOM 的残留，实际数据在 `output/` 目录）
- 提取了完整的 training dynamics：两个实验各 328 条记录，步数 1–1635
- 最终指标验证通过：taxei_10 loss=0.308 / acc=0.888，taxei_25 loss=0.285 / acc=0.893
- JSON artifact 已保存并注册：`art_20260515_695054`，类型 `data`，路径 `_project/data/training_dynamics_taxei_10_25.json`

---
