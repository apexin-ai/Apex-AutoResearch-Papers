# analysis mvp tie rate

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-tie-rate_20260513T170519_result.json`
- **Structured JSON:** [`e8f9de64a402202823cc.json`](../../sessions/e8/e8f9de64a402202823cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常明确：

## 结论：CRITICAL — 1-step tie rate 98.2%

| Task | Tie Rate | Non-tie | Verdict |
|------|----------|---------|---------|
| boil | 93.8% | 6.2% | CRITICAL |
| melt | 98.5% | 1.5% | CRITICAL |
| change-the-state-of-matter-of | 98.5% | 1.5% | CRITICAL |
| chemistry-mix-paint-secondary-color | 99.7% | 0.3% | CRITICAL |
| grow-plant | 100.0% | 0.0% | CRITICAL |
| **Overall** | **98.2%** | **1.8%** | **CRITICAL** |

### 核心发现

1. **全局 non-tie rate 仅 1.8%** — 远低于 10% critical 阈值。1-step oracle labeling 下 router 基本无法学到 selective routing 信号。

2. **绝大多数 tie 是 both_delta=0**（2880/2894 tie 步都是两个 agent 的 score_delta 都为 0）。说明在绝大多数步骤中，无论选哪个 agent，环境分数都不变——这是稀疏奖励问题的直接体现。

3. **非 tie 步的 gap 几乎全是 catastrophic（|gap|>=100）**：出现差异时通常是一个 agent 触发了 -100 惩罚而另一个没有。这意味着差异信号虽然极其稀少，但幅度巨大。

4. **Phase 趋势**：后期步骤（21-30）tie rate 略低于前期，说明差异更可能在 episode 后半段出现。

### 直接含义

**N-step rollout labeling 是必须的**，不是可选的。1-step lookahead 在 >98% 的步骤上给出相同 label，router 训练集几乎没有正负样本区分。需要用多步累积 reward 差异来生成更有辨别力的 counterfactual labels。

---
