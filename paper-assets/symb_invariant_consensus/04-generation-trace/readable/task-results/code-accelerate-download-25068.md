# code accelerate download 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_accelerate-download-25068_20260518T072309_result.json`
- **Structured JSON:** [`2c1ebed562ffcdc25f78.json`](../../sessions/2c/2c1ebed562ffcdc25f78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在跑。从 15:34 到 15:42（8分钟），下载了 ~3.6G（5.0G - 1.4G pre-existing），平均速度 ~7.5 MB/s。

## 产出

| 项目 | 值 |
|------|-----|
| **下载方式** | Python 16-worker 并行 + hf-mirror.com |
| **当前速度** | ~5-7 MB/s（机器外网出口硬限制） |
| **已下载** | 5.0 GB / ~140 GB |
| **预计完成时间** | ~5.5-6.5 小时（约 21:30-22:30 CST） |
| **PID** | 5399 |
| **日志** | `/tmp/download_qwen72b_v2.log` |

**监控命令：**
```bash
# 查进度
du -sh /root/autodl-tmp/models/Qwen2.5-72B-Instruct/
# 查日志（文件完成后会输出速度）
tail -20 /tmp/download_qwen72b_v2.log
# 查进程
ps aux | grep parallel_download
```

**说明：** 测试了 modelscope、hf_transfer、huggingface-cli (`hf`)、16-worker 并行四种方案。这台机器外网出口带宽上限约 5-7 MB/s，单连接仅 0.6-0.7 MB/s。16 并行连接是在该带宽约束下的最优方案，比原始单连接（3 MB/s）提升约 2x。

---
