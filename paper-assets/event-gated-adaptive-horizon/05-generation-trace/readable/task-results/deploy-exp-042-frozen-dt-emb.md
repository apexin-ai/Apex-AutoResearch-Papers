# deploy exp 042 frozen dt emb

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_042_frozen_dt_emb_20260522T021423_result.json`
- **Structured JSON:** [`98cf3a2b9cb11ef5ffa0.json`](../../sessions/98/98cf3a2b9cb11ef5ffa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**exp_042_frozen_dt_emb_walker** 已在 bjb1-40020 上启动 (PID 251331)，状态 RUNNING。

关键点：
- **无需新增代码** — `dt_emb_freeze` 配置已存在于 `configs.yaml`（默认 false）和 `models.py:96-98`（WorldModel.__init__ 中冻结 `_dt_embedding.weight`），功能与任务要求的 `freeze_dt_emb` 完全一致
- 实验命令使用 `--dt_emb_freeze True`（而非 `--freeze_dt_emb True`），匹配已有配置名
- `gate_dt_embed_dim` 默认 32（与 008d 一致）
- 日志路径: `logdir/exp_042_frozen_dt_emb_walker.log`
- 210k steps，预计 ~4-6 小时

---
