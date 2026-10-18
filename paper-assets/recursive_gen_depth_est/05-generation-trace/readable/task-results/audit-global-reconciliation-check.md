# audit global reconciliation check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_global_reconciliation_check_20260515T045928_result.json`
- **Structured JSON:** [`d5c94090ee4cf3fcf821.json`](../../sessions/d5/d5c94090ee4cf3fcf821.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Reconciliation 完成。文件已写入 `/root/autodl-tmp/recursive_gen_depth_est/artifacts/reconciliation_check.md`（231 行）。

## 结果总览

| 检查项 | 数量 | 匹配 | 差异 |
|--------|------|------|------|
| Pipeline vs edd_sensitivity AUC | 27 consecutive pairs | **27/27** | 0 |
| Pipeline vs Registry AUC | 41 pairs (有数据的) | **41/41** | 0 |
| Battery accuracy vs Registry | 9 cells | **9/9** | 0 |
| EDD T=0.75 vs Registry | 9 cells + 2 summaries | **全部** | 0 |

## 发现的问题

1. **Registry 字段命名错误**：`baseline_battery_9cell_001.best_acc_matrix_rf` 实际存储的是**所有方法中的最优 accuracy**，不是 RF accuracy。影响 olmo_topk50：registry 记 0.759（实为 LR），RF 实际为 0.737，差 2.2pp。如果论文引用此字段作为"RF accuracy"会出错。

2. **Registry 覆盖缺口**：54 个 pipeline AUC pair 中有 13 个无 registry 对应条目（olmo_temp09 缺 5/6，gpt2xl_topk50 缺 5/6，pythia_nucleus 缺 3/6）。值在 pipeline 文件中存在，但未入 registry。

3. **核心论文数值无问题**：所有 AUC（pipeline ↔ edd_sensitivity）完全一致，EDD 值一致。Battery 与 pipeline 的 AUC 差异均为随机种子方差（max |Δ|=0.015），非数据错误。

---
