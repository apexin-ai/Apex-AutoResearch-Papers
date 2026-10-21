# prep codellama 13b download

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_codellama-13b-download_20260516T074828_result.json`
- **Structured JSON:** [`e9fc888eea447c13ed32.json`](../../sessions/e9/e9fc888eea447c13ed32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态

**下载进度**: Shard 1 已下载 2.26 GB / ~8.7 GB，总模型 24.2 GB。速度 ~9 MB/s。

**预计完成时间**: 约 35-40 分钟后全部下载完成。

**已完成**:
- 7B 下载进程已终止 ✓
- 7B 残留文件已清理 ✓  
- 磁盘空间充足 (111 GB 可用) ✓
- 小文件(config/tokenizer)已下载 ✓
- 训练命令 artifact 已注册 ✓

**进行中**:
- PID 255083: `wget` 从 hf-mirror.com 下载 3 个 safetensors shards（无代理直连）

**待完成**:
- 验证下载完整性
- CPU dry-run（tokenizer + config 检查）

下载在稳定运行，需要等待。是否继续轮询直到完成，还是你想之后再来检查？

---
