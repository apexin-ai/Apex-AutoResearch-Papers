# code 14b model download

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b_model_download_20260516T044926_result.json`
- **Structured JSON:** [`1a6d932cf28471d10b0a.json`](../../sessions/1a/1a6d932cf28471d10b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进程运行中。汇报结果：

---

## 状态汇报

| 项目 | 状态 |
|------|------|
| **模型下载** | 进行中（PID: 318170） |
| **下载路径** | `/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct/` |
| **当前速度** | ~1.3 MB/s（多文件并行下载中） |
| **预计时间** | 约 5-6 小时（28GB / 1.3MB/s） |
| **磁盘空间** | 167GB 可用，充足 |

### 显存评估

| GPU | 已用 | 总计 | 空闲 |
|-----|------|------|------|
| 0 | 73 GB | 98 GB | 25 GB |
| **1** | **16 GB** | **98 GB** | **82 GB** |
| 2 | 73 GB | 98 GB | 25 GB |
| 3 | 73 GB | 98 GB | 25 GB |

**14B bf16 单卡可行性：GPU 1 有 82GB 空闲，完全可以单卡加载 14B（~34-40GB 含 KV cache + 激活）。**

### 待完成
下载完成后需要创建符号链接：
```bash
ln -sf /root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct /root/autodl-tmp/pacs/checkpoints/Qwen2.5-14B-Instruct
```

下载速度偏慢，需要等待。可以稍后用 `tail -5 /tmp/download_14b.log` 和 `du -sh /root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct/` 轮询进度。

---
