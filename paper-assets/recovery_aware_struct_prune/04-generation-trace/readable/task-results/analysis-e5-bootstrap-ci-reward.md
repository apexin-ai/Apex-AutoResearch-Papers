# analysis e5 bootstrap ci reward

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e5_bootstrap_ci_reward_20260518T100946_result.json`
- **Structured JSON:** [`3ea6b24e0e4f21fc284e.json`](../../sessions/3e/3ea6b24e0e4f21fc284e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**数据限制**: W&B 只存 aggregate metrics（mean, std），无 per-sample rewards。使用 parametric bootstrap（假设 CLT，n_eff=80 per interval）。

**Trajectory 级别平均 gap（95% CI，全部显著）**:

| Comparison | Gap | 95% CI | Favors |
|---|---|---|---|
| CKA-only vs Standard | +0.2351 | [0.205, 0.265] | CKA-only |
| CKA-only vs RASP | +0.2539 | [0.224, 0.282] | CKA-only |
| CKA-only vs Random | +0.1137 | [0.077, 0.151] | CKA-only |
| Standard vs RASP | +0.0187 | [0.006, 0.032] | Standard |
| Standard vs Random | -0.1153 | [-0.141, -0.091] | Random |
| RASP vs Random | -0.1313 | [-0.156, -0.107] | Random |

**关键发现**:
- CKA-only 显著优于所有其他方法（gap 0.11-0.25）
- Random pruning 显著优于 Standard 和 RASP（即 magnitude/RASP 剪枝反而不如 random）
- Standard 仅 marginally 优于 RASP（gap 0.019，CI 刚好不含 0）
- 所有结论对 n_eff∈{40,80,160} 稳健

Random 缺 step 100 数据（crash before sync）。结果已保存至 `artifacts/bootstrap_ci_reward_trajectories.json`。

---
