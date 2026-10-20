# analysis signals v7 done

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_signals_v7_done_20260516T021442_result.json`
- **Structured JSON:** [`96505c6fc6aa33e913af.json`](../../sessions/96/96505c6fc6aa33e913af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 产出清单

`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/`

| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| s1_embedding | 7.5 MB | 717 KB | 649 KB |
| s2_minkpp | 2.7 MB | 266 KB | 244 KB |
| s4_selfcritique | 3.2 MB | 309 KB | 283 KB |
| **merged** | 2.4 MB | 238 KB | 229 KB |

共 12 个文件（9 signal + 3 merged），全部非零，日志无报错。

**注意：缺少 s3 signal。** `--signal all` 只产出了 s1/s2/s4 三种，s3 未生成。如果 s3 是必需的，需要排查 `compute_signals.py` 中 `all` 的定义是否包含 s3。

---
