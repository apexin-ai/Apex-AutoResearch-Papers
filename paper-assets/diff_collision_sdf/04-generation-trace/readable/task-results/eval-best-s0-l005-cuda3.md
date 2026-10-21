# eval best s0 l005 cuda3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_best_s0_l005_cuda3_20260527T230013_result.json`
- **Structured JSON:** [`0c2af692583107f412ae.json`](../../sessions/0c/0c2af692583107f412ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动并正在加载模型。

**汇报：**

- **实验 ID**: `eval_pi05_a1_best_s0_l005`
- **命令**: `CUDA_VISIBLE_DEVICES=3 python scripts/eval_safelibero.py --checkpoint .../seed0_l005/30000 --model_type lora_baseline --pi05 --suite safelibero_object --safety_level II --n_episodes 50 --seed 7 --gpu 0 --output_path /root/autodl-tmp/eval_results/eval_pi05_a1_best_s0_l005.json`
- **PID**: 907049
- **日志**: `/root/runs/diff_collision_sdf/eval_pi05_a1_best_s0_l005.log`
- **预计完成**: ~30-40 分钟（4 tasks × 50 episodes）

**注意**: seed0_l005 没有 `best/` 目录（只有 `30000/`），使用 30000 作为 best checkpoint。seed1 的 best 在 step 16000，seed2 的 best 在 step 10000——seed0 训练时可能未启用 best checkpoint 保存。

---
