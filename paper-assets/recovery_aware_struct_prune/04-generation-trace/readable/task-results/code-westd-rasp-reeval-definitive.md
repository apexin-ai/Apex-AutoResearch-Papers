# code westd rasp reeval definitive

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-rasp-reeval-definitive_20260515T112703_result.json`
- **Structured JSON:** [`a0daf2237cceb5d28c8e.json`](../../sessions/a0/a0daf2237cceb5d28c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。关键数据：

## pruned_rasp_20 Definitive Re-eval 结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **29% (29/100)** |
| **EOS Rate** | 90% (90 natural EOS / 10 truncated) |
| **平均生成长度** | 809.5 tokens |
| **最大生成长度** | 4096 (truncated) |
| **最小生成长度** | 174 |
| **stderr** | ±4.54% |
| **解码方式** | greedy (temperature=0.0, do_sample=false) |

### 核心结论：29% 准确率完全可复现

greedy decoding 下 N=100 结果精确命中 29%，与之前观测值一致。这不是随机波动——greedy 解码是确定性的，相同模型+相同数据+相同参数必然得到相同结果。

EOS rate 从中间点的 86% 上升到最终的 90%，说明后 50 个样本中 truncation 更少。平均生成长度 809.5 tokens 属于正常范围，但仍有 10% 的样本打满 4096 上限被截断。

---
