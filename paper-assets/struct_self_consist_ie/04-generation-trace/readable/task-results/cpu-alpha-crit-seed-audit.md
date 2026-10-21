# cpu alpha crit seed audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_alpha_crit_seed_audit_20260521T092648_result.json`
- **Structured JSON:** [`eb6cd16a26218b3dde3c.json`](../../sessions/eb/eb6cd16a26218b3dde3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 1. 数据来源验证

| 数据集 | α_crit 表引用 seeds | 实际来源 | 实验 ID |
|--------|---------------------|----------|---------|
| FewNERD | (123, 456, 789) | entity_construction_fair_n8 | exp_021_inference + seed variants |
| CoNLL | (123, 456) | 未找到明确来源 | exp002_conll2003 + seed variants |
| SciERC | (456, 789) | entity_construction_fair_n8 | exp_012_rerun_1024 + seed variants |

### 2. 是否受 greedy_macro_f1 bug 影响

**是，全面受影响。** 证据：

- `fewnerd_seed789_merged/analysis.json` 字段名为 `greedy_macro_f1 = 0.7478`
- `entity_construction_fair_n8/multiseed_results.json` 的 `greedy_f1 = 0.7478`（同值，实为 macro-F1）
- 注册表 `exp_fewnerd_mf4_v2_s42` 明确标注："Replaces exp_021 which used incompatible greedy_macro_f1"
- MF4v2 micro-F1 = 0.7883 vs 旧 macro-F1 = 0.7478，差 **4.0pp**
- MV F1 受影响更严重：0.6561 (macro) → 0.7849 (micro)，差 **12.9pp**

### 3. 新旧数值对比

| 指标 | FewNERD old→new | CoNLL old→new | SciERC old→new |
|------|----------------|---------------|----------------|
| Greedy | 0.748→**0.791** | 0.908→**0.912** | 0.644→**0.666** |
| MV | 0.656→**0.785** | 0.894→**0.914** | 0.614→**0.670** |
| Δ_SC | −9.21→**−0.63pp** | −1.37→**+0.17pp** | −3.03→**+0.37pp** |
| Bound正确? | Yes→**Yes** ✓ | No→**Yes** ✓ | No→**Yes** ✓ |

**最重要的变化**：CoNLL 和 SciERC 的 Δ_SC 符号翻转（MV 从劣于 greedy 变为优于 greedy），α_crit bound 对全部三个数据集预测正确。"SC universally fails" 的结论需要修正为 "MV 与 greedy 接近持平，改善幅度远小于 oracle headroom"。

### 4. 已更新

`artifacts/alpha_crit_table.md` 已用 micro-F1 重算值更新，seeds 统一为 (42, 123, 456)，每个数据点标注来源实验 ID。重算脚本: `output/recompute_alpha_crit.py`，结果: `output/alpha_crit_recompute.json`。

---
