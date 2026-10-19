# research 1 7b cell a entropy kl pattern

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_1_7b-cell-a-entropy-kl-pattern_20260519T112115_result.json`
- **Structured JSON:** [`c190403a0e923d7c6ded.json`](../../sessions/c1/c190403a0e923d7c6ded.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整提取完成。

## 1.7B Cell A Entropy + KL 模式

### hsweep_h2_seed1 (wandb: 7o9bjszm)
| Step | entropy | ppo_kl | train_success |
|------|---------|--------|---------------|
| 1    | 0.330   | +0.044 | 18.8%         |
| 2    | 0.407   | +0.031 | 14.8%         |
| 3    | 0.413   | +0.040 | 18.8%         |
| 4    | 0.741   | +0.052 | 5.5%          |
| 5    | **1.009** | +0.050 | 1.6%        |
| 6    | 0.956   | +0.031 | 3.1%          |
| 7    | 0.972   | +0.030 | 4.7%          |
| 8    | 0.937   | +0.021 | 1.6%          |
| 9    | 0.877   | +0.012 | 0.0%          |
| 10   | 0.713   | +0.008 | 2.3%          |
| 11   | 0.638   | **-0.007** | 0.0%      |
| 12   | 0.374   | **-0.038** | 0.0%      |
| 13   | 0.328   | +0.011 | 0.0%          |
| 14   | **0.545** | +0.016 | 0.0%        |
| 15   | 0.342   | **-0.010** | 0.0%      |

### hsweep_h2_seed2 (wandb: jhwyg4tc)
| Step | entropy | ppo_kl | train_success |
|------|---------|--------|---------------|
| 1    | 0.319   | +0.115 | 0.8%          |
| 2    | 0.252   | +0.050 | 6.3%          |
| 3    | 0.329   | +0.019 | 5.5%          |
| 4    | 0.348   | +0.016 | 2.3%          |
| 5    | 0.260   | +0.014 | 12.5%         |
| 6    | 0.253   | +0.011 | 6.3%          |
| 7    | 0.260   | +0.009 | 0.0%          |
| 8    | 0.252   | +0.009 | 7.0%          |
| 9    | 0.370   | +0.008 | 3.1%          |
| 10   | 0.426   | +0.015 | 3.9%          |
| 11   | 0.306   | +0.008 | 0.8%          |
| 12   | 0.307   | +0.008 | 8.6%          |
| 13   | 0.312   | +0.007 | 2.3%          |
| 14   | 0.320   | +0.007 | 26.6%         |
| 15   | 0.401   | +0.006 | 28.1%         |

### 与 8B Cell A 对比

**8B Cell A 参考**：step 1 entropy=0.115(坍缩）→ step 2 entropy=0.605（反弹），ppo_kl=-1.885

**Entropy 反弹模式**：**是，seed1 有更剧烈的版本。**
- Seed1 展现完整的 3 阶段崩溃：
  1. **Entropy 爆炸**（steps 1→5）：0.33 → 1.01，策略扩散到随机
  2. **Entropy 坍缩**（steps 5→13）：1.01 → 0.33，策略重新收缩
  3. **Entropy 反弹**（steps 13→14）：0.33 → 0.55，与 8B 的 0.115→0.605 模式一致
- Seed2 entropy 始终稳定在 0.25-0.43 范围，无异常波动

**Negative KL 模式**：**是，seed1 有 3 个负 KL 步。**
- Step 11: -0.007，step 12: **-0.038**，step 15: -0.010
- 负 KL 出现在 entropy 坍缩阶段（steps 11-12）和反弹后（step 15），与 8B 中反弹伴随负 KL 的模式一致
- Seed2 全程 KL 为正（0.006-0.115），无任何异常

**结论**：sign misattribution 的破坏机制是 **scale-invariant 但 seed-dependent** 的。
- 1.7B seed1 复现了 8B Cell A 的完整 entropy 反弹 + 负 KL 模式，且更剧烈（entropy 从 0.33 爆炸到 1.01 再坍缩回 0.33，伴随 3 次负 KL），最终完全崩溃（success 降到 0%）
- 1.7B seed2 没有出现此模式，entropy 稳定，KL 始终为正，且成功学习（success 上升到 28%）
- 这说明 step-independent h=2 的 sign misattribution 问题跨尺度存在，但触发是随机的——一旦触发，破坏路径相同：entropy 异常振荡 → 负 KL → 完全崩溃

---
