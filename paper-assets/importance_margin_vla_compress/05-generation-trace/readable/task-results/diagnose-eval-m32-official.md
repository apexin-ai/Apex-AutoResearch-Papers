# diagnose eval m32 official

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_m32_official_20260519T110855_result.json`
- **Structured JSON:** [`afc1e541fdfc5ed4839f.json`](../../sessions/af/afc1e541fdfc5ed4839f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：Smart Compress M=32 (official checkpoint) Overall SR = 53.4%**

对比：
| 实验 | SR |
|---|---|
| 官方 SmolVLA baseline | 59.2% |
| Smart Compress M=32 (official) | **53.4%** |
| Smart Compress M=32 (smolvla_base, seed42) | 61.6% |

Official checkpoint 训练的 M=32 压缩模型 SR=53.4%，低于 baseline 59.2%（降了 5.8pp），也低于 smolvla_base 版本的 61.6%。95% Wilson CI [49.0%, 57.7%] 上界仍低于 baseline。

最差 task: tomato sauce 28%，最好 task: butter 78%。

---
