# fix permutation test add math

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_permutation_test_add_math_20260521T104726_result.json`
- **Structured JSON:** [`4fb874993278c51f42b9.json`](../../sessions/4f/4fb874993278c51f42b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`BENCHMARK_ORDER` 已更新为 5 个 benchmark：`['mmlu', 'arc', 'hellaswag', 'gsm8k', 'math']`。

- 语法检查通过
- 排列数由代码动态计算（`permutations(range(len(available_benchmarks)))`），k=5 时自动为 5!=120，p_min=1/120≈0.008
- 无其他 hardcoded benchmark 数量需要修改

---
