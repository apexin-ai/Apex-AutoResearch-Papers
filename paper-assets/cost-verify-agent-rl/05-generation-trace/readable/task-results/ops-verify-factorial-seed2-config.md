# ops verify factorial seed2 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-factorial-seed2-config_20260518T102709_result.json`
- **Structured JSON:** [`6ec02f6e2ec3b6b4e7fc.json`](../../sessions/6e/6ec02f6e2ec3b6b4e7fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 对比结果：seed1 vs seed2 config 完全一致

### 所有关键参数匹配 ✓

| 参数 | seed1 | seed2 |
|---|---|---|
| kl_loss_coef | 0.01 | 0.01 |
| total_training_steps | 15 | 15 |
| ppo_max_token_len_per_gpu | 65536 | 65536 |
| ppo_mini_batch_size | 16 | 16 |
| env_groups (train) | 16 | 16 |
| group_size (train) | 8 | 8 |
| learning_rate | 1e-6 | 1e-6 |
| context_window_mode | step_independent | step_independent |
| advantage_mode | episode_level | episode_level |
| adv_estimator | grpo | grpo |

### 差异（共 3 处，全部预期）

1. **seed block** — seed1 无显式 seed（用默认值），seed2 显式设置 `seed.train: 43, seed.val: 123` ✓ 预期
2. **experiment_name** — `factorial-h2-episode-adv` vs `factorial-h2-episodeadv-seed2` ✓ 预期
3. **checkpoint 路径** (local_log_dir / default_local_dir) — 对应 experiment_name 变化 ✓ 预期

**无意外差异。** 两个 config 除 seed/命名/路径外完全相同。

---
