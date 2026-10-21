# code f1 inconsistency audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_f1_inconsistency_audit_20260518T175553_result.json`
- **Structured JSON:** [`144c5f9db951741405af.json`](../../sessions/14/144c5f9db951741405af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查完成

### 根因
`analysis_dgs_gold_filter.py` 第 114 行的 SciERC 数据路径指向旧实验 `exp001_n16_seed42/samples.jsonl`，而 `entity_consensus.py` 和 `ccs_selection.py` 使用当前实验 `exp_012_rerun_1024/samples.jsonl`。F1 计算逻辑和 gold_filter 实现在三个脚本中等价，唯一差异就是数据源。

### 修复
- 将 `analysis_dgs_gold_filter.py` 的 SciERC 路径从 `exp001_n16_seed42` 改为 `exp_012_rerun_1024`
- CoNLL 和 FewNERD 路径本来就一致，无需修改

### 验证结果（三个脚本完全一致）
| Dataset | Greedy F1 | N |
|---------|-----------|---|
| SciERC | 0.6439 | 529 |
| CoNLL | 0.9070 | 2756 |
| FewNERD | 0.7478 | 4351 |

### 附注
`entity_consensus.py` 未对 samples 截断到 N=8（CoNLL/FewNERD 用全部 16 个 samples），影响 LP/MV/Oracle 指标但不影响 Greedy F1。

审计结果已写入 `output/f1_audit_results.json`。

---
