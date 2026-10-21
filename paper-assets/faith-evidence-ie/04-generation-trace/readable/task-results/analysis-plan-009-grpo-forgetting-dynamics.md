# analysis plan 009 grpo forgetting dynamics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_grpo_forgetting_dynamics_20260515T143751_result.json`
- **Structured JSON:** [`228c25788a71815952a0.json`](../../sessions/22/228c25788a71815952a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已就绪。

---

## 汇总表

| Run | Best rel_F1 | Final rel_F1 | Best Reward | Final Reward | Steps |
|-----|------------|-------------|------------|-------------|-------|
| CED, lr=5e-5, kl=0.01 | **0.2167** (step 100) | 0.2167 | 1.370 | 1.195 | 100 |
| CED, lr=5e-6, kl=0.01 | 0.0138 (step 100) | 0.0138 | 0.461 | 0.380 | 180 |
| CED, G=8, bf16 | N/A (无 eval) | N/A | 2.858 | 1.795 | 100 |
| **SFT baseline** | **0.4057** | — | — | — | — |

## Forgetting Dynamics 关键观察

1. **Reward-performance decoupling**: 所有 GRPO 配置的 reward 持续上升（lr=5e-5 达 1.37, G=8 达 2.86），但 rel_F1 最高仅恢复到 SFT baseline 的 53%（0.217 vs 0.406），lr=5e-6 更是全程 <0.014。

2. **Evidence-extraction decoupling**: lr=5e-6 的 evi_F1 从 0.628 稳步升至 0.850（超过 SFT 的 0.798），但 rel_F1 始终近零——模型学会了引用证据句但完全丧失了关系抽取能力，reward hacking 的典型表现。

3. **U 型恢复不足**: lr=5e-5 的 rel_F1 呈 U 型（step-10: 0.003 → step-100: 0.217），有缓慢恢复趋势但远不够，且 evi_F1 反而从 0.72 降至 0.57——关系恢复以证据质量为代价。

## 产出文件
- `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics.pdf`
- `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics.png`
- `artifacts/plan_009_grpo_forgetting/summary.json`
- 服务器端绘图脚本: `/root/autodl-tmp/artifacts/plan_009_grpo_forgetting/plot_forgetting_v2.py`

---
