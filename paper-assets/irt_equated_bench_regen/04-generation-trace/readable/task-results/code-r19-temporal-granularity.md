# code r19 temporal granularity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19_temporal_granularity_20260522T184726_result.json`
- **Structured JSON:** [`413fbf5ab602fdfcdb31.json`](../../sessions/41/413fbf5ab602fdfcdb31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

| 比较 | N_ref | N_foc | C% | ρ | 方向 (foc/ref) |
|------|-------|-------|----|---|---------------|
| A: 2023-H1→H2 | 62 ⚠ | 1,018 | 22.6% | −0.608 | 62.3% / 37.7% |
| B: 2023-H2→2024-H1 | 1,018 | 807 | 34.3% | −0.594 | 40.6% / 59.4% |
| C: 2023-full→2024-H1 | 1,080 | 807 | 31.3% | −0.587 | 43.9% / 56.1% |

**关键发现：**

1. **C% 非单调递增**：A (22.6%) < C (31.3%) < B (34.3%)。B > C 是因为 C 的 ref 组加入了 62 个 2023-H1 模型，稀释了纯 H2 信号。但跨年比较（B、C）均远高于年内比较（A），**时间跨度越大 DIF 越严重**这个大趋势成立。

2. **ρ 梯度高度一致**：三组都在 −0.59 附近，**难题更容易出现 DIF 这个规律不随时间窗口变化**。

3. **方向分布翻转**：A 是 focal-favoring 主导（62.3%，即 2023-H2 模型在 DIF 项上表现更好），而 B、C 翻转为 ref-favoring 主导（59.4% / 56.1%，即 2023 模型在 DIF 项上更强）。这意味着跨年对比中，**2024 模型在 DIF 项上系统性劣于 2023 模型**——与"新模型更可能在被污染项上获利"的直觉相反，需要在 paper 中讨论。

产出文件：
- `artifacts/r19_temporal_granularity/temporal_granularity_analysis.py`
- `artifacts/r19_temporal_granularity/temporal_granularity_results.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_items.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_report.md`

---
