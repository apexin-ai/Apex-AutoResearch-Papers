# code plan001 collider mbias iv fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-collider-mbias-iv-fix_20260520T102055_result.json`
- **Structured JSON:** [`0aa557cfa2d77f82b266.json`](../../sessions/0a/0aa557cfa2d77f82b266.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结修复结果：

### Warning 1: C6 copy-paste bug — 已修复
- `C6_DIFF_BASE` → `C6_DIFFERENTIAL = [[0.85, 0.15, 0.05], [0.075, 0.70, 0.05], [0.075, 0.15, 0.90]]`
- Column-stochastic 验证通过，每列 sum = 1
- C6 结果已不同于 C1（collider: C6 bias=-0.0465 vs C1=-0.0506）

### Warning 2: 新增 misclass_amplifies metric — 已实现
- 新增 baseline: `theory_collider(np.eye(3))` / `theory_mbias(np.eye(3))` 计算真实 A 控制时的偏差
- Named C 表新增 `Bias_trueA` 和 `Amplif` 列
- Random search 新增 `misclass_amplifies_rate`（`|bias(A*)| > |bias(trueA)|` 的比例）
- 保留了原有 `ctrl_worse_rate`

### 关键发现
| DAG | ctrl_worse_rate | misclass_amplifies_rate | 解读 |
|---|---|---|---|
| Collider | 85.4% | **0.0%** | 误分类从不放大 collider bias（总是衰减） |
| M-bias | 62.7% | **29.2%** | ~29% 的随机 C 使误分类放大了 M-bias |

---
