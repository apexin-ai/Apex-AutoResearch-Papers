# ops fix wandb offline

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-wandb-offline_20260518T084827_result.json`
- **Structured JSON:** [`fe72bbc5694af9207739.json`](../../sessions/fe/fe72bbc5694af9207739.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

1. **修改位置**：`/root/tbab_multi_turn/scripts/train.py` 第 20 行，在 `import os` 之后插入 `os.environ["WANDB_MODE"] = "offline"`（在 `import wandb` 之前，确保环境变量先于 wandb 导入生效）

2. **dry-run 结果**：condition1 + seed 42，3 步训练全部完成，无任何 error/fail。W&B 日志确认：
   - `wandb: W&B syncing is set to offline in this directory`
   - `[INFO] Running in WANDB offline mode`
   - 训练数据本地保存在 `wandb/offline-run-*` 目录

3. **覆盖范围**：4 个 condition（condition1~4）共享同一个 `train.py`，YAML 只控制实验参数。修一处即全修，8 个实验（4 conditions × 2 seeds）均已覆盖。

---
