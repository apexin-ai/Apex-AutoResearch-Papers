# code action head v2 untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_head_v2_untrained_20260526T204306_result.json`
- **Structured JSON:** [`7ecd33adaef36e1ed9dc.json`](../../sessions/7e/7ecd33adaef36e1ed9dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，所有注册已更新。

## 结果摘要

**Untrained v2** (5000 samples, 249s, 20.1 samp/s):
- 所有 33 层 R² 均为负值，范围 **-5.61 ~ -3.55**
- Peak R² = **-3.55** at Layer 32 (exit)
- Exit MSE = **0.87**

**Sanity checks 全部通过：**
- No-double-norm 验证：exit layer logits match (diff=0.0625)，double-norm 差异大 (diff=11.19)
- Generate 输出 6 个 unique tokens
- Exit layer argmax 匹配 generate first token

**Trained vs Untrained v2 对比：**

| 指标 | Trained | Untrained |
|------|---------|-----------|
| Peak R² | -2.77 (L31) | -3.55 (L32) |
| Exit R² | -3.04 | -3.55 |
| R² 范围 | -7.08 ~ -2.77 | -5.61 ~ -3.55 |
| Peak MSE | 0.81 | 0.78 |

两组实验 R² 全部为负——action head 在任何层都无法解码有意义的动作。Untrained 稍差但差异不大，pattern 一致。

---
