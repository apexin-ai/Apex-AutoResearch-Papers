# analysis compile paper results tables v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile_paper_results_tables_v2_20260516T164337_result.json`
- **Structured JSON:** [`f7ab1b6d44b7dcd8ee70.json`](../../sessions/f7/f7ab1b6d44b7dcd8ee70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个表格全部编译完成并注册：

| 文件 | 内容 |
|------|------|
| `table2_main_results.md` | 3 模型 × 2 数据集 × ZS/FT，完整 violation rates |
| `table3_composability.md` | FT+OntoCoDec 即插即用，Δ metrics |
| `table4_ft_ablation.md` | 4 modes ablation（Llama DocRED semantic_only 标注 RUNNING） |
| `table5_posthoc.md` | Post-hoc filtering 对比，ZS+FT |
| `table6_latency.md` | SciERC +2.3% / DocRED +5.3% overhead |

缺失数据：
- `latency_profiling_scierc` / `latency_profiling_docred` registry 中无此 ID，数据从 artifacts 文件读取
- `phase1_scierc_zs_qwen` / `phase1_docred_zs_qwen` 实际 ID 为 `phase2_scierc_unconstrained` / `phase2_docred_unconstrained`
- `phase2_llama_*` 实际 ID 为 `llama_scierc_full_s1` / `llama_docred_full_s1` 等
- `w8_llama_docred_ft_semantic_only` 状态 RUNNING，Table 4 中标注
- `w8_zs_posthoc_baseline` 不存在，数据合并在 `w8_ft_posthoc_baseline` 的 `zs_regime` 字段中

---
