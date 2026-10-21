# infra extract bce30 westd34887 only

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_extract_bce30_westd34887_only_20260517T224241_result.json`
- **Structured JSON:** [`41531dd01d9d8ac01d94.json`](../../sessions/41/41531dd01d9d8ac01d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。Cron 不存在（可能已被清理）。

## 结果汇总：`qwen14b_bce30_s42_eval`

| Metric | Value |
|--------|-------|
| wikitext2_ppl | **8.7634** |
| arc_challenge_acc_norm | **0.5759** |
| winogrande_acc | **0.7261** |
| mmlu_acc | **0.7167** |
| gsm8k_exact_match | **0.5307** |

配置：Qwen2.5-14B, BCE predictor, 30% sparsity (global_topk allocation), seed=42。总运行时间约 5.9 小时（21080s）。

PPL eval 还显示：dense baseline PPL = 5.18，predictor hard mask PPL = 5.57，TEAL sparse PPL = 8.76。

---
