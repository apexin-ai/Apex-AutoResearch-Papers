# analysis plan013 results

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan013-results_20260514T022618_result.json`
- **Structured JSON:** [`c17d2a857a50b7168d14.json`](../../sessions/c1/c17d2a857a50b7168d14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan013_analysis.md` 并注册。核心发现：

**三方对比结果出乎意料：**

| | exec-only | random reward | convex STA |
|---|:---:|:---:|:---:|
| last100 PR | 0.865 | **0.966** | 0.773 |
| ISR/PR ratio | ~1.0 | 1.0 | 0.298 |

1. **Random reward (0.966) > exec-only (0.865) > STA (0.773)**。随机噪声替代 ISR 后，不仅没有损害，反而因正则化效应超越了 exec-only baseline。

2. **ISR 作为 reward component 是 harmful 的**——plan005 的 convex STA 表现最差。ISR 梯度方向与 exec 冲突。

3. **ISR 是 prove_rate 的自然副产物**（r=0.994，495/500 步完全一致），说明它有诊断价值但不应直接进 reward。

4. **Paper claim "ISR provides structural feedback that improves formalization" 需要重新表述**。建议方向：ISR 作为 diagnostic metric 有价值；ISR 直接进 convex reward 有害是重要 negative finding；random noise 的正则化效应值得进一步 ablation。

5. **Data integrity warning**: plan013 config 的 data_path 是 `proofwriter_fol_500.jsonl`，需确认与 plan001/plan005 一致性（约束 C001）。

---
