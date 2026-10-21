# ssh check collapsed seed fsdp checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_collapsed_seed_fsdp_checkpoints_20260522T220352_result.json`
- **Structured JSON:** [`06e548fef205e67a171b.json`](../../sessions/06/06e548fef205e67a171b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确：

```
seed2048: FSDP checkpoint 不存在, 仅有空目录 seed2048_step5_ood_eval (0B), 含 optimizer: 否 ❌
seed42:   FSDP checkpoint 不存在, 仅有 HF 格式 qwen_exp029_seed42_step5_hf (3.8GB safetensors), 含 optimizer: 否 ❌
seed8:    FSDP checkpoint 不存在, 仅有 HF 格式 qwen_exp029_seed8_step5_hf (3.8GB safetensors) + 空目录 exp029_seed8_ood_precollapse (0B), 含 optimizer: 否 ❌
```

3 个 collapsed seeds 均无 FSDP 训练 checkpoint。整个服务器上唯一含 optimizer states 的 FSDP checkpoint 是 `exp029-seed100/global_step_5/`（21GB）。这 3 个 seed 无法 resume 训练，只能从头重跑或从 HF weights 初始化（但会丢失 optimizer states）。

---
