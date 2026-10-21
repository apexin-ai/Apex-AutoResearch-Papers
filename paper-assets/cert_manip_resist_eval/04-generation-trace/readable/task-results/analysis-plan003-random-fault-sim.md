# analysis plan003 random fault sim

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan003-random-fault-sim_20260522T070023_result.json`
- **Structured JSON:** [`58594f8db400d4894747.json`](../../sessions/58/58594f8db400d4894747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果与预期假设不一致：

| 指标 | 结果 |
|------|------|
| Adaptive K_eff 显著负 | **1/12** (arc_challenge×sycophancy) |
| Random-fault K_eff 显著负 | **0/12** |

Random-fault 条件下 K_eff 在多数 condition 的 β 为正（而非预期的负），说明在这组 20 panels 中，K_eff 与 η_max 强共线——高 K_eff 的 panel 通常包含弱 judge（如 llama3.1-8b），即使控制了 η_max，第二/三弱 judge 的故障率仍推高了 majority-vote 失败率。

不过 random-fault 的 R² 普遍更高（0.55–0.95 vs adaptive 的 0.14–0.73），说明独立故障模型的可预测性远高于 adaptive 攻击。这本身就是一个有价值的发现：**adaptive 攻击引入了 K_eff/η_max 无法解释的方差**。

结果已写入 `/root/cert_manip_resist_eval/artifacts/results/results_plan003_random_fault.json`。

---
