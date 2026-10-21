# ops gpu1 a1 ee disp reeval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1_a1_ee_disp_reeval_20260525T224412_result.json`
- **Structured JSON:** [`b502e9cdcc1396dbeac6.json`](../../sessions/b5/b502e9cdcc1396dbeac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报阻塞点。需要用户决策。

**问题 1：A1 checkpoint 命名与文档不一致**
- 文档要求路径：`/root/autodl-tmp/checkpoints/a1_sdf_object_pudding/a1_lora_object_pudding_seed0/best/` —— **不存在**
- 实际存在的 a1 目录是 `a1_sdf_pi05_object_pudding/`（注意是 `pi05`），且 **seed0 没有 `best/` 子目录**，只有 step `30000`：
  - `a1_sdf_pi05_object_pudding_seed0_l005/30000/`
  - `a1_sdf_pi05_object_pudding_seed0_l01/30000/`
  - `a1_sdf_pi05_object_pudding_seed0_l005_p2abl/`（待确认）
- 有 `best/` 的是 seed1/seed2 的两个 lambda 配置（l005、l01）和 spatial_bowl seed0_l005

**问题 2：GPU 1 不空闲**
- GPU 1：9014 MiB / 52% util（PID 257150 占用）
- 空闲的是 **GPU 2**（1 MiB / 0% util）
- GPU 0 和 3 满载（27 GB / 100%）

请决策：
1. 用哪个 A1 checkpoint？（seed0_l005/30000、seed0_l01/30000、seed0_l005_p2abl，或换成 seed1/seed2 的 best？）
2. 改用 GPU 2 跑（GPU 1 被占用）？

---
