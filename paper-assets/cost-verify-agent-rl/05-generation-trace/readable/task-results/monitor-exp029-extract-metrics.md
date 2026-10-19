# monitor exp029 extract metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029_extract_metrics_20260516T215648_result.json`
- **Structured JSON:** [`84ba28b2e6cb412f15e4.json`](../../sessions/84/84ba28b2e6cb412f15e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B tool has a configuration issue. Based on the log data, here are the exp029 metrics:

## exp029_episode_level Metrics

| Metric | Step 0 (val_before_train) | Step 1 (train) |
|--------|--------------------------|----------------|
| **success rate** | 12.5% (val) | 17.97% (train) |
| **pass@N** | pass@1: 12.5% | pass@8: 56.25% |
| **entropy** | — | 0.0278 |
| **mean reward** | 1.25 (val@32) | 1.797 |
| **KL (ppo_kl)** | — | 0.000289 |
| **KL loss** | — | 0.00887 |
| **pg_clipfrac** | — | 0.088% |
| **grad_norm** | — | 1.459 |
| **action_is_valid** | 78.3% | 68.2% |
| **response_length** | 7088 | 12689 (mean) |
| **time/step** | — | 1837s (~30.6min) |

**补充信息:**
- 实验仅完成 **1 个训练步** (step 1)，step 0 是 val_before_train
- 日志最后写入时间 2026-05-17 05:57，log 末尾仍在写 warnings（实验可能还在跑 step 2 的 rollout）
- batch_size=128, mini_batches=8, group_size=8 (16 env_groups × 8)
- val 用 32 episodes (32 env_groups × 1)，满足 ≥16 约束
- 模型来源: `qwen3_exp021_ragen_sft_v4`

---
