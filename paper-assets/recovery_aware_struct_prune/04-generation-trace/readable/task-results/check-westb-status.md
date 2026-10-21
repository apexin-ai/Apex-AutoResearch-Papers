# check westb status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_status_20260516T200709_result.json`
- **Structured JSON:** [`7d5b897cea958796f397.json`](../../sessions/7d/7d5b897cea958796f397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 使用

| GPU | 进程 | VRAM | Util |
|-----|------|------|------|
| cuda:0 | eval_grpo_rasp_25 (PID 639423) | 28.9/97.9 GB | 99% |
| cuda:1 | grpo_rasp_rlvr_20 (PID 635524) | 71.7/97.9 GB | 100% |

---

### 1. `grpo_rasp_rlvr_20` — **RUNNING** (cuda:1)
- 进度: **14/100 steps** (~1h35m elapsed, ~9h40m remaining)
- 速度: ~405s/step
- W&B run: `hmhrxpn0` (started 5/17 02:31 UTC)
- 预计完成: 5/17 ~12:00 UTC

### 2. `grpo_stage2_standard_20_v8` — **COMPLETED (partial, step 50/100)**
- W&B run: `q34vz8j2` (started 5/15 22:47)
- 只保存了 checkpoint-50，无最终模型 → 可能被 `reward_desert_patience` 早停或手动 kill
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50/`

### 3. `grpo_stage2_rasp_20_v9` — **COMPLETED (success)**
- 最终模型已保存（model.safetensors + config 全套）
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/`
- 有 checkpoint-10

### 4. `grpo_standard_25` — **FAILED/KILLED**
- W&B run: `halzuhy3` (started 5/16 16:13)
- log 停在 `0%|  | 0/100`，无 output dir → 启动后立即失败或被 kill
- 输出目录不存在

### 5. `eval_grpo_rasp_25` — **RUNNING** (cuda:0, tmux session)
- 正在评估 grpo_rasp_25 模型的 GSM8K（1319 samples）
- 进度: 59/1319 (~19min elapsed)
- 中间结果 @50 samples: **acc=0.5000**, eos_rate=94%, avg_len=385

---
