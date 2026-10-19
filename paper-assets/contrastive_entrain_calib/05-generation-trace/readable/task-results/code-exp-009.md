# code exp 009

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-009_20260520T022531_result.json`
- **Structured JSON:** [`c7e7b145fd22c026e30b.json`](../../sessions/c7/c7e7b145fd22c026e30b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

345 行，`IMPORT_OK`，dry-run 通过。

---

## 产出总结

### 1. 脚本文件
`/root/contrastive_entrain_calib/training/run_exp009_continuous_probe_grpo.py`（28034 服务器）

### 2. 与 exp-008v3 的 diff

| 位置 | exp-008v3 | exp-009 |
|------|-----------|---------|
| 类名 | `BinaryProbeTrainer` | `ContinuousProbeTrainer` |
| `compute_r1` 返回值 | `1.0 if p_syc <= 0.5 else 0.0` | `1.0 - p_syc` |
| OUTPUT_DIR | `/root/contrastive_entrain_calib/checkpoints/exp008v3_binary_probe_grpo` | `/root/autodl-tmp/checkpoints/exp009_continuous_probe_grpo` |
| logger name | `exp008v3` | `exp009` |
| 日志标识 | `"Binary Probe GRPO"` | `"Continuous Probe Probability GRPO"` |

其余完全相同：R1/R3 权重 (0.25/0.75)、REWARD_LAYERS、probe retrain 每 500 步、max_steps=8000、LoRA r=64、DeepSpeed ZeRO-2、2 GPU。

### 3. Dry-run 验证
`IMPORT_OK` — 模块导入无报错。

### 4. 提交命令
```bash
bash -c "unset CUDA_VISIBLE_DEVICES && cd /root/contrastive_entrain_calib/training && MASTER_PORT=29502 /root/miniconda3/bin/deepspeed --include localhost:1,2 --master_port 29502 run_exp009_continuous_probe_grpo.py"
```

---
