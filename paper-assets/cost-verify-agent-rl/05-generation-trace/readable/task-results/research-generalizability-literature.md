# research generalizability literature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_generalizability-literature_20260518T032045_result.json`
- **Structured JSON:** [`ce81c6db830c84835362.json`](../../sessions/ce/ce81c6db830c84835362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，结果已写入 `artifacts/literature_sign_misattribution_evidence.md`。

**核心结论：sign misattribution 不是个例，至少 6 篇独立工作从不同角度报告了相同问题。**

按佐证强度分层汇总：

### Tier 1：直接佐证 sign/advantage 方向错误（6 篇）
| 论文 | 关键证据 |
|------|---------|
| **IRC** (2604.02869) | 唯一明确报告 A^I 与 A^O sign disagreement |
| **MC-GRPO** (2601.22582) | 5% sign-flip → 4% accuracy drop，定量分析 |
| **G-RA** (2508.10548) | step reward 与 outcome reward 方向反转可视化 |
| **GRPO-λ** (2510.00194) | Lemma 1 证明 GRPO advantage 对下游 tokens 有 systematic misattribution |
| **Outcome-Grounded Reshaping** (2601.07408) | 直接使用 "advantage misattribution" 术语 |
| **Decoupled CA** (ICLR 2026) | invalid actions 在 positive trajectories 中获得 positive credit |

### Tier 2：GRPO Collapse 系统性证据（6 篇）
- **RAGEN/RAGEN-2**: Echo Trap + advantage collapse 数学证明 (`|g_task| ≤ √Var(R|X)·C`)
- **Turn-PPO**: GRPO crash，3 种 fix 均失败
- **GiGPO** (NeurIPS 2025): step vs episode ablation，+13.3pp
- **GRPO Collapse/Search-R1**: 300 步内 4 模型全 collapse
- **Gradient Coupling**: 互补视角，gradient interference 机制

### Tier 3：理论基础（3 篇）
- **RUDDER** (NeurIPS 2019): TD bias 随 delay 指数增长
- **COCOA** (NeurIPS 2023): spurious contribution estimates
- **CA Survey** (2026): O(T·Var[R]) variance scaling

**我们的独特贡献**：直接测量 advantage-outcome sign agreement rate (52%≈随机) 并建立与 catastrophic collapse 的因果关系——其他工作没有做过这个定量分析。

---
