# diagnose grpo cka only seed123

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_cka_only_seed123_20260519T151959_result.json`
- **Structured JSON:** [`8694ff936a95f9062f28.json`](../../sessions/86/8694ff936a95f9062f28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**grpo_cka_only_20_seed123：训练成功完成**

| 指标 | 值 |
|------|-----|
| 训练步数 | 100/100 |
| train_loss | 0.1361 (聚合), 0.0505 (末步) |
| 最终 reward | 0.2975 (std: 0.41) |
| 训练耗时 | ~11h 38m |
| WandB | `j8kn0sqd` |
| Checkpoint | 完整 (model.safetensors 12.3GB + config + tokenizer) |

**GPU 状态**：
- cuda:0: 95% 利用率（有任务在跑）
- cuda:1: 空闲，0 MiB 占用，可用于下一任务

**Registry 已更新**：status=DONE, conclusion=success, metrics 已写入。

**下一步**：需要在 seed 123 checkpoint 上跑 GSM8K eval，与 seed 42 的 64.37% 对比。cuda:1 当前空闲可用。

---
