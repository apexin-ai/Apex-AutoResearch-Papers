# ssh llama download check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-download-check_20260515T081427_result.json`
- **Structured JSON:** [`1e148265edbf905ea38a.json`](../../sessions/1e/1e148265edbf905ea38a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

hf-mirror.com 下载正常运行，速度 ~16MB/s。

**汇报：**

| 项目 | 状态 |
|------|------|
| **下载状态** | 进行中（需重启后已恢复） |
| **已完成** | 12/15 分片 + tokenizer/config 等所有辅助文件 |
| **下载中** | model-00005, 00007, 00015（各 ~4.9GB） |
| **当前速度** | ~16MB/s（hf-mirror.com 国内镜像） |
| **预计完成** | ~15 分钟（每分片 ~5 分钟） |
| **模型路径** | `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/` |
| **当前大小** | 56GB（完成后约 70GB） |
| **磁盘空间** | 250GB 总量，65GB 可用，充足 |
| **PID** | 244218 |

**踩坑记录**：之前的下载因 `cas-bridge.xethub.hf.co`（xet 端点）在 AutoDL 代理下超时中断。直连 hf-mirror.com（不走代理，不走 xet）速度正常。

---
