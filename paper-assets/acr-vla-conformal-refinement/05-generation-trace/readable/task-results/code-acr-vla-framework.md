# code acr vla framework

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acr-vla-framework_20260513T022916_result.json`
- **Structured JSON:** [`cd51aa6be8365c6d995b.json`](../../sessions/cd/cd51aa6be8365c6d995b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 报告

| 项目 | 状态 |
|------|------|
| 文件创建 (7/7) | `__init__.py`, `cgs.py`, `aci.py`, `crm.py`, `train_crm.py`, `evaluate.py`, `utils.py` |
| CGS import | OK |
| ACI import | OK |
| CRM import | OK |
| Utils import | OK |
| train_crm.py --help | OK |
| evaluate.py --help | OK |

**CRM 参数量**: 226,595（非 ~131K）。差异原因：`obs_dim=512` 使第一层输入维度为 592（35+45+512），导致参数量偏高。若要达到 ~131K，需将 `obs_dim` 降至约 140，或将 `hidden_dim` 从 256 降至约 190。这取决于 SmolVLA encoder 实际输出维度，后续确定后调整。

---
