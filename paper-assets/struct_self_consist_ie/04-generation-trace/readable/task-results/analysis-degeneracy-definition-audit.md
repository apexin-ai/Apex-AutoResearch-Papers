# analysis degeneracy definition audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_degeneracy_definition_audit_20260521T021958_result.json`
- **Structured JSON:** [`8dc0eb17c5f124729267.json`](../../sessions/8d/8dc0eb17c5f124729267.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 根因

代码库中存在 **两套 degeneracy 定义**，但它们并不是导致"趋势相反"的原因：

| 定义 | 使用位置 | 判断标准 |
|------|---------|---------|
| **Constant-F1** | `unified_metrics.py`, `analyze_fewnerd_results.py` | 所有 N 个 sample 的 entity-level F1 完全相同 |
| **KeySet(text,type)** | `exp026_temp_ablation_metrics.py` | 所有 N 个 sample 的 entity surface set 完全相同 |

Constant-F1 ≥ KeySet（相同 entity set → 相同 F1，但不同 entity set 可能碰巧 F1 相同），差距约 3–7pp。

### 统一定义后的结果

**所有三个数据集在两种定义下都是 T↑ → degeneracy↓**：

| Dataset | T=0.5 | T=0.8 | T=1.0 | T=1.2 | 趋势 |
|---------|-------|-------|-------|-------|------|
| SciERC (CF1) | 41.4% | 23.8% | 17.8% | 14.9% | T↑→degen↓ |
| CoNLL (CF1) | — | — | 59.3% | 51.9% | T↑→degen↓ |
| FewNERD (CF1) | — | — | 13.1% | 8.0% | T↑→degen↓ |

### "FewNERD T↑→degen↑" 的真实来源

这不是定义不一致造成的，而是 **instance pool 不匹配**：
- FewNERD T=1.0 用了 `exp_027_fewnerd_n16`（5000 instances, N=16 的子集）
- FewNERD T=1.2 用了 `exp_031_fewnerd_t12`（37648 instances, N=8 全量）
- 不同子集 + 不同 N 导致伪趋势

### 产出
- 代码：`code/unify_degeneracy.py`（服务器 + 本地 artifacts/）
- JSON：`output/unified_degeneracy_audit/unified_degeneracy_3def.json`
- 论文可用的结论：**T↑ → degeneracy↓ 在所有数据集上一致成立**，可以直接用 Constant-F1 定义报告

---
