# infra ssh check westd34887 urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_ssh_check_westd34887_urgent_20260517T215643_result.json`
- **Structured JSON:** [`35284887121d11cdbca6.json`](../../sessions/35/35284887121d11cdbca6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果:

**两个实验均正常运行，无错误。** 此前 cron 回调失效是误报。

| 实验 | 状态 | PPL | GSM8K 进度 | ETA |
|------|------|-----|-----------|-----|
| qwen14b_bce30_s42_eval | 运行中 | 8.7634 | 86% (1137/1319) | ~44min |
| bce_isocompute_v3_s123_eval | 运行中 | 28.0627 | 16% (209/1319) | ~21min |

两个 GPU 都在满负载工作。完整指标（ARC-c, WinoGrande, MMLU, GSM8K）要等 generate_until 跑完后才会写入 results.json。bce_isocompute_v3_s123 预计 ~06:18 UTC 完成，qwen14b 预计 ~06:41 UTC 完成。

---
