# code unified metrics migration audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_metrics_migration_audit_20260518T213153_result.json`
- **Structured JSON:** [`7630bd743dfac69aa328.json`](../../sessions/76/7630bd743dfac69aa328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### 1. 全局审计结果

**96 个脚本**仍使用旧 `from evaluation import`。但经验证：**旧 `evaluation.per_instance_f1` 和新 `unified_metrics.compute_entity_f1` 数值完全一致**（两者都用 `(start, end, type)` 集合匹配，唯一差异是 both-empty 返回 1.0 vs 0.0，但所有脚本已过滤空 gold 实例）。

已迁移：`analyze_fewnerd_results.py`（关键路径脚本）
剩余 95 个脚本：数值正确，仅是 import 路径统一性问题，非紧急。

### 2. FewNERD 3-seed unified_metrics 正确数字

| 指标 | seed=42 | seed=123 | seed=456 | Mean ± Std |
|------|---------|----------|----------|------------|
| Greedy F1 | 0.7478 | 0.7480 | 0.7486 | 0.7482 ± 0.0003 |
| Oracle F1 | 0.8719 | 0.8772 | 0.8751 | 0.8747 ± 0.0022 |
| Headroom | 12.40pp | 12.92pp | 12.65pp | 12.66 ± 0.21pp |
| Degeneracy | 13.8% | 13.1% | 12.1% | 13.0 ± 0.67% |
| LP Δ | +1.36pp | +1.44pp | +1.37pp | +1.39 ± 0.04pp |
| N (gold-filtered) | 32565 | 32565 | 32565 | — |

### 3. 回归验证：PASS
- SciERC 529: greedy=0.6439 (expect 0.6439), degen=0.178 (expect 0.178)

### 4. 产出文件
- `output/exp_021_inference/results.json` — seed42 完整分析
- `output/exp_021_fewnerd_n8_seed123/results.json` — seed123 完整分析
- `output/exp_021_fewnerd_n8_seed456/results.json` — seed456 完整分析
- `output/fewnerd_multiseed_unified_v2.json` — 三 seed 汇总 + cross-seed summary
- `output/fewnerd_multiseed_unified.json` — 已删除

---
