# infra registry field name unify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_registry_field_name_unify_20260520T085748_result.json`
- **Structured JSON:** [`ec76346a6d4d9c816798.json`](../../sessions/ec/ec76346a6d4d9c816798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新成功。

### 汇报

**修正的实验（4 个）：**

| exp_id | 旧字段名 | 新字段名 |
|--------|---------|---------|
| `adaptive_rho06_tau07_seed42` | `downstream_arc_easy` | `downstream_arc_easy_acc_norm` |
| `adaptive_rho06_tau07_seed456` | `downstream_arc_challenge` | `downstream_arc_challenge_acc_norm` |
| `adaptive_rho06_tau07_seed123` | `downstream_hellaswag` | `downstream_hellaswag_acc_norm` |
| `adaptive_fix_seed42` | `downstream_piqa` | `downstream_piqa_acc_norm` |
| | `downstream_winogrande` | `downstream_winogrande_acc` |

**字段映射（每个实验均应用全部 5 项重命名）：**
- `downstream_arc_easy` → `downstream_arc_easy_acc_norm`
- `downstream_arc_challenge` → `downstream_arc_challenge_acc_norm`
- `downstream_hellaswag` → `downstream_hellaswag_acc_norm`
- `downstream_piqa` → `downstream_piqa_acc_norm`
- `downstream_winogrande` → `downstream_winogrande_acc`
- `downstream_mean` — 保持不变

**共修正 4 个实验，每个实验 5 个字段重命名，值不变。**

---
