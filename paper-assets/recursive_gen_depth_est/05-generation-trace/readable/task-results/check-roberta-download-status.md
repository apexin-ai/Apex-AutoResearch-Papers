# check roberta download status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_roberta_download_status_20260515T121100_result.json`
- **Structured JSON:** [`9722cf67a7c27ce2c41a.json`](../../sessions/97/9722cf67a7c27ce2c41a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**roberta-base 下载未完成，疑似卡住。**

| 项目 | 状态 |
|------|------|
| 下载进程 PID 124867 | 仍在运行 |
| Tokenizer + Config | ✅ 已下载到 `/root/autodl-tmp/models/roberta-base/` |
| 模型权重 (safetensors) | ❌ 下载中断/卡住 |

详细情况：
- HF cache 中权重文件 `.incomplete`，大小 230MB，最后修改时间 20:11，多次检查文件大小未增长
- roberta-base 完整权重约 499MB，当前仅下载了约 46%
- 日志停在 `"Downloading model..."` 无后续输出
- 可能原因：AutoDL 代理下载 HuggingFace 大文件速度极慢或连接超时

**需要 kill 当前进程并改用 ModelScope 重新下载。** 是否继续？

---
