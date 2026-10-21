# fix bootstrap qwen7b path

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap-qwen7b-path_20260520T141201_result.json`
- **Structured JSON:** [`bce034b9a694caa3b5da.json`](../../sessions/bc/bce034b9a694caa3b5da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改内容**:
1. 在 westd 的 `results/eval_results_v2/` 创建了 Qwen-7B s123 的 5 个 dosage 的 `mmlu_results.json`（从 cqa1 数据）
2. `bootstrap_triple_seed.py` 新增 `load_eval_results_v2()` 函数，支持 `eval_results_v2/{family}_{dosage}_s{seed}/` flat 目录格式
3. `discover_data()` 现在按 CSV → mmlu_eval JSON → eval_results_v2 优先级合并数据

**Bootstrap 结果**:

| Family | n_seeds | Baseline | Δ(d100) | 95% CI | Pattern | ρ̄ |
|--------|---------|----------|---------|--------|---------|-----|
| Phi-4 | 1 | 76.44% | -0.17pp | [-0.17, -0.17] | Immune | --- |
| Qwen2.5-14B | 2* | 69.05% | -9.37pp | [-9.37, -9.37] | U-collapse† | --- |
| **Qwen2.5-7B** | **2** | 66.35% | -0.89pp | [-1.78, -0.89] | V-recovery† | 0.40 |
| Gemma-2-9B | 2 | 63.85% | +2.62pp | [+1.49, +2.62] | Benefit-sat† | 0.30 |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | 0.03 |

*Qwen2.5-14B s123 只有 d000-d005，所以 Δ(d100) 仍基于 n=1

**Qwen-7B pattern 不一致**：s42=V-recovery, s123=Immune（s123 的 d000=66.59%, d100=66.59% 几乎一样）。rho=0.40 表示两个 seed 的 dose-response 曲线有弱正相关。

†Pattern inconsistent across seeds

---
