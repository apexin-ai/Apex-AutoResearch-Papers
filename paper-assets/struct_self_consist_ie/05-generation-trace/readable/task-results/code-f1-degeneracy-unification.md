# code f1 degeneracy unification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_f1_degeneracy_unification_20260518T132220_result.json`
- **Structured JSON:** [`75d372027850e2b4a827.json`](../../sessions/75/75d372027850e2b4a827.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

**已修改的文件:**
- `code/analyze_fewnerd_results.py` (line ~163-165): 原来用 `len(set(sample_f1s)) == 1`（raw float 比较），改为 `len(set(round(float(f), 10) for f in sample_f1s)) == 1` + 注释。实际上原定义已经是 F1-based，但缺少 float rounding 的鲁棒性处理。

**其他文件中 degeneracy 定义现状（未修改）:**

已统一为 F1-based 的：
- `code/analyze_exp023_rank8_full.py:177` — `round(f, 6)`，F1-based ✓
- `code/d140_oracle_gated_analysis.py:107` — `round(f, 10)`，F1-based ✓
- `output/d112_hybrid_strategy/compute_hybrid.py:137` — `np.var(f1s) < 1e-10`，F1-based ✓
- `output/exp_025_n_ablation/n_ablation.py:151` — `round(f, 8)`，F1-based ✓

仍为 KeySet-based 的（需后续统一）：
- `code/analyze_per_type_lp.py:86` — `len(set(key_sets)) == 1`
- `code/analyze_per_type_lp_scierc.py:81,133` — `len(set(key_sets)) == 1`
- `code/statistical_hardening.py:160` — `len(set(key_sets)) == 1`
- `code/exp026_temp_ablation_metrics.py:42-53` — KeySet surface set 比较
- `scripts/n_scaling_gf_maxlp.py:89-95` — entity surface frozenset 比较

---
