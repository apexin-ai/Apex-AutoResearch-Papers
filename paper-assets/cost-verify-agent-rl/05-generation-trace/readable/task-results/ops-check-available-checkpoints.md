# ops check available checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-available-checkpoints_20260514T125635_result.json`
- **Structured JSON:** [`406dcbdce186744e2a79.json`](../../sessions/40/406dcbdce186744e2a79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 扫描结果

**所有 GRPO checkpoint 已被清理。** `global_step_*` 目录在整个 `/root/autodl-tmp/` 下均不存在。

### 可用 checkpoint

| 路径 | 类型 | 大小 | 完整性 |
|------|------|------|--------|
| `/root/autodl-tmp/checkpoints/exp008_sft/final/` | SFT final | 3.3GB | **完整** — `model.safetensors` (3.2GB) + `config.json` + tokenizer 全套 |
| `qwen3_sft_final` → 上述路径的 symlink | — | — | — |

### 不可用

| 目标 | 状态 |
|------|------|
| exp008_grpo/global_step_5 | **已清理，不存在** |
| exp013f 任何 checkpoint | **已清理，不存在** |

### 结论

exp015 唯一可用的起点是 **exp008_sft/final**（纯 SFT 模型，优先级 3）。GRPO checkpoint 全部丢失，需从 SFT 重新开始 GRPO 训练。

---
