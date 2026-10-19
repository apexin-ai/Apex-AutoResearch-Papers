# ops baseline ckpt prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_baseline_ckpt_prep_20260521T234039_result.json`
- **Structured JSON:** [`e9f317121aabde809ee7.json`](../../sessions/e9/e9f317121aabde809ee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SCP 完成。文件大小与源完全一致：
- model.safetensors: 7,011,543,960 bytes ✓
- optimizer.pt: 12,550,741,381 bytes ✓
- metadata.pt: 3,187 bytes ✓
- assets/ 目录 ✓

---

## 汇报

**1. Baseline checkpoint 状态：已 scp 完成**
- 路径：`/root/autodl-tmp/checkpoints/baseline_object_pudding_eval/best/`
- 来源：westd-35807 的 `baseline_object_pudding_seed0/best/`
- 文件完整（model.safetensors 6.5GB + optimizer.pt 11.7GB + metadata.pt + assets/）

**2. --model_type 可选值：`{baseline, a1, a3}`**
- baseline: 纯基线模型
- a1: SDF auxiliary loss
- a3: gradient refiner

**3. Eval 当前进度（eval_v9_a3_refine）**
- PID 263983 仍存活，已运行 2h48m
- 已完成：Task 0（TSR 0%，CAR 8%）、Task 1（TSR 0%，CAR 22%）
- 正在执行：Task 2（pick up the milk），已到 Episode 20/50
- 全部 50 episodes 均走满 300 steps，success=False

---
