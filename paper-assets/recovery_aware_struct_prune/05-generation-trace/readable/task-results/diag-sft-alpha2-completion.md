# diag sft alpha2 completion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft-alpha2-completion_20260515T153951_result.json`
- **Structured JSON:** [`48e477041ef8fe51623c.json`](../../sessions/48/48e477041ef8fe51623c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session，无需清除。

**结果：α=2.0 SFT 成功完成。**

| 指标 | 值 |
|------|-----|
| 总步数 | 1870/1870 (100%) |
| train_loss (avg) | 0.7424 |
| final loss | 0.6114 |
| token_accuracy | 0.8354 |
| 训练时间 | ~40min (2422s) |
| model.safetensors | 11.5GB |
| checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0/` |

Registry 已更新为 DONE/success，metrics 已记录。下一步需要对 α=2.0 post-SFT 做 GSM8K eval (N=100) 以完成 α ablation 对比。

---
