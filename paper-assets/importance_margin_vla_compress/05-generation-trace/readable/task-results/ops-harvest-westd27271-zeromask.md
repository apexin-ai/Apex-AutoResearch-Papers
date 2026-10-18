# ops harvest westd27271 zeromask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_westd27271_zeromask_20260522T122853_result.json`
- **Structured JSON:** [`40f869ab244875e8de58.json`](../../sessions/40/40f869ab244875e8de58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已更新为 DONE (negative)。

## 结果摘要

| 实验 | 方法 | SR | 500 eps 中成功数 |
|------|------|----|-----------------|
| zeromask_random_k095 | 随机 5% token 置零（保持长度64） | **0.2%** (1/500) | 仅 task5 1次 |
| zeromask_l2norm_k095 | 最低L2 norm 5% token 置零 | **0.0%** (0/500) | 全灭 |

### 关键结论

**zero_mask 同样导致接近 0% SR，与 true_removal 结果一致。** 这排除了 "position shift" 假说——即使序列长度保持不变（64 tokens），仅将 5% 的 token 值置零就足以摧毁模型性能。

**含义：** SmolVLA 64-token 视觉表示中的信息是**不可丢弃的**，不是 position shift 问题，而是 token 信息本身的丢失造成 0% SR。每个 token 都承载了不可替代的信息。random zero_mask 的 0.2% 和 l2norm zero_mask 的 0% 都在统计噪声范围内（Wilson CI 包含 0），实际上等价于完全失败。

---
