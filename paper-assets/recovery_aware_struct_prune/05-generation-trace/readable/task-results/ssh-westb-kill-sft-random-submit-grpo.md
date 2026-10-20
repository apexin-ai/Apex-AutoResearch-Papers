# ssh westb kill sft random submit grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_kill_sft_random_submit_grpo_20260523T214613_result.json`
- **Structured JSON:** [`6d4d7bb5e0e96bce6f52.json`](../../sessions/6d/6d4d7bb5e0e96bce6f52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交成功，进程在加载模型中。汇报结果：

---

### 1. Kill 结果 & GPU 验证
- PID 327972 (sft_random_20_fixed_v2) 已 kill，GPU 1 已释放（0MiB, 0%）
- GPU 0 仍在跑 `eval_math500_grpo_cka_only_20_fixed`（PID 321428）

### 2. grpo_random_20 checkpoint 状态
- `grpo_random_20/` 和 `grpo_random_20/checkpoint-100/` **不存在**
- `grpo_random_20_retrain/` 存在，根目录有 `model.safetensors`（12.2GB），已用此路径提交

### 3. 提交结果
- **tmux session**: `eval_math500_grpo_random_20_fixed`
- **PID**: 330254（python eval_math500.py）
- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain`
- **GPU**: cuda:1
- **output**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_fixed.json`

### 4. sft_rasp_alpha0p5_20 搜索结果（westb）
- `sft_rasp_alpha0p5_20/` **不存在**
- `sft_alpha0p5_20/` **不存在**
- 有 `grpo_rasp_alpha0p5_20/`（GRPO checkpoint，非 SFT）
- 有 `sft_rasp_alpha3p0_20/`（alpha3.0，非 alpha0.5）
- **结论**：westb 上没有 sft_rasp_alpha0p5_20 的 checkpoint

---
