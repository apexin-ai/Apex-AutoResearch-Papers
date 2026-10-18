# ops c4ext eval westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext-eval-westd41074_20260520T111059_result.json`
- **Structured JSON:** [`00ca8e834126b768a078.json`](../../sessions/00/00ca8e834126b768a078.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已启动，进入 Task 0 inference。

总结：
- **修复了 3 个 bug**：
  1. `obs_to_inputs`: camera key 映射不匹配（`observation.images.image` → 需从 `obs['pixels']['image']` 取）
  2. `predict_action`: `generate()` 用 `inputs_embeds` 时只返回新 token，不含 input prefix，修复 slicing
  3. `n_envs`: 从 `args.num_episodes`(50) 改为 1，避免同时创建 50 个 MuJoCo 环境
- **正式 eval 已提交**：tmux session `eval_sc_m128_20k`，westd-41074 GPU 0
- **日志**：`/tmp/eval_sc_m128_20k_full.log`
- **输出**：`eval_results/eval_openvla_sc_m128_vtconly_20k_seed42.json`
- **预计时间**：~2s/step，280 max steps × 50 ep × 10 tasks = 最多 ~78h（实际会短很多，多数 episode 早停）
- **注意**：模型每步输出相同 action，可能是 overfitting 的表现，但需要完整 eval 才能判断

---
