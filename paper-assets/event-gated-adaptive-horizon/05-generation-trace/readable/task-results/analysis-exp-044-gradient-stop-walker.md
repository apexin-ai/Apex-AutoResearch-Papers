# analysis exp 044 gradient stop walker

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_044_gradient_stop_walker_20260522T160607_result.json`
- **Structured JSON:** [`ed818227c2f485a236e6.json`](../../sessions/ed/ed818227c2f485a236e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## exp_044_gradient_stop_walker 最终结果汇总

### 关键指标

| 指标 | 值 |
|------|-----|
| eval_final (215K) | **538.6** |
| eval_peak (185K) | **561.2** |
| eval_civo_trough (95K) | **44.3** |
| pre-CIVO peak (75K) | 545.6 |
| ve_ratio_peak (95K) | **4.4** |
| ve_ratio_final (215K) | **0.1** |
| total_steps | 224K |

### CIVO 时间线

- **Onset**: ~85K（ve_ratio 从 0.4 跳至 0.9）
- **Peak**: 95K（ve_ratio **4.4**，eval 从 545.6 崩至 **44.3**）
- **Declining**: 105K（ve_ratio 1.9，eval 87.8）
- **Resolved**: ~125K（ve_ratio 回落至 0.5）
- **Full recovery**: 175K-185K（eval 回到 508-561，ve_ratio 稳定 0.1）
- **CIVO 持续时间**: ~40K steps（85K→125K）

### 与中期数据对比

中期分析（D135）记录的 95K 时 ve_ratio=4.45、eval 44→105K 振荡回落 1.9，**完全吻合**。但中期未能观测到的关键发现：**CIVO 是 transient 的**，125K 后完全自愈，eval 最终超过 pre-CIVO 峰值。

### Conclusion: **success**（成功证伪 gradient stopping 的有效性）

Gradient stopping（detach dt_emb→reward_head）**无法阻止 CIVO onset**（peak ve_ratio 4.4 >> 1.5 阈值），直接支撑 Intervention Hierarchy：

| Intervention Level | Method | CIVO Prevented? | Peak NVE |
|---|---|---|---|
| **Gradient-level** (weakest) | detach (exp_044) | ❌ 发生但 transient | 4.4 |
| **Architecture-level** | frozen (exp_042) | ✅ | 0.19 |
| **Architecture-level** | removal (exp_043) | ✅ | <1.0 |

**Nuance**: detach 下 CIVO 是 transient（40K steps 后自愈），而非 permanent collapse。这说明 gradient stopping 虽不能阻止 CIVO 触发，但保留了系统自纠能力。论文中可以强调：gradient-level intervention 不足以 **prevent** CIVO，但可以 **limit its duration** — 这进一步细化了 Intervention Hierarchy 的层次结论。

---
