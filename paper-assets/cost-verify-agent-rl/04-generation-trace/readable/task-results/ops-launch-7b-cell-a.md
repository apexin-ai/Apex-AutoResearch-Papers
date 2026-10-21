# ops launch 7b cell a

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-7b-cell-a_20260519T074924_result.json`
- **Structured JSON:** [`c341d576a72eb0cc6f55.json`](../../sessions/c3/c341d576a72eb0cc6f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动！

**汇报：**

| 项 | 状态 |
|---|---|
| GPU 占用 | 0: 42.9G, 1: 47.8G, 2: 47.8G, 3: 47.8G ✅ 全部 4 GPU 在用 |
| PID 828607 (OOD eval) | 已不存在 |
| lr 修改 | 1e-6 → 5e-7 ✅ |
| model_path | 去除尾部 `/` ✅ |
| 入口点修复 | `verl.trainer.main_ppo` → `train.py`（RAGEN 自动设置 `data.train_batch_size`）|
| 训练 PID | 849089（TaskRunner PID 855415） |
| tmux session | `7b_cell_a_h2` |
| W&B run | `irxgmlm2`（8b-cell-a-step-independent-h2） |
| W&B URL | `wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/irxgmlm2` |
| 磁盘 | 86G 可用 (66%) |
| 当前进度 | val_before_train 阶段，正在初始化 AlfredTWEnv（140 games eval_in_distribution） |

启动过程中修了 3 个问题：
1. Hydra config path：`--config-path config` 相对于 `main_ppo.py` 模块路径解析，需用绝对路径或改用 `train.py`
2. 入口点：`train.py` 而非 `verl.trainer.main_ppo`（前者自动设 `data.train_batch_size = env_groups * group_size`）
3. `model_path` 尾部 `/` 触发 assertion

---
