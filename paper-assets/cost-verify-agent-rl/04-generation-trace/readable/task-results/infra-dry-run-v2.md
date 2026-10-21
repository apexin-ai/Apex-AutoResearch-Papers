# infra dry run v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dry-run-v2_20260513T180908_result.json`
- **Structured JSON:** [`ca5b67e2338c7d00f854.json`](../../sessions/ca/ca5b67e2338c7d00f854.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/alfworld_dryrun_report.md`。

## 验证结果总结

**PASS** — RAGEN ALFWorld 训练流水线在 vLLM 0.18.1 下完整跑通。

| 验证项 | 结果 |
|--------|------|
| vLLM 0.18.1 兼容性 | **兼容**，无需降版本/适配 |
| 训练流水线 | **完整**，GRPO rollout→reward→update 全通 |
| 稳态 step/h | **~36.5**（98.64s/step） |
| ALFWorld 环境交互 | **正常**，8810 训练 games 加载，agent 产生 action 并收到 reward |

**修复了 2 个问题**：
1. `flash_attn` 缺失 → 改为 try/except lazy import（2 文件）
2. `ALFWORLD_DATA` 环境变量 → 指向 `/root/autodl-tmp/alfworld/`

---
