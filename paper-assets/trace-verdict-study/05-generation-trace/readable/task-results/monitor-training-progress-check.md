# monitor training progress check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_check_20260515T163421_result.json`
- **Structured JSON:** [`626b561c8f4ae512b342.json`](../../sessions/62/626b561c8f4ae512b342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 训练进度汇报

### 实验 1: exception_only_seed123 (GPU 1, pid 124207)
- **状态**: 训练中
- **进度**: step 178/444 (40%), epoch 2/3
- **速度**: ~10-20s/step（当前 ~10s/step）
- **预计完成**: ~60-80 min 后训练完成，之后自动跑 eval
- **GPU**: 89% util, 32648 MiB

### 实验 2: deepseek_full_trace_seed42 (GPU 0)
- **状态**: 已完成（exit code 0, 16:35 UTC）
- **⚠️ 异常**: eval 结果崩溃 — accuracy 28.5%，模型全部预测为 "fail"（pass recall=0, fail recall=1.0）。模型坍缩，需要排查。
- **无 predictions.jsonl**

### 额外发现: deepseek_no_trace_seed42 (GPU 0)
- **状态**: 已完成（exit code 0, 13:35 UTC）
- **Eval**: 73.4% accuracy, lift +1.8pp（基本等于 majority baseline 71.5%）
- **无 predictions.jsonl**

---

## GPU 状态
| GPU | Util | Memory | 状态 |
|-----|------|--------|------|
| 0 | **0%** | 49175/97887 MiB（残留缓存） | **空闲可用** |
| 1 | 89% | 32657/97887 MiB | exception_only 训练中 |

---

## Predictions 文件
| 实验 | predictions.jsonl |
|------|------------------|
| deepseek_vota | ❌ 不存在 |
| deepseek_no_trace | ❌ 不存在 |
| full_trace_label_only | ✅ 存在 (77KB, accuracy 86.2%) |

---

## 关键异常

1. **deepseek_full_trace eval 坍缩**: accuracy 28.5%，全预测 fail。可能原因：生成格式不匹配 eval 解析、DeepSeek 模型 chat template 问题、或训练崩溃。GPU 0 当前空闲，可以用来排查/重跑 eval。

2. **GPU 0 空闲**: deepseek_full_trace 和 deepseek_no_trace 均已完成，GPU 0 无活跃进程，可以立即用于下一步实验（如重跑 deepseek eval 生成 predictions.jsonl、或启动新训练）。

3. **缺失 predictions.jsonl**: deepseek_vota 和 deepseek_no_trace 需要用 v2 evaluate 脚本重新 eval 以生成 predictions.jsonl 供 paired bootstrap 使用。

---
