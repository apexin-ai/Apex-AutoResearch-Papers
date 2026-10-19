# ops d020 kill restart exp002v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d020-kill-restart-exp002v2_20260518T235500_result.json`
- **Structured JSON:** [`97c43f100e711182db5b.json`](../../sessions/97/97c43f100e711182db5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

前 3 步全部正常运行：

| Step | R1 mean | R1 range | R3 mean | Combined |
|------|---------|----------|---------|----------|
| 1 | -0.0026 | [-0.10, +0.11] | 0.28 | 0.21 |
| 2 | -0.0544 | [-0.16, +0.07] | 0.57 | 0.41 |
| 3 | -0.0601 | [-0.12, +0.05] | 0.84 | 0.61 |

R1 在 [-0.2, +0.2] 范围内稳定运行，tanh saturation 问题已修复。约 26s/step，50 步约 22 分钟后回来做完整 sanity check。

---

**D020 执行总结**：

1. **exp-002 kill**: PID 69020 已 SIGTERM 终止
2. **dcgrpo_trainer.py 同步**: compute_r1 从 `dot product + tanh(raw/20)` 改为 `cosine similarity (dot/||h||)`，已验证无残留 tanh
3. **exp-002v2 训练脚本**: `/root/contrastive_entrain_calib/training/run_exp002v2_dcgrpo_cosine.py`
   - OUTPUT_DIR: `exp002v2_dcgrpo_cosine`
   - R1=0.25, R2=0, R3=0.75, lr=5e-5, max_steps=8000, seed=42, LoRA r=64, num_gen=2
   - recalibration_interval=0
   - 修复了 `compute_rewards` 签名不匹配 bug
4. **训练启动**: PID 122450, GPU 0, tmux session `exp002v2`
5. **初步 sanity check (前 3 步)**: R1 range [-0.16, +0.11]，不再是 ±1 震荡，修复成功

需要约 20 分钟后回来检查前 50 步的完整数据。

---
