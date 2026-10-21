# code design update

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_design_update_20260520T142026_result.json`
- **Structured JSON:** [`3144afa47a1597d33000.json`](../../sessions/31/3144afa47a1597d33000.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。变更摘要：

| 文件 | 变更 |
|------|------|
| `src/design/generate_design.py` | 删除 `hardware`，precision 扩展为 `[float32, bfloat16, float16]`，assert 改为 108 |
| `src/inference/run_experiment.py` | `--hardware` → `--precision` 过滤 + `--gpu-id` 参数，删除 output record 中的 hardware 字段 |
| `src/analysis/variance_decomposition.py` | ALL_FACETS 从 7→6，FIXED_FACETS 从 3→2，均删除 hardware |
| `src/analysis/d_study.py` | FIXED_FACETS 删除 hardware |
| `src/analysis/visualize.py` | ALL_FACETS、FACET_LABELS、FIXED_FACETS 均删除 hardware |
| `run_mvp.sh` | 重写为 3 precision × 3 GPU 并行，无需传 hardware 参数 |
| `src/inference/sanity_check.py` | 新建，seed determinism 检查脚本 |

所有文件语法验证通过，`src/` 下无残留 hardware 引用。

---
