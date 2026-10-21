# ops fix bce v2 registry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_bce_v2_registry_20260515T201921_result.json`
- **Structured JSON:** [`e4251de077336e0ae01c.json`](../../sessions/e4/e4251de077336e0ae01c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### (1) PID 129187 完整命令
```
python src/train.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --loss_type bce --num_steps 1000 --warmup_steps 100 \
  --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 \
  --sparsity_target 0.5 --sparsity_reg_weight 2.0 \
  --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42 \
  --gradient_checkpointing --log_every 100 --save_every 250 \
  --wandb_run_name bce_isocompute_v2_s42
```
进程树：PID 129182 (bash wrapper) → 129186 (timeout 7200) → **129187** (python)，GPU 显存 90.7GB。

### (2) reg_weight = **2.0** 
满足 Director 要求（≥0.2）。注意这比旧版大幅提高（之前默认可能是 0.1），且 num_steps 从 2700 改为 **1000**（iso-compute 策略变了：不再是 FLOPs 匹配 2700 步，而是同步数 1000 步 + 高 reg_weight 逼 sparsity 到 0.5）。

### (3) 当前训练进度
| 指标 | 值 |
|------|-----|
| 进度 | Step 200/1000 (20%) |
| loss | 0.6802 |
| bce | 0.6652 |
| reg | 0.0171 |
| **sparsity** | **0.501** (已收敛到 target 0.5) |
| 速度 | 1.05 s/step |
| 预计剩余 | ~14 min |

Sparsity 趋势良好：Step 100 = 0.502, Step 200 = 0.501，reg_weight=2.0 有效地将 sparsity 锁定在 target 附近。

### (4) 日志路径
`~/runs/distill_sparse_swiglu/bce_isocompute_v2_s42.log`

### (5) Registry 更新
- **PID/log_path**：registry 中已有 PID 129182（bash wrapper，正确）和正确日志路径，无需更新
- **Status**：当前为 ANALYZING，state machine 不允许回退到 RUNNING，已在 notes 中标注实际仍在训练
- **Notes**：已更新，记录进程树、训练进度、状态说明

### 异常说明
用户提到的 PID 127703 已死（介于旧 PID 125967 和当前 129187 之间），可能是中间一次短命的重启。当前运行是第三次提交，状态正常。

---
