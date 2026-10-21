# setup eval auto trigger s2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_eval_auto_trigger_s2_20260527T190819_result.json`
- **Structured JSON:** [`3a167f9e8ca96a972a43.json`](../../sessions/3a/3a167f9e8ca96a972a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sentinel 正在运行：

- **Sentinel PID**: 552915（实际 bash 进程），正在 sleep 60 等待轮询
- **训练 PID**: 425058（157% CPU，仍在运行 step ~25567/30000）
- **GPU 0**: 空闲，eval 就绪

---

**报告：**

| 项目 | 值 |
|------|-----|
| Sentinel PID | 552915 |
| Sentinel 日志 | `/root/autodl-tmp/auto_eval_s2_sentinel.log` |
| 监控的训练 PID | 425058 |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/30000` |
| Eval GPU | cuda:0 |
| Eval 日志 | `/root/autodl-tmp/eval_results/eval_sdf_s2_l01_30k_auto.log` |
| Eval 命令 | `python scripts/eval_safelibero.py --checkpoint <上述路径> --config_name pi05_libero --model_type lora_baseline --pi05 --suite safelibero_object --safety_level II --n_episodes 50 --seed 7 --gpu 0` |
| 预计触发时间 | ~08:48 UTC May 27（训练 85%，4433 steps × 4.61s/step ≈ 5.7h） |

Eval JSON 会由脚本自动输出到 `/root/autodl-tmp/eval_results/` 目录（文件名由 eval_safelibero.py 自动生成，基于 checkpoint 路径和参数）。

---
