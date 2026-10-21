# analysis theorem1 violation

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theorem1-violation_20260523T071732_result.json`
- **Structured JSON:** [`8eb09ebea14ebc484462.json`](../../sessions/8e/8eb09ebea14ebc484462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `theorem1_violation.json`。核心发现：

**整体**: 1,081,545 ordered pairs 中 290,316 违反单调性 (violation rate = 26.8%)，73.2% 满足 Theorem 1 预测。

**关键 pattern**:

1. **Near-tie 效应显著** — η_gap 最小的 Q1 quartile violation rate 40.2%，最大的 Q4 仅 16.5%。说明大部分违反发生在 η_max 差距小的 pair 间（noise-dominated regime），差距大时单调性基本成立。

2. **Panel 组成是最强预测因子**:
   - `local_only→api_only`（local 面板 η_max 更高）: violation rate 仅 0.45% — 几乎完美单调
   - `api_only→local_only`（API 面板 η_max 更高）: violation rate 84.8% — 几乎全部违反
   - 解释: API 模型个体 ASR 低（η_max 低），但 local 模型在 panel 中通过 majority vote 获得 diversity bonus，使得 panel ASR 反而可以低于预期。这正是 Theorem 1 的前提条件 "correlated judges" 在异构面板中不成立的表现。

3. **攻击类型**: prompt_injection 违反率最低 (23.0%)，authority_bias 最高 (31.1%)。Implicit bias 类攻击（authority/sycophancy）违反率更高，可能因为其 ASR 方差更大、更接近 noise floor。

4. **K_eff gap**: 违反对中 K_eff 差异 mean=0.30, median=0.26，说明违反往往涉及 K_eff 差异显著的面板——即 diversity 差异抵消了 η_max 的排序。

---
