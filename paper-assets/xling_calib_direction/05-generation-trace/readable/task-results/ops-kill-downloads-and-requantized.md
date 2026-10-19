# ops kill downloads and requantized

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_downloads_and_requantized_20260520T211721_result.json`
- **Structured JSON:** [`a606e9d7ff8abe23e68f.json`](../../sessions/a6/a606e9d7ff8abe23e68f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已超过 15 分钟，下载仍在进行。以下是当前状态报告。

---

## 产出报告

### 1. 清理结果
- 进程 27403/27560/27565 已终止，所有下载进程已停止
- 已删除：Llama4Scout/, Qwen3-235B-A22B/, 相关缓存和日志
- 释放空间：根分区 29GB 可用，数据盘从 263GB → 当前 258GB（下载中占用）

### 2. 预量化模型选定

| 模型 | ID | 量化方式 | 大小 | 来源 |
|------|----|---------|------|------|
| Qwen3-235B-A22B | `Qwen/Qwen3-235B-A22B-GPTQ-Int4` | GPTQ-Int4 | ~125GB (32 shards × 3.73GB) | ModelScope 官方 |
| Llama 4 Scout | `RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16` | W4A16 | ~65GB (27 files) | HF mirror |
| **合计** | | | **~190GB** | < 258GB 可用 ✓ |

### 3. 下载状态（进行中）

| 模型 | PID | 已下载 | 速度 | 预估完成 |
|------|-----|--------|------|---------|
| Qwen3 GPTQ-Int4 | 28065 | 2.1GB / ~125GB | ~500KB/s/shard, 多分片并行 (~3-4MB/s 聚合) | ~8-10 小时 |
| Llama4 W4A16 | 28918 | 2.7GB / ~65GB | 进行中 | 待观察 |

### 4. 量化依赖安装结果

| 包 | 版本 | 状态 |
|----|------|------|
| bitsandbytes | 0.49.2 | ✓ |
| optimum | 2.1.0 | ✓ |
| gptqmodel | 7.0.0 | ✓（替代 auto-gptq） |
| auto-gptq | — | ✗ 编译失败（QiGen kernel 生成错误），已用 gptqmodel 替代 |

### 5. 注意事项
- Qwen3 GPTQ-Int4 模型卡建议用 **vLLM/SGLang** 推理（transformers 多 GPU GPTQ 有问题）
- Llama4 W4A16 使用 **compressed-tensors** 格式，也主要面向 vLLM
- 如需通过 transformers 访问 hidden states 做 probing，可能需要额外适配
- 下载速度较慢（ModelScope ~3-4MB/s），两个模型预计需要 **8-10 小时**完成

---
