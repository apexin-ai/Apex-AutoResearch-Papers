# ops westb grpo verify conflict cka sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_grpo_verify_conflict_cka_sft_20260517T134405_result.json`
- **Structured JSON:** [`43c43afa2575ef6dc380.json`](../../sessions/43/43c43afa2575ef6dc380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### 1. GPU 状态 + 冲突解决 ✓

- **PID 715803**（旧 CKA eval）在 **cuda:1** 上占 12994MiB，已 kill
- **PID 719684**（grpo_random_20）在 **cuda:1** 上，kill 后显存从 25582MiB 扩展到 43834MiB，GPU-Util 100%，运行正常
- **cuda:0**：完全空闲，0MiB，可用

### 2. cka_only eval + SFT 参数确认

- **PID 710618**（cka_only eval）已结束（/proc/710618 不存在）
- **结果文件已生成**：`eval_cka_only_20_n200.json`
  - accuracy = **38.5%** (77/200)
  - eos_rate = 56%，avg_response_length = 2490
  - 44% 的 response 被截断到 4096 tokens
- **cuda:0 空闲**，可用于 SFT
- **`--save_strategy no` 已支持**：`sft_recovery.py` 接受 `{no, epoch, steps}` 三种选项

### 3. frac_zero_std 检查

- `frac_zero_std`、`zero_std`、`collapse` 在 `train_grpo_v5.py` 和整个 `src/` 目录中**均不存在**
- **未内置**。当前只有一个 `RewardDesertCallback`（监测连续 zero reward 并 early stop，patience=50 log events）
- per-step logging 通过 `logging_steps=10` 控制，但只记录 TRL 默认 metrics，没有自定义的 std 监控

### 4. grpo_random_20 初始 metrics

- 刚启动（21:44:24），log 显示 **0/100 steps，0%**，尚无训练 metrics 输出
- 配置确认：beta=0.01, loss_type=dapo, format_reward=0.1, temperature=0.4, repetition_penalty=1.15, optimizer=adamw_bnb_8bit
- 基于 `sft_random_20` 模型，wandb run: `z9nqlucg`

---
