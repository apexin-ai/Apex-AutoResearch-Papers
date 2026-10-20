# ops check both running experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_both_running_experiments_20260520T220426_result.json`
- **Structured JSON:** [`ef90128bb3e4db0e6ed4.json`](../../sessions/ef/ef90128bb3e4db0e6ed4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

### 1. qwen15b_no_trace_seed456 (cuda:1)
- **PID 657684**: 运行中，已运行 9 分钟
- **训练进度**: step 286/444 (64%)，~1.8s/step
- **预计剩余**: ~5-8 分钟完成训练（含周期性 eval）
- **Checkpoint**: checkpoint-148 已保存
- **Eval 结果**: 尚未生成（训练完成后自动运行 evaluate.py）
- **异常**: 无

### 2. codellama13b_label_only_seed123_v2 (cuda:0)
- **PID 654451**: 运行中，已运行 45 分钟
- **训练进度**: step 95/444 (21%)，~27.5s/step
- **预计剩余**: ~2.7 小时
- **Checkpoint**: 尚未保存（首个 checkpoint 未触发）
- **Eval 结果**: 尚未生成
- **异常**: 无

### GPU 状态
| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| 0 (codellama13b) | 100% | 85.7/97.9 GB | 75°C |
| 1 (qwen15b) | 29% | 54.2/97.9 GB | 47°C |

GPU 1 利用率低是正常的——Qwen-1.5B 模型小，计算密度不高。两个实验均正常推进，qwen15b 即将完成训练并进入 eval 阶段。

---
