# ops check mistral download

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_mistral_download_20260515T200357_result.json`
- **Structured JSON:** [`c7cfc5d90b2be773c666.json`](../../sessions/c7/c7cfc5d90b2be773c666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态：**失败**

**结果汇总：**

| 项目 | 状态 |
|------|------|
| 下载进度 | 1/15 文件 (7%)，日志停在此处 |
| 模型权重 | **0 个 .safetensors 完成**，3 个分片（model-00001~00003-of-00003.safetensors）全未完成 |
| 缓存碎片 | 4 个 `.incomplete` 文件共 ~3.4GB（1010M + 910M + 850M + 700M） |
| 元数据 | config.json / tokenizer 等已下载（3.2MB） |
| 目录总大小 | 4.1GB（全是缓存碎片，不可用） |
| 磁盘空间 | /root/autodl-tmp 剩余 221GB，空间充足 |

**失败原因：** 日志显示 `Warning: You are sending unauthenticated requests to the HF Hub`，未认证下载大文件大概率被限速或断连，进程中断后 nohup 日志也不存在，进程已死。

**需要重新下载。** 建议：
1. 清理 `.cache` 目录中的 `.incomplete` 碎片
2. 设置 `HF_TOKEN` 或改用 ModelScope（AutoDL 上 HF 下载极慢）
3. 重新用 nohup 启动下载

---
