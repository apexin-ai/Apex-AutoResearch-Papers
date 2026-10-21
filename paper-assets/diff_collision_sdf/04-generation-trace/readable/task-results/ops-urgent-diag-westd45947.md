# ops urgent diag westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_diag_westd45947_20260525T043854_result.json`
- **Structured JSON:** [`d4c56a5fd5b33efde883.json`](../../sessions/d4/d4c56a5fd5b33efde883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论清晰了。

```
问题1: LoRA baseline（非 SDF 训练）
  脚本: train_pi05_lora_baseline（无 lambda_sdf 参数）
  配置: pi05_lora_baseline_object_pudding, lr=2.5e-05, batch=32, target=30000 steps
  两个 seed 同时启动于 5/24 19:25:
    - seed0 (wandb: fjmhoj37) → GPU 0
    - seed1 (wandb: e1gwkkop) → GPU 1

问题2: 两个 GPU 均无进程，训练已停止
  GPU 0: 0MiB 显存, 无进程 (GPU-Util 100% 但无实际进程，可能是 persistence mode 残留)
  GPU 1: 0MiB 显存, 无进程, 0% util

  最新 checkpoint 时间戳:
    seed0: step 16000 @ 5/25 11:15
    seed1: step 16000 @ 5/25 11:18
  目标 30000 steps, 仅完成 ~53%。训练在 step 16000 后崩溃/退出（距今约 1.5 小时前）。
  /tmp/ 下无对应训练日志文件（train_pi05_lora_baseline_s0/s1.log 不存在），无法从日志确认崩溃原因。
```

---
