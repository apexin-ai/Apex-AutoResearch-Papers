# ssh check eval status

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-status_20260512T195719_result.json`
- **Structured JSON:** [`b2a66210edda8f54b271.json`](../../sessions/b2/b2a66210edda8f54b271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 两个实验都在运行中

| 实验 | PID | 运行时间 | GPU | 显存 | GPU 利用率 |
|------|-----|---------|-----|------|-----------|
| **SFT eval** (`evaluate.py`) | 17840 | 4h55m | GPU 0 | 17,140 MiB / 97,887 MiB | 68% |
| **PostHoc NLI** (`rerank_nli.py`) | 17369 | 4h56m | GPU 1 | 17,140 MiB / 97,887 MiB | 72% |

### 结果文件
- `outputs/sft/eval_results.json` — **不存在**
- `outputs/posthoc_nli/eval_results.json` — **不存在**

### 进度分析

日志文件只有模型加载信息（4-5 行），无推理进度输出。原因：
1. Python stdout 重定向到文件时使用 block buffering，`print()` 输出积压在缓冲区未写入磁盘
2. 脚本每 50 个样本才打印一次进度

**推理参数**：Mistral-Small-3.1-24B 模型，985 个样本，逐条推理（无 batch），每条最多生成 2048 tokens（greedy）。

**时间估算**：24B 模型单 GPU greedy 生成约 30-50 tok/s，假设平均生成 500-1000 tokens/样本，每条约 15-30 秒。985 条总计约 4-8 小时。已跑约 5 小时，**可能接近完成或还需 1-3 小时**。`rerank_nli.py` 在生成后还需额外做 NLI 评分，会更慢。

### 无异常迹象
- 进程状态 `Rl`（运行中 + 多线程）
- GPU 利用率正常（68-72%）
- 无 error/traceback

---
