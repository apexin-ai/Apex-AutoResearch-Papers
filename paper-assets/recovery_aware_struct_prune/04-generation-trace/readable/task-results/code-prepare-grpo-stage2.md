# code prepare grpo stage2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-grpo-stage2_20260515T000859_result.json`
- **Structured JSON:** [`cbccfd2a8e9a1a4af7ce.json`](../../sessions/cb/cbccfd2a8e9a1a4af7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_grpo_stage2.sh` 已创建，语法验证通过。

配置要点：
- RASP (GPU0) / Standard (GPU1) 并行训练，输入为 SFT warmup checkpoint
- `num_train_epochs=1`, `max_samples=2000`, `max_completion_length=4096`
- `save_steps=100`, `save_total_limit=3`, `reward_desert_patience=50`
- 输出到 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_{rasp,standard}_20_stage2/`
- 日志 tee 到 `logs/grpo_stage2_{rasp,standard}.log`
- wandb run_name: `grpo_stage2_rasp_20` / `grpo_stage2_standard_20`

SFT eval 通过后执行 `bash src/run_grpo_stage2.sh` 即可启动。

---
