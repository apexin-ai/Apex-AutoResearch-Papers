# analysis factorial wandb deep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_factorial_wandb_deep_20260518T020221_result.json`
- **Structured JSON:** [`dc9d7fe3d8fdd1cb35e1.json`](../../sessions/dc/dc9d7fe3d8fdd1cb35e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### Factorial vs hsweep_h2 对比（W&B 数据）

**决定性差异在 step 3→4**：
- **hsweep** (step-level adv): action_valid 91.3% → 43.1%，catastrophic collapse 启动，最终归零
- **factorial** (episode-level adv): action_valid 保持 79-85%，无崩溃

**V-shaped recovery 含义**：factorial 的 success dip (20.3%→3.1%) 是探索期波动（action_valid 始终 >79%），step 5 反弹到 15.63% 证明学习信号方向正确。hsweep 的 dip 伴随 action_valid 崩溃，是不可逆退化。

**结论**: **Sign misattribution 是 collapse 的 primary driver。** 两组共享相同 h=2 信息约束，episode-level advantage 完全阻止了 catastrophic collapse。Val 5.97% vs 最终 0% 有统计意义。3-cell factorial 结构清晰：sign misattribution 贡献 ~6pp (Cell1→Cell2)，information loss 贡献 ~22pp (Cell2→Cell3)。

**预测**: Factorial 不会 collapse，final val 预估 8-15%。完成后需 AlfworldSG_OOD re-eval（D064）。

---
