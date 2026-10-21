# monitor westd grpo restart verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd_grpo_restart_verify_20260516T140753_result.json`
- **Structured JSON:** [`4a8f5a672064a93b0a15.json`](../../sessions/4a/4a8f5a672064a93b0a15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

✅ **4 个 GRPO 训练全部健康启动**

| 实验 | 进度 | 速度 | wandb run |
|------|------|------|-----------|
| grpo_rasp_qwen_math | 3/100 | ~27s/it | fijvduj2 |
| grpo_standard_qwen_math | 2/100 | ~27s/it | xof06efr |
| grpo_rasp_25_qwen_math | 3/100 | ~26s/it | bz6gmt0b |
| grpo_standard_25_qwen_math | 3/100 | ~26s/it | idwo5jp0 |

**磁盘状态**：
- 根分区：5.1G/30G (17%) — 正常
- 数据盘：268G/750G (36%) — 充裕

**wandb symlink 生效**：`/root/recovery_aware_struct_prune/wandb → /root/autodl-tmp/recovery_aware_struct_prune/wandb`，不再写根分区。

所有训练已过模型加载阶段，正在正常推进 step，无报错。

---
