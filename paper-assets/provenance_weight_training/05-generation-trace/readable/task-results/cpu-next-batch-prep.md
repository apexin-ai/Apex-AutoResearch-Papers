# cpu next batch prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_next-batch-prep_20260515T154637_result.json`
- **Structured JSON:** [`c8a43165b43781222c7c.json`](../../sessions/c8/c8a43165b43781222c7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。关键发现：

**nmin4_seed42** — 代码逻辑确认 n_min=4 (=batch_size) 会强制 b*=0（ESS(0)=4 刚好满足约束，任何 b>0 都不满足）。命令就绪，registry 已有 PREPARING 条目。

**ess_only_seed123** — 基于 ess_only_seed42 改 seed=123，命令就绪，需新建 registry entry。

**所有文件验证通过**：训练脚本、模型、数据、eval holdout 均存在，输出目录干净无残留。

**需你决策**：
1. nmin4 是否加 inline eval（run script 有，但当前其他实验都不加）
2. GPU 分配（4 个 tau sweep 完成后全部释放）

详细报告已存入 `artifacts/next_batch_prep.md`。

---
