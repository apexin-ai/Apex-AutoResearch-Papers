# code plan 031 temporal granularity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_031_temporal_granularity_20260521T123458_result.json`
- **Structured JSON:** [`53b396948fea9c48189d.json`](../../sessions/53/53b396948fea9c48189d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

**MMLU 时间粒度**：
| 比较 | 时间距离 | N_ref | N_foc | C% | Random C% |
|------|---------|-------|-------|----|-----------|
| 2023 vs 2024 | 1yr | 1080 | 807 | 31.3% | 0.02% |
| 2023-H2 vs 2024-H1 | 0.5yr | 1018 | 807 | **34.4%** | 0.19% |
| 2023-H1 vs 2023-H2 | 0.5yr | 62 | 1018 | 22.6% | 0.18% |

**意外结果**：6个月的 2023-H2 vs 2024-H1 比较 C%=34.4%，比 1年的全量比较 (31.3%) 还高。这不符合"时间距离越大 DIF 越大"的线性预期，但有合理解释——2023-H2 vs 2024-H1 删除了 2023-H1 的 62 个"早期"模型（它们可能还没来得及被 benchmark 污染），使 reference group 更纯粹地由 2023 下半年模型组成，反而让 cohort 差异更锐利。

**跨 benchmark**：所有 benchmark 的 2023-H2 vs 2024-H1 C% 都略高于全量 2023 vs 2024，同样趋势一致。所有 C% >> random C%，确认信号是真实的时间效应。

输出文件在 `artifacts/plan_031_temporal_granularity/`：
- `plan_031_temporal_granularity.py`
- `temporal_granularity_results.csv`
- `plan_031_report.md`

---
