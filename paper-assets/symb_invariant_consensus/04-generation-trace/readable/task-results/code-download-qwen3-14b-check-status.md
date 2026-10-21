# code download qwen3 14b check status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download-qwen3-14b-check-status_20260518T124411_result.json`
- **Structured JSON:** [`c15978b52298631e38d9.json`](../../sessions/c1/c15978b52298631e38d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充足，汇总报告。

---

## 报告

### 1. exp-026 进度
- **PID 27245**: 运行中，正常
- **已完成**: 53/204 题（~26%）
- **速率**: ~40-45 秒/题
- **预计剩余**: ~105 分钟（约 1 小时 45 分钟）

### 2. 磁盘空间
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| /root (overlay) | 30G | 12G | 19G |
| /root/autodl-tmp | 250G | 144G | 107G |

### 3. 72B 下载状态
- **无活跃下载进程**（不是"还在下载"的状态）
- 已有 75G 文件（config.json + 28 个 safetensors），看起来是完整下载
- **未执行 kill/删除**，因为条件"还在下载"不成立

**需要确认：是否仍要删除已完成的 72B 模型（释放 75G）？**

### 4. Mistral 下载状态
- **已完成**（16G，config.json + 3 safetensors），无活跃下载进程
- 已保留

### 5. Qwen3-14B 下载
- **正确模型名**: `Qwen/Qwen3-14B`（Qwen3 系列不带 `-Instruct` 后缀，统一模型支持指令模式）
- **下载方式**: ModelScope（PID 29779），HF Mirror 已 kill（更慢）
- **当前速度**: ~2-2.5 MB/s/线程，8 个文件并行下载
- **模型总大小**: ~27.6G（7×3.69G + 1×1.78G safetensors）
- **预计完成**: ~1 小时
- **下载目录**: `/root/autodl-tmp/models/Qwen3-14B`

### 6. 额外发现
- **Llama-3.1-8B 下载**（PID 17783）仍在运行（已跑 2.5 小时），正在与 Qwen3 抢带宽。Llama 目录已 24G 但只有 1 个 safetensors 文件——可能在重下或卡住。是否 kill 以加速 Qwen3 下载？

---
