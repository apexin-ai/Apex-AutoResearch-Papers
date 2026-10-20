# check w6 mistral progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_w6_mistral_progress_20260516T051855_result.json`
- **Structured JSON:** [`1b3f73c930518485d8f8.json`](../../sessions/1b/1b3f73c930518485d8f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## w6_mistral_scierc_unconstrained
- 进程状态: **alive** (pid=332156, 运行 25m17s, CPU 100%)
- 已完成: **428/551** samples (77.7%)
- 速度: ~16.9 samples/min (~3.5s/sample)
- ETA: **~7 分钟后完成**
- GPU 0: 14703/97887 MiB, 89% util
- 异常: 无（日志仅有 pad_token_id 警告，正常）

## w5_qwen_docred_lora_constrained_eval
- 进程状态: **alive** (pid=321568, 运行 3h24m, CPU 100%)
- 已完成: 日志进度 **486/998**，输出文件 550 行（日志可能有缓冲延迟）
- 速度: ~3.0 samples/min (~18s/sample，近 20 条平均)
- ETA: **~2.5 小时后完成**（按剩余 448-512 samples 估算）
- GPU 1: 17427/97887 MiB, 83% util
- 异常: sample 486 (Bill Warner) FAIL，E=0 R=0，耗时 76.1s（疑似生成超长/空输出）。其余正常。

---
