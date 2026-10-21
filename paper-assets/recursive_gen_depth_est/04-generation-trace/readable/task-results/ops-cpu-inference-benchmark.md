# ops cpu inference benchmark

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cpu_inference_benchmark_20260519T032144_result.json`
- **Structured JSON:** [`45a2f36afe64419cb579.json`](../../sessions/45/45a2f36afe64419cb579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收齐。汇总如下：

---

## CPU Inference Benchmark 结果

### 1. 硬件

| 项目 | 值 |
|---|---|
| CPU | Intel Xeon Platinum 8470Q × 2 |
| 物理核心 | 104 (52/socket) |
| 逻辑线程 | 208 |
| GPU 状态 | cuda:0 被 14B 训练占满 (64.6GB), cuda:1 空闲 |

### 2. Benchmark 结果（Pythia-1.4B, float32, CPU only, seq_len=512）

| Threads | Batch Size | Per-sample (s) | 5000 samples 外推 |
|---------|-----------|---------------|-------------------|
| 16 | 1 | 0.981 | **81.8 min** |
| 16 | 8 | 1.213 | 101.1 min |
| **32** | **8** | **0.563** | **46.9 min** |
| 64 | 8 | 1.327 | 110.6 min |
| 104 | 8 | 1.251 | 104.2 min |
| 64 | 16 | 0.957 | 79.7 min |
| 104 | 16 | 0.735 | 61.2 min |

### 3. 关键发现

- **最优配置**：32 threads, bs=8 → 每样本 0.563s → 5000 samples ≈ **47 分钟**
- 超过 32 线程后因 NUMA 跨 socket 竞争反而变慢（64/104 线程 bs=8 比 32 线程慢 2x+）
- 大 batch (16) 在高线程数下可以部分补偿，但仍然 >60 min

### 4. 论文 "2 分钟" 声明评估

**严重不准确。** 即使在 104 核 Xeon 服务器上最优配置，5000×512 的 CPU 推理需要 **~47 分钟**，是声称值的 ~25 倍。

"2 分钟"很可能是 GPU 上的实际时间（`extract_features.py` 默认用 `cuda:1` + float16 + bs=16）。

### 5. 建议修正

论文中应改为以下之一：
- **方案 A**（推荐）：删除 "requires no GPU" 的表述，改为 "Feature extraction takes ~2 minutes on a single GPU (Pythia-1.4B forward pass)" — 诚实反映实际使用场景
- **方案 B**：如果坚持宣传 CPU 可用性，改为 "Feature extraction can run on CPU without GPU, taking approximately 45-80 minutes on a server-grade CPU (Intel Xeon, 32 threads) for 5,000 passages"
- **方案 C**：同时给出两个数字 "~2 min on GPU / ~50 min on CPU"

---
