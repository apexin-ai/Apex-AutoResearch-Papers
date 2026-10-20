# ops diag llama sft cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diag_llama_sft_cuda4_20260516T131208_result.json`
- **Structured JSON:** [`f0a080284192ded28606.json`](../../sessions/f0/f0a080284192ded28606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清除或未创建），无需处理。

**结论：**

| 项目 | 状态 |
|------|------|
| 训练 | **成功** — epoch 1.0 完成，train_loss=1.517，runtime=8170s (~2h16m) |
| lora_alpha | **32** ✓（符合 C006） |
| Checkpoint | lora_adapter + merged model（2 shards，~6GB） |
| Registry | 已更新 conclusion=success |
| **cuda:4** | **0 MiB — 已释放，可分配新任务** |

---
