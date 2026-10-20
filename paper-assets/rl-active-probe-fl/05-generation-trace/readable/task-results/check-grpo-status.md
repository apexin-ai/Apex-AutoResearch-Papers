# check grpo status

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grpo-status_20260514T081411_result.json`
- **Structured JSON:** [`b5ca4413986ed131f1ec.json`](../../sessions/b5/b5ca4413986ed131f1ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GRPO 训练 — **DONE (失败性完成)**

- 73/73 steps 全部跑完，耗时 2481s (~41 min)，EXIT_CODE=0
- **严重问题：全程 reward = 0.0**
  - fix_based_reward: 0.0
  - probe_execution_bonus: 0.0
  - probe_dependence_reward: 0.0
  - frac_reward_zero_std: 1.0（所有 sample reward 方差为 0）
- completions/clipped_ratio: **1.0**（所有生成都撞 512 token 上限，无一自然终止）
- loss: 0.0, grad_norm: ~0.0009（模型几乎没学到东西）
- Checkpoints: `checkpoint-50`, `checkpoint-73`（在 `/root/autodl-tmp/diagprobe/checkpoints/grpo/`）
- wandb offline run: `offline-run-20260514_151415-v93btbiu`

**根因**：模型生成全部在 think/reason 阶段消耗完 512 token，从未输出有效 probe 代码，导致所有 reward 信号为 0，训练无效。

---

### 2. eval-base — **DONE**

- 202 samples，模型：Qwen3-8B base（无 LoRA）
- 所有指标为 0：
  | Metric | Mean |
  |---|---|
  | debug_accuracy | 0.000 |
  | probe_executed | 0.000 |
  | probe_diagnostic | 0.000 |
  | probe_dependent | 0.000 |
  | probe_generation_rate | 0.005 |

- 仅 1/202 个 sample 生成了 probe（0.5%），其余全部在 `&lt;think>` 中做推理分析，未输出实际 probe 代码
- 结果文件：`/root/autodl-tmp/diagprobe/results/eval_base.json`

---

### 3. Qwen3-30B-A3B 下载 — **Running (缓慢)**

- 正在下载 shard 4/16 (41%) 和 shard 5/16 (49%)
- 已完成 4 个完整 shard（1,2,3,7），已下载 15GB
- 速度：~480-530 kB/s
- 总大小约 16 shards × 3.73GB ≈ 60GB，按当前速度预计还需 **十几小时**

---

### 4. GPU 状态

两张 GPU 均空闲（0 MiB, 0% utilization），GRPO 和 eval-base 都已结束。

---

### 关键结论

GRPO 训练和 base eval 都暴露同一问题：**max_completion_length=512 太短**，模型的 `&lt;think>` 推理就消耗完了全部 token，根本没机会输出 probe 代码。需要增大 completion length 或调整 prompt 让模型跳过冗长推理直接输出 probe。

---
