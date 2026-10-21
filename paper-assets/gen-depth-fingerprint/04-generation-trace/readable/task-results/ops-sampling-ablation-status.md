# ops sampling ablation status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sampling-ablation-status_20260515T202451_result.json`
- **Structured JSON:** [`0740b2d1dbb868bf0eea.json`](../../sessions/07/0740b2d1dbb868bf0eea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：SUCCESS — 全部完成

### 1. 进程退出状态
- PID 222783 (cuda:3, low + default): **已退出**
- PID 226113 (cuda:2, high_t10_p095): **已退出**

### 2. 日志最后内容 (high_temp_cuda2.log)
```
high_t10_p095: 100%|██████████| 996/996 [3:33:48<00:00, 12.88s/it]
  [high_t10_p095] 4672 records in 12828.9s

Generation complete

PHASE 2: Feature Extraction (high_t10_p095 only)
  [high_t10_p095] Features exist: features_qwen3-1.7b-high-temp.csv (4702 rows)

=== HIGH-TEMP DONE ===
Features saved. Run evaluate phase separately after all configs finish.
```

### 3. 输出文件完整性

| Config | Features CSV | Rows | 时间 |
|--------|-------------|------|------|
| low_t05_p08 | `features_qwen3-1.7b-low-temp.csv` | 4810 | May 16 04:21 |
| default_t07_p09 | `features_qwen3-1.7b.csv` | 4617 | (已存在) |
| high_t10_p095 | `features_qwen3-1.7b-high-temp.csv` | 4702 | May 16 04:21 |

最终评估结果 `results/sampling_ablation.json` 生成于 May 16 04:22，包含所有 3 种 config 的 metrics。

### 4. 各 Config LOGO F1 结果

| Config | 3-class F1 | Binary F1 | Spearman(entropy_mean) |
|--------|-----------|-----------|----------------------|
| **low_t05_p08** | **0.785** | **0.797** | -0.694 |
| **default_t07_p09** | **0.788** | **0.799** | -0.602 |
| **high_t10_p095** | **0.726** | **0.733** | -0.002 |

**F1 range: 6.19 pp** (low→high)，`robust: false`。

关键发现：高温配置（t=1.0, p=0.95）使 depth signal 大幅退化——entropy 相关性从 -0.69 降到接近 0，F1 下降 ~6pp。低温和默认配置表现接近（差 <0.3pp）。qwen3-1.7b 在 high config 下 per-generator F1 暴跌至 0.418（因为它同时是生成器和评估目标，高温使自身 fingerprint 模糊化）。

---
