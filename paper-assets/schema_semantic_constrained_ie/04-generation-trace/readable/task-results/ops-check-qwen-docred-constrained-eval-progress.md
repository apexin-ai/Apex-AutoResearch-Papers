# ops check qwen docred constrained eval progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_qwen_docred_constrained_eval_progress_20260516T021047_result.json`
- **Structured JSON:** [`c5ccd9e8f4778e756f9e.json`](../../sessions/c5/c5ccd9e8f4778e756f9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## w5_qwen_docred_lora_constrained_eval 进度

| 指标 | 状态 |
|------|------|
| 完成进度 | **48 / 998** samples (4.8%) |
| GPU 进程 (321568) | **ALIVE**, 运行 16m16s, RSS 1.9GB |
| Wrapper 进程 (321563) | **ALIVE**, 运行 16m17s |
| GPU 0 | 86% 利用率, 16825 / 97887 MiB |
| GPU 1 | 83% 利用率, 17265 / 97887 MiB |

**速度**: ~3 samples/min (~20s/sample)，比预估的 14s 略慢。

**预估剩余时间**: 950 samples / 3 per min ≈ **5.3 小时**（约 10:30 UTC 完成）。

注意：日志显示 `Device: cuda:0`（非 cuda:1），进程运行时间仅 16 分钟——看起来是近期才启动的，并非 02:00 UTC 提交的那次。

---
