# ops disk cleanup and llama70b download

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_and_llama70b_download_20260523T090601_result.json`
- **Structured JSON:** [`34fea5e196641be38e27.json`](../../sessions/34/34fea5e196641be38e27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行，进程存活。速度约 1.4-2.5 MB/s，下载的是 `consolidated.*.pth` 文件（每个约 16.4GB）。按当前速度预估需要较长时间。

---

## 汇报

### 磁盘清理

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 321G | 182G |
| 可用 | 30G | **169G** |
| **释放** | — | **139G** |

已删除：LLM-Research（61G）、pip cache（7G）、Yi/01ai（17G）、InternLM（14G）、DeepSeek（13G）、OLMo/allenai（27G）。Qwen 缓存完整保留。

### Llama-3.1-70B-Instruct 下载

- **方式**：ModelScope（HF 无 token 且直连不通）
- **PID**：313198，正在运行
- **当前进度**：刚启动，正在下载 `consolidated.*.pth`（并行多文件），速度 ~1.4-2.5 MB/s
- **预估大小**：~140GB（多个 16.4GB 的 pth 文件）
- **预估时间**：当前速度下需要数小时

轮询命令（后续检查）：
```bash
tail -5 /tmp/llama70b_download.log
du -sh /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama*
df -h /root/autodl-tmp/
```

---
