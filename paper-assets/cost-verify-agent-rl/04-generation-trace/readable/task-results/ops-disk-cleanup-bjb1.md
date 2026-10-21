# ops disk cleanup bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-bjb1_20260514T124603_result.json`
- **Structured JSON:** [`a8e6bd8d4a89f40231a3.json`](../../sessions/a8/a8e6bd8d4a89f40231a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| | 使用量 | 使用率 |
|---|---|---|
| **清理前** | 113G | 45% |
| **清理后** | 32G | 13% |
| **释放** | **81G** | |

### 已删除
- `/root/autodl-tmp/checkpoints/exp013f/` — 62G（global_step_10/15/20/25/30）
- `/root/autodl-tmp/checkpoints/exp008_sft/checkpoint-225/` — 9.7G
- `/root/autodl-tmp/checkpoints/exp008_sft/checkpoint-75/` — 9.7G
- `/root/autodl-tmp/ray_tmp/*` — 42M
- `/root/autodl-tmp/tmp/*` — 53M

### 已保留
- `exp008_sft/final/` — 3.3G，完整（model.safetensors 3.4GB + tokenizer + config）
- `qwen3_sft_final` symlink → exp008_sft/final ✓
- `alfworld/` — 2.2G
- `sft_data/` — 4.3M

### 备注
- `exp008_grpo` 不存在于服务器上（已被之前清理或从未保存到此路径）
- 无 wandb 目录、无 /tmp/ray/、无 `__pycache__` 需要清理
- 当前可用空间 219G，充足。

---
