# diag sft standard westd completion and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft-standard-westd-completion-and-eval_20260515T173550_result.json`
- **Structured JSON:** [`382a5c79dd4d3a984001.json`](../../sessions/38/382a5c79dd4d3a984001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**SFT Standard 20% retrain — 成功**

| 指标 | 值 |
|------|-----|
| final_loss | 0.6403 |
| avg_train_loss | 0.7577 |
| mean_token_accuracy | 0.8258 |
| train_runtime | 1679s (~28 min) |
| epochs / steps | 2 / 1870 |
| 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd/` (12GB) |

与 westb 上的 RASP SFT 对比：loss 0.64 vs 0.66，token_acc 0.83 vs 0.83，基本一致，符合预期。

**cuda:1 状态**: 空闲（0MiB / 0% 利用率）。cuda:0 同样空闲。两张 RTX PRO 6000 均可用于 N=100 eval。

**已完成**: registry 已更新为 success + metrics，cron 已删除。

---
