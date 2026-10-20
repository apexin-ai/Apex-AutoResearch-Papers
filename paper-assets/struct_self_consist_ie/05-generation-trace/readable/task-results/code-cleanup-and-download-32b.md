# code cleanup and download 32b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cleanup_and_download_32b_20260519T063858_result.json`
- **Structured JSON:** [`2d2dcfd7d3fb80c22cf0.json`](../../sessions/2d/2d2dcfd7d3fb80c22cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载在继续（1.1G，有多个 .incomplete 文件在写入中）。32B 模型约 65GB，预计需要较长时间。

---

## 汇报

### 磁盘清理

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 203G | 142G |
| 可用 | 48G | 109G |
| 使用率 | 81% | 57% |

**释放空间：~61GB**（4 个 merged model 目录）

已删除：
- `qwen3-8b-scierc-3epoch-merged` (16G)
- `qwen3-8b-scierc-10epoch-merged` (16G)
- `llama3.1-8b-scierc-merged` (15G)
- `qwen3-8b-conll2003-merged` (16G)

LoRA adapter 全部保留。

### 模型下载

- **状态**：后台下载中（PID 764902/764903）
- **模型**：`Qwen/Qwen2.5-32B-Instruct`（~65GB）
- **下载路径**：`/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-32B-Instruct/`
- **镜像**：hf-mirror.com（huggingface.co 不可达）
- **进度**：已下载约 1.1GB，27 个文件中正在并行下载多个 shard
- **监控**：`tail -f /root/autodl-tmp/qwen25_download.log` 或 `du -sh /root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-32B-Instruct/`

### 训练环境

| 包 | 版本 |
|----|------|
| torch | 2.10.0+cu128 |
| transformers | 4.57.1 |
| peft | 0.17.1 |
| trl | 0.24.0 |
| accelerate | 1.11.0 |
| bitsandbytes | 0.49.2 |
| GPU | 4× RTX 5090 (31.4GB each, 共 125.6GB) |

环境版本均较新，可直接用于 QLoRA 训练 32B 模型。

---
