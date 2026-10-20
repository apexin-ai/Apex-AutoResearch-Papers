# code c2 n500 analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c2_n500_analysis_prep_20260514T173800_result.json`
- **Structured JSON:** [`560ae3b40245c51e30fa.json`](../../sessions/56/560ae3b40245c51e30fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出

**脚本位置**：`/root/autodl-tmp/pacs/pacs/profiling/analyze_n500.py`（也有一份在 `/root/autodl-tmp/pacs/profiling/analyze_n500.py`）

**运行方式**：
```bash
# n=500 正式数据
python -m pacs.profiling.analyze_n500 --model deepseek
python -m pacs.profiling.analyze_n500 --model qwen

# n=50 dry-run
python -m pacs.profiling.analyze_n500 --model deepseek --n50-only
```

**功能覆盖**：
| 功能 | 状态 |
|------|------|
| 数据完整性校验（n=500、problem_idx 单调性、重复 problem_id、NaN 值） | Dry-run 验证通过 |
| Per-condition mean/std/CI (B=10000) | 通过 |
| Paired d_z importance vs random (by problem_id) + Wilcoxon | 通过 |
| Dose-response Spearman ρ (II vs sparsity) | 通过 |
| Gini coefficient + CV + IQR | 通过 |
| JSON + 人类可读输出 | 通过 |

**目录结构**：
- n=50 bf16 数据：`profiling_output_bf16_{ds,qw}_{imp,rand}_s{015..030}/`
- n=500 数据（运行中）：`profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015..030}/`
- 目前 n500 目录都是空的（6个已创建，2个尚未创建），等实验完成后产出 `profiling_results.json`

**Dry-run 结果要点**（n=50）：
- DeepSeek：imp-vs-rand gradient d_z 从 +0.32 (s015) 递增到 +0.69 (s030)，全部 p<0.001
- Qwen：imp-vs-rand gradient d_z 不显著（符合预期，Qwen 的 importance vs random 差异主要在绝对 II 而非 gradient 上）
- Dose-response：两个模型的 importance 条件下 rho=1.0（完美单调递增）

---
