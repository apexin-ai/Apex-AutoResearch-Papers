# code dual judge calibration

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dual_judge_calibration_20260521T070927_result.json`
- **Structured JSON:** [`54404892402e8a70f168.json`](../../sessions/54/54404892402e8a70f168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

- **Binary κ = 0.65** (substantial agreement), 85% raw agreement
- **Weighted κ = 0.78** (substantial), 75% exact severity match
- **McNemar p = 0.61** — 两个 judge 无显著偏差方向 (GPT-4.1 only: 9, GPT-5.4 only: 6)
- Per-type κ 范围 0.38 (authorization_scope) 到 0.88 (incompleteness)
- Per-model κ 范围 0.52 (claude) 到 1.0 (gpt-4.1)

结果已保存到 `artifacts/full_study/analysis/dual_judge_calibration.json`。

---
