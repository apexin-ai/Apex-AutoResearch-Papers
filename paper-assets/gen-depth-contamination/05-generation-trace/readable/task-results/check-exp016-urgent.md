# check exp016 urgent

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp016_urgent_20260516T044820_result.json`
- **Structured JSON:** [`3a3deb47014bdfbf3dba.json`](../../sessions/3a/3a3deb47014bdfbf3dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。以下是完整报告。

---

## exp-016 状态报告

### 1. 进程状态：已完成
- PID 3442 已退出，无 Python 进程在运行
- 4 卡 GPU 全部空闲（0MiB / 0%）— 符合预期，pipeline 已跑完
- 日志末尾：`Pipeline complete.`

### 2. 结果：K* = 2

| Pair | AUC (±std) | JSD |
|------|-----------|-----|
| 0v1 | **0.987** ± 0.0015 | 0.1637 |
| 1v2 | **0.6262** ± 0.0152 | 0.0108 |
| 2v3 | 0.5496 ± 0.0067 | 0.0053 |
| 3v4 | 0.5294 ± 0.0132 | 0.0039 |
| 4v5 | 0.5182 ± 0.0139 | 0.0035 |

Ordinal: MAE=1.169, Accuracy=37.2%

### 3. exp-016 (Base) vs exp-017 (Instruct) 对比

| Metric | exp-016 Base | exp-017 Instruct |
|--------|-------------|-----------------|
| **K\*** | **2** | **2** |
| 0v1 AUC | 0.987 | 0.9972 |
| 1v2 AUC | 0.6262 | 0.6114 |

**结论：K\*=2 在 base model 上完全复现，NOT an instruct-tuning artifact。** Base 的 0v1 略低（生成文本更接近 human），1v2 略高（depth 1→2 区分度稍强）。差异不影响 K\* 判定。

### 4. 数据完整性
- features.csv: 30001 行（header + 30000 = 6 depths × 5000 samples）✓
- results 目录: pairwise_auc.json, jsd.json, ordinal_results.json, feature_importance.json, summary.txt 全部存在 ✓

### 5. 模型下载进度
| 模型 | 大小 | 状态 |
|------|------|------|
| LLaMA-3.1-8B | 30GB | ✓ 完成 |
| Mistral-7B (mistralai/) | 4.3GB | ⚠️ 可能不完整（fp16 应~15GB） |
| Mistral-7B (AI-ModelScope/) | 4KB | ✗ 仅占位符 |

Mistral-7B 下载可能中断或只下载了部分文件，后续使用前需确认。

### 6. Registry
已更新：status=DONE, conclusion=success, metrics 已写入。

---
