# analysis plan 030 rssm quality

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_030_rssm_quality_20260525T210913_result.json`
- **Structured JSON:** [`7794bd622b42bae36970.json`](../../sessions/77/7794bd622b42bae36970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan_030 完成。核心发现与初始假设**相反**：

**CIVO seed (exp_078) 的 RSSM 预测质量比 no-CIVO seed (exp_088) 更好**，所有指标均优：

| 指标 | exp_078 (CIVO) dt=2 | exp_088 (noCIVO) dt=2 | 差异 |
|------|---------------------|----------------------|------|
| velocity loss | 0.738 | 0.850 | −13% |
| reward loss | 0.299 | 0.616 | −51% |
| KL | 6.36 | 8.01 | −21% |
| position loss | 0.023 | 0.032 | −29% |

关键解读：
1. **CIVO 不是由 world model 质量差导致的** — 恰恰相反，CIVO seed 有更准确的模型
2. **更准确的 reward model 可能反而促进 CIVO**：reward head 预测过准，value function 容易 latch onto model 内部预测模式，形成自强化的过高估计
3. **no-CIVO seed 的更高 model error 起到了隐式正则化作用**，阻止 value function 过拟合

报告和数据已保存至 `artifacts/plan_030_rssm_quality/`。

---
