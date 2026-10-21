# code conditional correlation analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_conditional-correlation-analysis_20260517T162844_result.json`
- **Structured JSON:** [`e53d66cfdf08ceeb1144.json`](../../sessions/e5/e53d66cfdf08ceeb1144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。关键发现与预期**完全相反**：

## Conditional Correlation 结果

| 指标 | 值 |
|---|---|
| Within FAILED episodes: r(adv, step_return) | **0.6400** (p=3.92e-44, n=371) |
| Within SUCCESS episodes: r(adv, step_return) | **0.9115** (p=6.30e-12, n=29) |
| Partial correlation (controlling outcome) | **0.8677** |
| Unconditional | 0.9006 |

## 判断

**Sign misattribution 假说不成立。** 具体证据：

1. **Within-failure r=0.64 远非 ≈ 0**：即使在失败 episode 内部，advantage 仍然强烈追踪 local step quality (step_return)。这直接否定了 "失败 episode 内 advantage 对所有 step 一视同仁" 的假设。

2. **Partial correlation r=0.87**：控制 episode outcome 后，advantage vs step_return 的相关性从 0.90 仅降至 0.87。episode outcome 对 unconditional correlation 的 confounding 效应极小。

3. **先前的 within-failure variance=6.9e-5 线索为什么误导**：失败 episode 的 advantage 绝对方差小是因为失败 episode 的 step_return 本身范围窄（都是负值、差异小），不是因为 advantage 不区分 step。r=0.64 说明在这个窄范围内 advantage 仍然跟踪了 local quality 的相对差异。

step_independent 模式确实在做 local credit assignment，不只是 episode-level 的 sign 分配。

---
