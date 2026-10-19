# urgent phase1 full cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_phase1_full_cleanup_20260521T210225_result.json`
- **Structured JSON:** [`243bff43ba25783c14d0.json`](../../sessions/24/243bff43ba25783c14d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

```
=== westd 清理 ===
GPU 残留进程: 已清理 (PID 769407, GPU 0, 90458 MiB)
磁盘: 清理前 47 GB → 清理后 110 GB (删了 exp029-seed7 21G + exp029-seed7-len-penalty 41G + ray sessions 1.5G)
GPU 状态: GPU 0=0 MiB, GPU 1=0 MiB, GPU 2=0 MiB, GPU 3=0 MiB

=== bjb1 清理 ===
high_kl: 已结束（无 GPU 进程）
GPU 状态: GPU 0=0 MiB, GPU 1=0 MiB
磁盘: 80 GB 可用

=== Phase 2 准备 ===
max_new_tokens 位置:
  - agent_proxy.py:74 — max_tokens=ro_config.response_length (per-turn，每次 LLM 调用)
  - base.yaml:56 — response_length: 400 (single-turn response length)
  - config/envs.yaml — max_tokens: 100~512 (仅用于 prompt 提示词，不控制 rollout)
  - base.yaml:90 — max_response_length: null (per-trajectory 上限，当前未启用)
当前值: 400 tokens per turn (base.yaml default)
len_penalty 代码: 仍在（未 revert）— agent_trainer.py 有大量 diff，包括 step_rewards import、_adjust_token_rewards_with_step_penalties 函数、compute_advantage 新增参数 (invalid_action_penalty_coef, reward_include_step_penalties 等)

=== Seed 4 HF checkpoint ===
存在 — /root/autodl-tmp/checkpoints/exp029-seed4/global_step_15_hf/ (3.8G)
symlink: qwen_exp029_seed4_step15_hf → exp029-seed4/global_step_15_hf

=== 崩溃 seed step 5 checkpoint ===
Seed 7 step 5: 存在 (actor/ 子目录, 非 HF 格式)
Seed 8 step 5: 存在 (actor/ 子目录, 非 HF 格式)
```

---
