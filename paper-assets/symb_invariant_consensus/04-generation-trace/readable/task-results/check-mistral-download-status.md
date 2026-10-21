# check mistral download status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mistral-download-status_20260517T010339_result.json`
- **Structured JSON:** [`c499460bc757c2fa8f58.json`](../../sessions/c4/c499460bc757c2fa8f58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**下载状态: 完成（有冗余文件）**

模型文件列表：

| 文件 | 大小 |
|------|------|
| model-00001-of-00003.safetensors | 4.95 GB |
| model-00002-of-00003.safetensors | 5.00 GB |
| model-00003-of-00003.safetensors | 4.55 GB |
| consolidated.safetensors | 14.50 GB |
| config.json, tokenizer.model 等 | 正常 |

**3 个 shard 合计 ~14.5 GB，完整。** 另外还有一个 `consolidated.safetensors`（14.5 GB），是合并后的单文件版本，两者都可用。

下载日志显示最后一次操作因 `httpx.ConnectTimeout` (SSL handshake timeout) 失败，但这应该是之前某次重试的残留错误，模型文件本身已完整下载。

无 `.incomplete` 或 `.tmp` 文件，无缺损迹象。模型可直接使用。

---
