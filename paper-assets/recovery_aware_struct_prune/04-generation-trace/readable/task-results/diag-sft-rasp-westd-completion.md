# diag sft rasp westd completion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft-rasp-westd-completion_20260515T173352_result.json`
- **Structured JSON:** [`ffe6c5e7902c003c83ce.json`](../../sessions/ff/ffe6c5e7902c003c83ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 项目 | 值 |
|------|-----|
| 状态 | 成功 |
| final loss | 0.658 |
| token accuracy | 0.8302 |
| 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd/model.safetensors` (12G) |
| 训练时长 | 28.4 min (1870 steps, 2 epochs) |

与 westb 结果基本一致（预期 loss ~0.6, accuracy ~0.84）。Registry 已更新，cron 已清除。

---
