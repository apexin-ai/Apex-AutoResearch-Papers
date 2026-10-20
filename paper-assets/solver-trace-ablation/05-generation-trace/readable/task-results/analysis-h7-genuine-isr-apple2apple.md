# analysis h7 genuine isr apple2apple

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_h7-genuine-isr-apple2apple_20260514T153611_result.json`
- **Structured JSON:** [`589645b3ab659aa8b3cb.json`](../../sessions/58/589645b3ab659aa8b3cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已计算完成。

## 结果

| 条件 | Proved | H7 (n/%) | H1 (n/%) | Genuine (n/%) | Genuine ISR | Overall ISR |
|------|--------|----------|----------|---------------|-------------|-------------|
| **ISR β=0.1 s42** | 81 | 13/16.0% | 42/51.9% | 26/32.1% | **0.6014** | 0.4154 |
| **Random β=0.1 s42** | 79 | 0/0.0% | 58/73.4% | 21/26.6% | **0.2519** | 0.1314 |
| **Random β=0.1 s44** | 89 | 0/0.0% | 74/83.1% | 15/16.9% | **0.1992** | 0.0695 |

### 关键发现

1. **Random 无 H7**：random reward 训练的模型从不产生单 premise 直接复制 conclusion 的退化行为（H7=0%），而 ISR 训练有 16%。

2. **Random 的 H1 极高**：random s42 73.4%、s44 83.1% 的 proved 样本中 conclusion 出现在 premises 中（多 premise 场景）。这比 ISR 训练的 51.9% 更严重。

3. **Genuine ISR 大幅低于 ISR 训练**：
   - ISR 训练 Genuine ISR = **0.601**
   - Random s42 Genuine ISR = **0.252**（-58%）
   - Random s44 Genuine ISR = **0.199**（-67%）

4. **Genuine 样本数也更少**：random 训练的 Genuine 占比（26.6%/16.9%）低于 ISR 训练（32.1%），说明 random reward 不仅没学到推理，还更倾向于生产含 conclusion-in-premise 的 trivial proof。

5. **s44 的 Genuine 中有两个 ISR=1.0 的样本**（folio_556, folio_669），都只有 2 个 premise——这是少数随机命中的高质量证明，拉高了均值。去掉这两个后 Genuine ISR 降至约 0.069。

---
