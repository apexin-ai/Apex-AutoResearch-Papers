# verify table23 bt values

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_table23_bt_values_20260524T093035_result.json`
- **Structured JSON:** [`6b392f09d752b7cd6866.json`](../../sessions/6b/6b392f09d752b7cd6866.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

24 条记录的 trial choices 不同——两个文件来自不同的评估运行。

## 验证结果汇总

| Config | 文件 | NLI过滤后 n | 计算 BT | Table 23 期望 | 匹配 |
|--------|------|-----------|---------|-------------|------|
| AEval × Qwen3 × Formality | `pairwise_results_alpacaeval_qwen32b.jsonl` | 86 | **0.6569** | .657 | **匹配** (四舍五入 .657) |
| AEval × Qwen3 × Verbosity | `pairwise_results_alpacaeval_verbosity_qwen32b.jsonl` | 82 | **0.8414** | .841 | **匹配** (四舍五入 .841) |
| AEval × Llama-70B × Formality | `pairwise_results_alpacaeval_llama70b_formality.jsonl` | 86 | **0.7499** | .756 | **不匹配** → .750 (已知问题确认) |
| MTB × Qwen3 × Formality | `pairwise_results_mtbench_qwen32b.jsonl` | 73 | **0.7123** | .712 | **匹配** (四舍五入 .712) |

### 关键发现

1. **Config 1 & 2**：完全匹配 Table 23。NLI ≥ 0.90 过滤是关键（不过滤时分别为 .650 和 .840）。

2. **Config 3 (AEval × Llama-70B × Formality)**：当前数据计算为 **.750**，Table 23 报告 **.756**。
   - `cross_benchmark_local.json` 中的旧值为 0.7558（→ .756），与 Table 23 匹配
   - 当前 `pairwise_results_alpacaeval_llama70b_formality.jsonl`（5月24日生成）是更新后的数据，BT 降为 .750
   - 数据文件在 Table 23 制表后被重新生成了

3. **Config 4 (MTB × Qwen3 × Formality)**：
   - `pairwise_results_mtbench_qwen32b.jsonl`（NLI≥0.90）→ BT=0.7123 → **.712** ✅ 匹配
   - `scored_mtbench_qwen32b_formality.jsonl`（NLI≥0.90）→ BT=0.6986 → **.699** ❌ 不匹配
   - 两文件有 24/80 条 trial choices 不同，来自不同评估运行
   - `cross_benchmark_analysis.py` 当前配置指向 `scored_` 文件，会产生 .699 而非 .712
   - Table 23 的 .712 来自 `pairwise_results_` 文件

### 需要注意的问题

- **Config 3**：如需论文值与数据一致，要么用旧数据恢复 .756，要么将 Table 23 更新为 .750
- **Config 4**：`cross_benchmark_analysis.py` 的 `pairwise_file` 配置应改为 `pairwise_results_mtbench_qwen32b.jsonl` 以匹配 Table 23 的 .712

---
