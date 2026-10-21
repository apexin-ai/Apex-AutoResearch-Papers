# analysis r8 w3 dedup statistics

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8-w3-dedup-statistics_20260520T201613_result.json`
- **Structured JSON:** [`e320d5cb4c3ceb4faf01.json`](../../sessions/e3/e320d5cb4c3ceb4faf01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `westd-25068:/root/symb_invariant_consensus/results/r8_w3_dedup_statistics/`（`results.json` + `summary.md`）。

**核心数据（11 个条件，跨 3 个 benchmark）：**

| 条件 | N | Avg Pre | Avg Post | Dedup Ratio | Avg/Trace |
|------|---|---------|----------|-------------|-----------|
| **FOLIO** (6 models) | 204 each | 65.0 | 33.2 | **46.4%** | 6.0 |
| **ProofWriter** (3 models) | 600 each | 134.1 | 43.8 | **63.3%** | 12.0 |
| **LogiQA** (2 models) | 200 each | 48.1 | 39.2 | **18.8%** | 4.2 |

- 全局平均 dedup ratio = **46.0%**（范围 15.3%–75.8%）
- ProofWriter 冗余最高（规则化前提→重复约束模式），LogiQA 最低（自然语言前提→更多样化的约束提取）
- Qwen2.5-14B/PW 达 75.8% dedup ratio（最高），Mistral-7B/LogiQA 为 15.3%（最低）
- 16639 服务器的 per-problem 详细数据在 `westd-16639:/root/symb_invariant_consensus/results/r8_w3_dedup_statistics/results_16639.json`

---
