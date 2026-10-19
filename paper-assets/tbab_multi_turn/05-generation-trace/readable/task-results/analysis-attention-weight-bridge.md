# analysis attention weight bridge

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention-weight-bridge_20260518T192950_result.json`
- **Structured JSON:** [`dca2ee0179e13e740ae3.json`](../../sessions/dc/dca2ee0179e13e740ae3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have the complete results. Here's the analysis:

## 结果总结

### Bridge tokens 被 attend 了（机制确实 engage）

**VERDICT: Peak attention ratio = 4.65x expected (STRONG)**

#### 1. Content → Bridge 注意力

| 层级 | 行为 |
|------|------|
| **L0-L1** | bridge 获得 **2.5-5.6x 预期**的注意力。L1 H24（最高 12.7% attention fraction，vs 1.16% baseline）是最强 bridge-attending head |
| **L2-L30** | bridge 获得 **0.06-0.34x 预期**的注意力，被**主动抑制** |
| **L31** | bridge 回升到 0.31-0.80x，但仍低于 chance |

#### 2. Bridge → Content 注意力（信息聚合）

Bridge tokens **强烈 attend to 前序内容**：所有层 >97% 的注意力流向前序 content tokens（L31 略低，~80-90%）。这说明 bridge tokens 确实在聚合上文信息。

#### 3. Notable Bridge-Attending Heads

集中在 L0/L1：H8, H9, H24, H29, H5, H28, H11, H1。这些 head 给 bridge tokens 的注意力达到 **5-19x expected**。

### 诊断结论

Bridge tokens 机制 **已经 engage**，但存在以下问题：

1. **注意力集中在最浅层（L0-L1）**：只有最底层 attend to bridge，中间层和深层主动忽略。这意味着 bridge 信息没有被深层利用来改善生成质量。
2. **Bridge 确实聚合了上文信息**（bridge→content >97%），但 **content 在深层不读取 bridge**（L2-L30 仅 0.06-0.34x）。
3. C4 低于 C1 baseline 的原因：bridge tokens 作为额外的序列元素**分散了浅层的注意力预算**，但没有在深层提供有用信号来补偿这种开销。

**方向判断**：机制 engage 了但方向有问题。Bridge tokens 成了「只写不读」的 dead memory：它们从上文收集信息（bridge→content 强），但后续 content 在做实际语言建模的深层却不读取它们。

---
