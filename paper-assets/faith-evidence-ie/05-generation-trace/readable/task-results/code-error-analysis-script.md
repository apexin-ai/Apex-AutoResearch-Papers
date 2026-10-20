# code error analysis script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_error_analysis_script_20260518T144152_result.json`
- **Structured JSON:** [`0cf280eb1d8fe0bfc694.json`](../../sessions/0c/0cf280eb1d8fe0bfc694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FP 子类计数已修复（1.7B: 4748+582=5330 == Total FP）。

脚本完成，输出位于 `/root/autodl-tmp/analysis/error_analysis/`：

| 文件 | 内容 |
|------|------|
| `{eval}_errors.csv` | 每个 eval 的分类统计 |
| `{eval}_per_relation.json` | 每个关系的 TP/FP/FN 明细 |
| `comparison.csv` | 多 eval 横向对比 |
| `error_analysis_table.tex` | LaTeX 表格，可直接放论文 |
| `per_relation_all.json` | 合并的 per-relation 数据 |

关键发现（3 个 SFT baseline 对比）:
- **FP**: 主要是 hallucinated relation（~89%），relation confusion 占 ~11%
- **FN**: cross-sentence miss 和 truncation loss 占主导，rare relation miss 相对少
- **Evidence**: exact match 65-70%，over-citation 和 under-citation 各 ~15%，evidence shift 很低（<2%）
- 1.7B→8B→Llama-8B 升级时，duplicates 显著下降（4538→4075→2624），truncation loss 也降

---
