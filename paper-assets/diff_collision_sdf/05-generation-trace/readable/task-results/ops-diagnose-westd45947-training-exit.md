# ops diagnose westd45947 training exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_westd45947_training_exit_20260523T003046_result.json`
- **Structured JSON:** [`b438d9161094157219c2.json`](../../sessions/b4/b438d9161094157219c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个训练都正常运行中，Cron 报告为误报。**

| 实验 | tmux session | 进程 | GPU | 当前 step | 状态 |
|------|-------------|------|-----|-----------|------|
| train_pi05_a1_obj_l005 | 存活 | 运行中 | cuda:0 (19.1/97.9 GB, 100%) | ~717/30000 | RUNNING |
| train_pi05_a1_obj_l01 | 存活 | 运行中 | cuda:1 (19.1/97.9 GB, 51%) | ~716/30000 | RUNNING |

- 训练于 08:14 启动，已运行约 14 分钟，~1.21s/step
- 预计总时长 ~10h（不是之前估的 15h，速度比预期快）
- 尚无 checkpoint（save_interval=2000，首个 checkpoint 在 step 2000）
- loss 正常下降：action ~0.14, sdf ~0.035, ee ~0.10

两个实验状态保持 RUNNING 不变，无需更新 registry。

---
