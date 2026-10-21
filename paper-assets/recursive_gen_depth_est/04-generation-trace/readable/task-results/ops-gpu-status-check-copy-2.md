# ops gpu status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260517T224924_result.json`
- **Structured JSON:** [`27b52934eb0881e232d3.json`](../../sessions/27/27b52934eb0881e232d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 状态

| GPU | 型号 | 利用率 | 显存占用 | 温度 |
|-----|------|--------|----------|------|
| cuda:0 | RTX PRO 6000 Black | **89%** | 32,385 / 97,887 MiB (33%) | 47°C |
| cuda:1 | RTX PRO 6000 Black | **0%** | 0 / 97,887 MiB | 29°C |

### 进程状态

| PID | 状态 | 说明 |
|-----|------|------|
| **806751** | **存活** ✓ | `python scripts/qwen25_14b_scale_validation.py`，运行 ~5.7h，占 cuda:0 32GB，CPU 105% |
| **813673** | **已死** ✗ | instruct 实验进程不存在 |
| **813535** | **已死** ✗ | instruct 实验进程不存在 |
| **695547** | **已死** ✗ | prompted_gen_gpt2xl_001 旧进程不存在 |

### 14B 模型下载

**未找到 Qwen2.5-14B 模型文件。** HF cache 中没有 `models--Qwen--Qwen2.5-14B` 目录。PID 806751 当前运行的是 `qwen25_14b_scale_validation.py`，可能模型以其他方式加载（已在 GPU 显存中），或缓存路径不同。

HF cache 中已有模型：Qwen3-8B, Qwen2.5-1.5B-Instruct, OLMo-1B, roberta-base, pythia-410m

### 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (overlay) | 30G | 11G | 20G | 35% |

### 总结

- PID 806751 正在正常运行 14B scale validation 实验，GPU 利用率 89%，状态健康
- 813673/813535/695547 三个进程均已结束
- 14B 模型不在标准 HF cache 路径，可能在 autodl-tmp 或通过自定义 cache_dir 加载（已在显存中使用）
- 磁盘充裕（65% 空闲）

---
