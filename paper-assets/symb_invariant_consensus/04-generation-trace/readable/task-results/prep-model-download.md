# prep model download

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_model-download_20260516T061644_result.json`
- **Structured JSON:** [`e882c6036fa167489675.json`](../../sessions/e8/e882c6036fa167489675.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前下载状态汇总：

**两个下载都在后台正常运行：**

| 模型 | 来源 | 已下载 | 总大小 | 速度 | 预计剩余时间 |
|------|------|--------|--------|------|------------|
| Mistral-7B-Instruct-v0.3 | ModelScope (mistralai/) | ~400MB | ~14GB (3 shards) | ~3MB/s (3并行) | ~1.3 小时 |
| LLaMA-3.1-8B-Instruct | ModelScope (LLM-Research/) | ~3.6GB | ~15GB (4 shards) | ~1MB/s (2并行) | ~3 小时 |

**进程详情：**
- Mistral PID: 187141 — `snapshot_download('mistralai/Mistral-7B-Instruct-v0.3', ignore_file_pattern=['consolidated*', '*.pth'])`
- LLaMA PID: 186855 — `snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct', ignore_file_pattern=['original/*'])`
- 日志: `/tmp/dl_mistral.log`, `/tmp/dl_llama.log`
- 两个都不占 GPU，不影响 PID 181491 和 174291

**注意：**
- LLaMA 因 Meta license 限制无法从 HuggingFace 直接下载，已改用 ModelScope 镜像
- ModelScope 下载后文件存在 `&lt;cache_dir>/mistralai/Mistral-7B-Instruct-v0.3/` 和 `&lt;cache_dir>/LLM-Research/Meta-Llama-3___1-8B-Instruct/` 子目录中
- 下载完成后需要验证 tokenizer 是否正常加载

需要我继续轮询等待下载完成并验证吗？预计还需数小时。

---
