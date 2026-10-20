# exp deepseek traj func v2 s123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deepseek-traj-func-v2-s123_20260516T133725_result.json`
- **Structured JSON:** [`d0dfe33e1ee5fd98b4ef.json`](../../sessions/d0/d0dfe33e1ee5fd98b4ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s123 已成功启动，确认 resolved/unresolved 格式（与 s42 一致的 `train_traj_verifier.py`）。

**汇报：**

| 项目 | s42 (cuda:2) | s123 (cuda:3) |
|------|-------------|---------------|
| PID | 511676 | 513110 |
| GPU 显存 | 17347 MiB | 15901 MiB |
| Total steps | 756 | 756 |
| 进度 | 260/756 (epoch 2) | 3/756 (epoch 1) |

- **PID**: 513110
- **Total steps**: 756（3 epochs × 252 steps/epoch）
- **预估时间**: ~3.9s/it × 756 steps ≈ 49 分钟
- **配置与 s42 完全一致**：batch_size=2, grad_accumulation=16, lr=2e-4, epochs=3, lora_rank=16, lora_alpha=32，仅 seed/output_dir/run_name 不同
- **日志**: `/tmp/deepseek_traj_v2_s123.log`
- **输出目录**: `/root/autodl-tmp/checkpoints_deepseek_traj_v2_s123/`

---
