# code download mistral 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download-mistral-25068_20260518T102231_result.json`
- **Structured JSON:** [`45dce6143940e2bd5d03.json`](../../sessions/45/45dce6143940e2bd5d03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

**Mistral-7B-Instruct-v0.3**
- 状态：后台下载中 (PID: 18676)
- 下载方式：HF mirror (`hf download`，`HF_HUB_DISABLE_XET=1`)
- 速度：~3.5 MB/s
- 当前 I/O：rchar 336M，稳步增长
- 预计完成：~60 分钟

**Qwen2.5-14B-Instruct** (关键路径)
- 状态：后台下载中 (PID: 16416，modelscope)
- 进度：17GB / ~28GB（7/8 safetensor 分片在 `._____temp/`）
- 预估还剩 ~11GB

另外发现 **LLaMA-3.1-8B-Instruct** (PID 17783) 也在通过 modelscope 下载中。

三个模型同时后台下载。Mistral 预计 ~1 小时完成。

---
