# ops bjb1 fix offload and resume v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_fix_offload_and_resume_v2_20260522T020852_result.json`
- **Structured JSON:** [`bf71c3da31a7866a83f0.json`](../../sessions/bf/bf71c3da31a7866a83f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认成功：

- **PID**: 376153 (tmux session: `exp029_c_prime_resume_mt50`)
- **GPU**: cuda:0 = 11095 MiB, cuda:1 = 11095 MiB
- **Resume**: 成功从 `global_step_5` 恢复
  - `[Rank 0] Loaded model from .../global_step_5/actor/model_world_size_2_rank_0.pt`
  - `[Rank 1] Loaded optimizer from .../global_step_5/actor/optim_world_size_2_rank_1.pt`
  - lr_scheduler + rng 也已恢复
- **optimizer_offload**: false ✓
- **max_turn**: 50 ✓
- **无 device mismatch 错误** ✓
- **W&B run ID**: `u6jn1njs` — https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/u6jn1njs

---
