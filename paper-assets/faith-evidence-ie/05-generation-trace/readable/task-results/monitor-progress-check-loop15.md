# monitor progress check loop15

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_loop15_20260516T164332_result.json`
- **Structured JSON:** [`dc6d11b09a5fe6108314.json`](../../sessions/dc/dc6d11b09a5fe6108314.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | GPU | PID存活 | 进度 | 速率 | 预计完成 |
|------|-----|---------|------|------|----------|
| **plan_006_qwen3_1_7b_rsft_candidates** | cuda:0 (13.5/32.6 GB, 52%) | ✅ (2h52m) | 820/3027 (27.1%) | ~12.5s/doc | ~7.7h 后 (~08:00 UTC) |
| **plan_006_qwen3_8b_rsft_candidates** | cuda:3 (28.1/32.6 GB, 78%) | ✅ (2h53m) | 649/3027 (21.4%) | ~16s/doc | ~10.6h 后 (~11:00 UTC) |
| **plan_016_llama_rsft_candidates_r3** | cuda:2 (24.0/32.6 GB, 88%) | ✅ (53m) | 271/2963 (9.1%, 从idx=64恢复) | ~11.8s/doc | ~8.8h 后 (~09:10 UTC) |
| **plan_007_redocred_rsft_eval_r2** | cuda:1 (10.5/32.6 GB, 42%) | ✅ (16m) | 30/124 batches (24.2%) | ~32s/batch | ~50min 后 (~01:20 UTC) |

备注：
- 1.7B 和 8B 的 RSFT Monitor 报告 truncation_rate 14.8%/16.4%（超过 10% 阈值），建议后续考虑 max_new_tokens=3072
- Llama 刚恢复运行 53 分钟，速度正常
- Eval 预计很快完成（~50min）

---
