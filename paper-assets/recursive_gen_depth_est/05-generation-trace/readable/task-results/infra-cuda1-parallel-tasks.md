# infra cuda1 parallel tasks

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda1-parallel-tasks_20260514T125138_result.json`
- **Structured JSON:** [`06b7100ba007a7f7b57f.json`](../../sessions/06/06b7100ba007a7f7b57f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ModelScope 正在下载中（rust_model.ot 2%, tf_model.h5 4%，~600-900KB/s）。下载会在后台继续。

---

## 产出汇报

### 1. Pipeline 当前进度
- **Step 4: Generate depth-2** — depth-1 LoRA 训练已完成 (loss=1.389, 3 epochs)，正在生成 depth-2 数据
- 已生成文件:
  - `depth_0.jsonl` — 11MB (seed data)
  - `depth_1.jsonl` — 9.2MB (完成)
  - `depth_2.jsonl` — 1.9MB (生成中)

### 2. depth_0 特征提取结果
- **5000 行**，每行 **19 个特征**
- 特征包括: perplexity 统计量 (mean/var/skew/kurtosis/percentiles)、surprisal 统计量、词汇多样性指标 (TTR/hapax/n-gram entropy/repetition)
- 耗时: ~43 秒 (313 batches × batch_size=16, ~7.3 batch/s)
- 截断长度: 498 tokens (depth_0 median)
- 输出: `data/depth_0_features.jsonl`

### 3. DeBERTa 下载状态
- HF CLI 下载卡住 → 已切换 ModelScope
- ModelScope 正在下载中 (~600-900 KB/s)，预计 10-15 分钟完成
- 下载目标: `/root/autodl-tmp/models/deberta-v3-base-ms/`

### 4. GPU 利用率
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 61% | 13759 MiB (pipeline) |
| cuda:1 | 0% | 0 MiB (特征提取已完成) |

---
