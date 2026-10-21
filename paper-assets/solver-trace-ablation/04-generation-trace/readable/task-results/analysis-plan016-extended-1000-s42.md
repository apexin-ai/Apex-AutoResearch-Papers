# analysis plan016 extended 1000 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan016-extended-1000-s42_20260514T080430_result.json`
- **Structured JSON:** [`a02b5151f923d5546287.json`](../../sessions/a0/a02b5151f923d5546287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结如下：

---

## plan016-extended-1000-s42 分析结果

### 训练完成情况
训练正常完成 1000/1000 步，耗时 2h26m，4 epochs。无 wandb。EXIT_CODE=0。

### 1000 步 vs 500 步 (plan001-s42) 对比

| 指标 | plan001-s42 (500步) | plan016 (1000步) | 变化 |
|---|---|---|---|
| eval PR | 93% | **96%** | +3pp ↑ |
| eval ISR mean | 0.123 | **0.003** | **-97.8%** ↓↓↓ |
| proved_only ISR | 0.132 | 0.003 | **-97.9%** ↓↓↓ |
| n_components | 6.58 | 18.55 | +182% ↑ |
| train entropy (末期) | — | 0.017 | 极低 |
| median ISR | — | 0.000 | 96/96 proved 样本中绝大部分 ISR=0 |

### Conclusion: **negative** (ISR 崩塌)

### 核心发现

1. **PR 是真实收敛**：500步的 93% 不是 lucky — 1000步进一步提升到 96%，证明 exec-only 确实能稳定学会证明。

2. **ISR 灾难性崩塌**：ISR 从 0.123 崩塌到 0.003（-97.8%）。96 个成功证明中，绝大多数 ISR=0（median=0），说明模型生成的形式化中每个 component 都被证明器使用，没有任何结构冗余。

3. **Entropy collapse**：训练末期 entropy 降到 0.017，模型变得极度确定性，mode-collapse 到生成最短可证明的形式化。

4. **对论文 narrative 的影响**：这是一个非常有力的 negative result —— 它直接证明了 exec-only reward 的根本缺陷：**PR 和 ISR 的 divergence 随训练时间加剧**。500 步时 ISR 尚有 0.123，1000 步时彻底归零。exec-only 训练越久，结构质量越差，即使 PR 继续提升。这强化了 STA/ISR 作为诊断工具的必要性——仅看 PR 无法发现这种退化。

---
