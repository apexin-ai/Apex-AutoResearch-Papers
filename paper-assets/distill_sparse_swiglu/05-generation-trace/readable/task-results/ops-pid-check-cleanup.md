# ops pid check cleanup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pid-check-cleanup_20260516T022237_result.json`
- **Structured JSON:** [`408648b032aabc234054.json`](../../sessions/40/408648b032aabc234054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部清理完成。

---

## 报告

### PID 存活状态

| PID | 实验 | 状态 | 运行时长 |
|-----|------|------|----------|
| 190830 | `lm_eval_teal_50pct` (cuda:1) | **存活** | 24min49s |
| 191335 | `lm_eval_kl_30pct_s42` (cuda:0) | **存活** | 24min07s |
| 174840 | `lm_eval_mistral_downstream` | 已死亡 | — |
| 153249 | `lm_eval_dense_test` | 已死亡 | — |
| 123231 | `eval_spon_supp_retry` | 已死亡 | — |
| 123984 | `bce_isocompute_s42_v2` | 已死亡 | — |

### GPU 占用

| GPU | 显存占用 | 利用率 | 当前任务 |
|-----|---------|--------|----------|
| cuda:0 | 16.4 / 97.9 GB (17%) | 89% | `lm_eval_kl_30pct_s42` |
| cuda:1 | 20.0 / 97.9 GB (20%) | 90% | `lm_eval_teal_50pct` |

两张卡都在活跃计算，显存占用不高（模型推理为主）。

### 活跃实验进度

**`lm_eval_teal_50pct`** (PID 190830, cuda:1):
- 当前阶段：GSM8K generate_until，993/1319 (75%)
- 速度：~1.3s/it
- 预计剩余：~7 分钟完成 GSM8K → 之后应该就结束了（4 个 task 中最后一个的生成阶段）

**`lm_eval_kl_30pct_s42`** (PID 191335, cuda:0):
- 当前阶段：GSM8K generate_until，506/1319 (38%)
- 速度：~1.8s/it（波动较大，1.3-2.8s/it）
- 预计剩余：~25 分钟完成 GSM8K

### 已清理的僵尸实验

| 实验 | 原因 | Registry 操作 |
|------|------|--------------|
| `lm_eval_mistral_downstream` | tmux session 被 teal_50pct 启动时覆盖 | conclusion=failed → DONE |
| `lm_eval_dense_test` | 早期探索，tmux 消失 | conclusion=failed → DONE |
| `eval_spon_supp_retry` | tmux 消失，被后续实验覆盖 | conclusion=failed → DONE |
| `bce_isocompute_s42_v2` | tmux 再次被外部终止（与 v1 同模式） | 已有 conclusion=killed → DONE |

### 调度建议

- `lm_eval_teal_50pct` 约 7 分钟后完成，之后 cuda:1 释放
- `lm_eval_kl_30pct_s42` 约 25 分钟后完成，之后 cuda:0 释放
- `bce_isocompute_s42_v2` 已两次被 tmux 终止，如果要重跑建议等两个 lm_eval 都结束后，在空闲 GPU 上单独执行

---
