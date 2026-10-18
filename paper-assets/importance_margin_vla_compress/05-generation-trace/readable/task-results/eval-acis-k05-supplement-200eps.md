# eval acis k05 supplement 200eps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acis_k05_supplement_200eps_20260518T132147_result.json`
- **Structured JSON:** [`37f2d8f39b1aed8d71ab.json`](../../sessions/37/37f2d8f39b1aed8d71ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 运行正常，正在 eval task 6-9。

**完成摘要：**
- GPU 1 (cqa1-33015) 空闲，已确认
- 从 westd-27271 传输 checkpoint (`libero_imm_twostage_fullft/stage1_done/checkpoint.pt`, 1.2GB) 到 cqa1-33015
- Dry-run 2 episodes 验证通过（0% SR，符合预期）
- 已通过 `submit_training_job` 提交正式 eval：
  - `exp_id`: `eval_acis_k05_supplement_200eps`
  - tasks 6,7,8,9 x 50 eps = 200 episodes
  - `--mode acis_prune`, `--seed 42`（与原始一致）
  - `--pruning_method zero_mask`（默认值，与原始一致）
  - cuda:1, tmux session
- Registry 已更新：RUNNING, parent=`eval_stage1only_object_v2_fixed`
- 预计运行时间：每 episode ~10s x 200 eps ≈ 30-40 分钟

---
