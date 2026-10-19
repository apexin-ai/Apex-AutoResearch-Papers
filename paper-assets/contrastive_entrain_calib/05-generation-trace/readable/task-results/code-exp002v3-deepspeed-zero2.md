# code exp002v3 deepspeed zero2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002v3-deepspeed-zero2_20260519T083215_result.json`
- **Structured JSON:** [`07a7aaf9e888dc838e63.json`](../../sessions/07/07a7aaf9e888dc838e63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All prerequisite data files present. Here's the final compatibility report.

---

## exp-002v3 DeepSpeed ZeRO-2 转换完成报告

### 完成的 7 步操作

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 找到 exp-008v3 DS 参考配置 | ✅ | `/root/contrastive_entrain_calib/training/ds_config_zero2.json` |
| 2. 创建 exp-002v3 DS 配置 | ✅ | `ds_config_exp002v3.json` (ZeRO-2, bf16, grad_accum=16, micro_batch=1) |
| 3. 修改 run script | ✅ | `sys.path` → 本地, `deepspeed=`, `report_to="none"` |
| 4. 创建 launch script | ✅ | `launch_exp002v3.sh`, GPU 0+3, `NCCL_P2P_DISABLE=1` |
| 5. Dry-run 验证 | ✅ | JSON 语法, Python AST, DCGRPOConfig import 均通过 |
| 6. DeepSpeed 兼容性 | ✅ | deepspeed 0.19.0, `recalibrate_direction()` 用 `accelerator.unwrap_model()` |
| 7. 报告 | ✅ | 本报告 |

### dcgrpo_trainer.py 补丁 (8/8 applied)

- 789 → 919 行
- `r1_scale_factor`, `recalibration_interval`, `calibration_data_path` 添加到 config + init
- `compute_r1`: dot product → cosine similarity, tanh → `r1_scale_factor * mean`
- `recalibrate_direction()` 方法已加入, 用 `self.accelerator.unwrap_model()` 兼容 DeepSpeed
- `r3_model_name` 默认值修正为 `cross-encoder/nli-deberta-v3-base`

### 关键参数确认（未改动）

| 参数 | 值 |
|------|-----|
| R1_WEIGHT | 0.4 |
| R3_WEIGHT | 0.6 |
| R2_WEIGHT | 0.0 |
| R1_SCALE_FACTOR | 5.0 |
| lora_alpha | 64 |
| lora_r | 64 |
| recalibration_interval | 500 |
| max_steps | 8000 |
| seed | 42 |

### 环境确认

- 4x GPU (GPU 0, 3 可用)
- DeepSpeed 0.19.0
- directions.pt, calibration data, Qwen3-8B 模型均存在

### 启动命令

```bash
cd /root/contrastive_entrain_calib/training
bash launch_exp002v3.sh
```

---
