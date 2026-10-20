# ssh autodl status check 2h

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_status_check_2h_20260524T003359_result.json`
- **Structured JSON:** [`f891be90b53756849393.json`](../../sessions/f8/f891be90b53756849393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. API Judges (n17 run, /17982 total)

| Judge | 完成 | 进度 | 速率 | ETA | 500错误/100行 |
|-------|------|------|------|-----|---------------|
| claude-sonnet-4.6 | 849 | 4.7% | 0.2/s | ~19.5h | 17 |
| gemini-2.5-pro | 580 | 3.2% | 0.2/s | ~28.5h | 15 |
| deepseek-v4-pro | 491 | 2.7% | 0.1/s | ~33.5h | 8 |
| qwen3-235b | 583 | 3.2% | 0.2/s | ~28h | 11 |

4个进程全部存活。500 错误频率偏高（每100行日志 8-17 次），但都在 retry 处理。DeepSeek 最慢（0.1/s）。

### 2. LLaMA 下载：**未完成，已停滞**

6/9 safetensors 已下载（29GB），缺 shard 00002、00006、00009。无下载进程在运行，无 .incomplete/.tmp 文件。下载进程已死，需要重新启动下载。

**不部署 vLLM。**

### 3. rtx6000-4x：**断连**

连接被拒（port 23687），服务器可能已关机或端口已变更。

### 4. 磁盘

| 分区 | 使用 | 可用 | 使用率 |
|------|------|------|--------|
| /root/autodl-tmp | 164G | 87G | 66% |
| / (root) | 15G | 16G | 49% |

空间充足。

---

**需要决策：**
1. LLaMA 下载停滞 — 是否重新启动下载（补齐 3 个缺失 shard）？
2. rtx6000-4x 断连 — 是否需要去控制台检查？

---
