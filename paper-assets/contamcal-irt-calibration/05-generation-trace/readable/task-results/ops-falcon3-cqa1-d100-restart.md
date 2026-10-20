# ops falcon3 cqa1 d100 restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-cqa1-d100-restart_20260522T045707_result.json`
- **Structured JSON:** [`f7e8a8f8c117bd8ca92f.json`](../../sessions/f7/f7e8a8f8c117bd8ca92f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。step 4/4159，~5s/step，预计 ~5.8 小时完成。

**总结**:
- **崩溃原因**: OOM — Falcon3-7B (bf16 ~14GB) 在 batch-size 4 和 batch-size 2 下都超出 24GB 4090D 的显存
- **修复**: batch-size 1 + grad-accum 16 + `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`，保持有效 batch size = 16 不变
- **当前状态**: PID 652456 正在训练，GPU 占用 19.5GB/24.5GB，~5s/step，ETA ~5.8h
- bitsandbytes 的 `libnvJitLink.so.13` 警告是非致命的，不影响当前训练

---
