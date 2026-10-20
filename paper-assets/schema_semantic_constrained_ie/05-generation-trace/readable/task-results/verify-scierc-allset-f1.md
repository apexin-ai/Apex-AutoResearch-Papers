# verify scierc allset f1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_scierc_allset_f1_20260514T135218_result.json`
- **Structured JSON:** [`8ee339c82a69a0d9d370.json`](../../sessions/8e/8ee339c82a69a0d9d370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果：

### SciERC all_set R-F1 与 registry 一致性

| Mode | Registry R-F1 | all_set R-F1 | 匹配 | Unrecognized |
|------|-------------|-------------|------|-------------|
| unconstrained | 8.23% | 8.23% | **一致** | 24/1724 (1.39%) |
| grammar_only | 8.23% | 8.23% | **一致** | 0/1725 (0.00%) |
| semantic_only | 8.15% | 8.15% | **一致** | 26/1726 (1.51%) |
| full_s1 | 8.36% | 8.36% | **一致** | 0/1729 (0.00%) |

### 关键确认

1. **violation_checker.py 的 F1 计算已是 all_set 方法**——`compute_f1(gold_rels, relations, rel_key)` 传入全部 predictions，OOV relations 进入 pred_set 计为 FP。
2. **4 个实验的 all_set R-F1 与 registry 完全一致**，无需更新。
3. **all_set vs recognized_set 差异极小**：unconstrained -0.07pp，semantic_only -0.08pp，grammar_only 和 full_s1 无差异（两者 unrecognized=0，grammar constraint 已消除 RV violations）。

---
