# ops eval s0 l005 cuda1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_s0_l005_cuda1_20260525T181347_result.json`
- **Structured JSON:** [`35f964e2fe873b1a7b95.json`](../../sessions/35/35f964e2fe873b1a7b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 还在加载中（模型权重加载中，尚未占满显存）。日志显示已在创建模型，进程正常运行。

**总结：**
- `eval_pi05_a1_30k_s0_l005_r4` 已成功启动在 westd-35807 cuda:1
- Checkpoint: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000`
- 输出路径: `/root/autodl-tmp/eval_results/eval_s0_l005_30k_final.json`
- 修正了两个 CLI 错误：`--checkpoint_path` → `--checkpoint`，添加了 `--suite safelibero_object` 和 `--pi05`
- tmux session: `eval_pi05_a1_30k_s0_l005_r4`，PID 6658

---
