# ops download qwen3 8b

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-qwen3-8b_20260513T090740_result.json`
- **Structured JSON:** [`dc674213b98cd71420d3.json`](../../sessions/dc/dc674213b98cd71420d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正常进行中。

- **PID**: 690535
- **状态**: 正在并行下载 5 个 safetensors 分片
- **当前速度**: ~15 MB/s（model-00005）、~3 MB/s（model-00001），多文件并行
- **总大小**: ~16GB（5 个分片）
- **预估时间**: 按当前速度约 15-20 分钟完成
- **日志**: `/tmp/download_qwen3_8b.log`
- **模型路径**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`

下载完成后日志末尾会输出 `DOWNLOAD COMPLETE`。可用以下命令检查进度：
```bash
tail -5 /tmp/download_qwen3_8b.log
```

---
