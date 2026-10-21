# ops dreeam gpu migration

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_dreeam-gpu-migration_20260515T142649_result.json`
- **Structured JSON:** [`628adaddbade72bb7f05.json`](../../sessions/62/628adaddbade72bb7f05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终 GPU 分布

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| cuda:0 | 1,701 / 32,607 MiB | PID 178055 — CED reranker（仅此一个，已无冲突） |
| cuda:1 | 14,083 / 32,607 MiB | PID 197386 |
| cuda:2 | 1,915 / 32,607 MiB | PID 213006 — **DREEAM teacher**（正在加载数据，显存会增长） |
| cuda:3 | 1,467 / 32,607 MiB | PID 208155 |

**DREEAM teacher 新 PID: 213006**（tmux session: `plan_004_dreeam_baseline`，日志: `~/runs/faith-evidence-ie/plan_004_dreeam_baseline.log`）

cuda:0 现在只有 CED reranker (PID 178055)，OOM 风险已消除。

注意：wandb 未在服务器配置，本次训练以 `WANDB_MODE=disabled` 运行（与原脚本一致）。如需 wandb 追踪，需先在服务器上 `wandb login`。

---
