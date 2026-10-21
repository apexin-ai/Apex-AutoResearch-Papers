# infra download progress check

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_progress_check_20260520T101302_result.json`
- **Structured JSON:** [`2a1ac86e0241ac297899.json`](../../sessions/2a/2a1ac86e0241ac297899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. Qwen3-8B — 下载中
- **进程**: PID 12091 存活，已运行 **13m47s**
- **已下载**: **2.2 GB**（config/tokenizer 等元数据文件已完成，safetensors 权重文件尚未落盘——正在下载到临时文件中）
- **预估总大小**: ~16 GB（8B bf16，4 个 shard）
- **进度**: ~14%，预计还需 ~1.5 小时

### 2. Qwen3-32B — 下载中
- **进程**: PID 12163 存活，已运行 **13m47s**
- **已下载**: **4.7 GB**（config 等元数据已完成，safetensors 尚未落盘）
- **预估总大小**: ~64 GB（32B bf16）
- **进度**: ~7%，预计还需数小时

### 3. vLLM — 安装中
- **进程**: PID 9275 存活，已运行 **39m06s**（pip install 通过清华源）
- vLLM 尚未可用（仍在编译/安装依赖）

### 4. 磁盘
- `/root/autodl-tmp/`: 250G 总量，已用 8.5G，剩余 **242G** — 空间充足

### 结论
三个任务均在正常运行中，无异常。**8B 尚未就绪**，safetensors 权重文件还在下载。建议 ~30 分钟后再查一次进度。

---
