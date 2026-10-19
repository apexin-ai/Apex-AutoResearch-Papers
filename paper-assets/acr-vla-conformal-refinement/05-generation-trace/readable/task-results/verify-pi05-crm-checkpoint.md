# verify pi05 crm checkpoint

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pi05-crm-checkpoint_20260526T024935_result.json`
- **Structured JSON:** [`02892114568b6adbb346.json`](../../sessions/02/02892114568b6adbb346.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

## 结论：π0.5 CRM 实验**全部使用了正确的 checkpoint**，无误用。

关键证据：

| 维度 | π0.5 CRM | SmolVLA CRM |
|---|---|---|
| 文件大小 | 2,484,379 B | 1,320,219 B |
| MD5 | `25093621...` | `4161c640...` |
| 输入维度 | 2118 | 990 |
| 参数量 | 620,202 | 329,178 |

**不可能互换**——输入维度不同，误加载会在第一次前向传播时因 shape mismatch 崩溃。所有 eval 日志和 registry 记录均确认使用 `crm_pi05_unified_3suite/crm_best.pt`，obs_dim=2048。

报告已注册为 artifact: `art_20260526_2170d1`

---
