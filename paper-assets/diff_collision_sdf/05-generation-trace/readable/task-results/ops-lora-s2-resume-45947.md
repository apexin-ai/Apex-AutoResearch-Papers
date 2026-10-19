# ops lora s2 resume 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_s2_resume_45947_20260527T024701_result.json`
- **Structured JSON:** [`32e8c8ab620e1d5e7218.json`](../../sessions/32/32e8c8ab620e1d5e7218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Resume 成功，已从 step 22000 恢复训练，进度 73% (22000/30000)。

汇总结果：

### Part 1: Checkpoint 完整性 ✅
- 路径: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/22000/`
- `model.safetensors` 7.5GB, `optimizer.pt` 130MB, `metadata.pt`, `norm_stats.json` 齐全

### Part 2: Resume 命令 ✅
- 脚本支持 `--resume` flag（line 68），自动定位最新 checkpoint

### Part 3: 训练已提交 ✅
- exp_id: `train_pi05_lora_baseline_s2_resume`
- timeout: 48h
- 已从 step 22000 成功恢复，剩余 8000 steps

### Part 4: tmux timeout 根因
- **没有 tmux 配置文件**（`/root/.tmux.conf` 和 `/etc/tmux.conf` 均不存在）
- **timeout 来自 `submit_training_job` 的 `timeout` 命令包装**，原始任务用了 `timeout 86400`（24h），可在 ps 输出中看到。这不是 tmux 的问题，是 `timeout_hours=24` 参数的直接效果。

### Part 5: 另一个训练健康 ✅
- `train_pi05_a1_obj_s2_l01_high` (cuda:1) 正在运行，PID 425058，CPU 170%
- 使用 `timeout 172800`（48h），有足够余量
- 有多个 compile_worker 和 multiprocessing fork 子进程在工作

---
