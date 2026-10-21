# download qwen3 14b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_qwen3_14b_20260518T112127_result.json`
- **Structured JSON:** [`649a65101e4792510629.json`](../../sessions/64/649a65101e4792510629.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

11.8GB (42%)。18 分钟内下载了 11.8GB。稳定 ~11 MB/s。剩 ~16GB，约 25 分钟。

当前状态汇报：
- **进度**: 11.8GB / ~28GB (42%)，1/8 shards 完成
- **速度**: ~11 MB/s
- **PID**: 534739，运行中
- **预计完成**: ~20:05

下载在后台稳定进行。如果你需要我继续监控到完成请告诉我，否则可以稍后手动检查：
```bash
ssh rtx5090-4x 'ls -lh /root/autodl-tmp/models/Qwen/Qwen3-14B/*.safetensors | wc -l && du -sh /root/autodl-tmp/models/Qwen/Qwen3-14B/'
```
期望结果：8 个 safetensors 文件，总计约 28GB。

---
