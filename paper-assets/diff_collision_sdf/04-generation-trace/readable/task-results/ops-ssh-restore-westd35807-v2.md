# ops ssh restore westd35807 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ssh_restore_westd35807_v2_20260525T044857_result.json`
- **Structured JSON:** [`1ef7073c2e59662c64a9.json`](../../sessions/1e/1ef7073c2e59662c64a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。注意：任务提到的是 4 个实验（s1_l005, s1_l01, s2_l005, s2_l01），实际有 6 个（还有 seed0_l005/l01），但 seed0 的两个没有 best 目录、没有 wandb_id，只有一个 step 30000 checkpoint。

```
1. SSH: 成功（密钥已复制，免密登录正常）
2. 磁盘: 根=20G/30G (65%), 数据盘=140G/350G (40%)
3. GPU: 4× RTX PRO 6000 Blackwell 96GB, 无训练残留进程（仅 tensorboard + jupyter）
4. Checkpoint 核实（全部跑完 30000 步）:
   - seed1_l005: 路径=/root/autodl-tmp/checkpoints/.../seed1_l005, 最终step=30000, 时间戳=May24 21:24, best_step=16000 (loss=0.01143)
   - seed1_l01:  路径=/root/autodl-tmp/checkpoints/.../seed1_l01,  最终step=30000, 时间戳=May24 21:24, best_step=16000 (loss=0.01168)
   - seed2_l005: 路径=/root/autodl-tmp/checkpoints/.../seed2_l005, 最终step=30000, 时间戳=May24 21:29, best_step=10000 (loss=0.00874)
   - seed2_l01:  路径=/root/autodl-tmp/checkpoints/.../seed2_l01,  最终step=30000, 时间戳=May24 21:32, best_step=10000 (loss=0.00911)
   - seed0_l005: 路径=/root/autodl-tmp/checkpoints/.../seed0_l005, 最终step=30000, 时间戳=May24 19:47, 无best
   - seed0_l01:  路径=/root/autodl-tmp/checkpoints/.../seed0_l01,  最终step=30000, 时间戳=May24 19:47, 无best
5. conda libero: 正常 (Python 3.10.20)
```

所有 4 个主实验（seed1/2 × l005/l01）成功从崩溃恢复并跑完 30000 步，训练时长约 31 小时。seed0 的两个也跑完但缺少 best checkpoint 记录。

---
