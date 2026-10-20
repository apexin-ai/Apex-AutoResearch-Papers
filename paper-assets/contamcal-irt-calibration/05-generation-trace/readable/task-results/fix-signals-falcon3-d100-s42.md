# fix signals falcon3 d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_signals_falcon3_d100_s42_20260522T145922_result.json`
- **Structured JSON:** [`d5d561533ce002448be3.json`](../../sessions/d5/d5d561533ce002448be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中：

- PID 702456 活跃，GPU 0 占用 15594 MiB
- S4 selfcritique mmlu 已开始处理（14042 items，chunked mode），不再报 `token_type_ids` 错误
- `bitsandbytes` 的 `libnvJitLink.so.13` 是非致命警告，不影响运行

**总结**：
- 实际错误不是 faiss，而是 `s4_selfcritique.py` 中 Falcon3 不接受 tokenizer 返回的 `token_type_ids`
- 已修复：在两处 `inputs` 构建后 `pop("token_type_ids", None)`
- S1 (embedding) 和 S2 (minkpp) 已在 v1 成功完成（6个文件），v2 只跑 S4
- 实验 `signals_falcon3_d100_s42_v2` 已在 cqa1-21977 cuda:0 运行（PID 702456），预计 mmlu 14042 items 约 7.5h + arc/gsm8k 约 1.5h

---
