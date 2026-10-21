# research exp001 data schema

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp001-data-schema_20260517T042158_result.json`
- **Structured JSON:** [`d8eebe5992beddbcc976.json`](../../sessions/d8/d8eebe5992beddbcc976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是结论：

---

## 结果

### JSON Schema 树（`sica_expanded_14b.json`，804 题）

```
{
  "summary": { n_problems, sica_accuracy, sc_accuracy, ... },
  "results": [
    {
      "problem_idx": int,
      "problem_id": str,
      "problem": str,                    // 完整题目文本
      "dataset": "proofwriter"|"folio",
      "level": str,
      "ground_truth": str,
      "sica_answer": str,
      "sica_scores": {answer: float},
      "sica_correct": bool,
      "sc_answer": str,
      "sc_vote_count": int,
      "sc_vote_distribution": {answer: int},
      "sc_correct": bool,
      "constraints_stats": {
        "total_extracted": int,          // 所有 trace 提取的总约束数
        "traces_with_constraints": int,  // 有约束的 trace 数
        "unique_after_dedup": int        // z3 去重后唯一约束数
      },
      "maxsat_stats": {
        "satisfied": int,
        "excluded": int,
        "total_weight": float,
        "solve_time_ms": float
      },
      "timing": { trace_gen_s, extraction_s, dedup_s, maxsat_s, total_s },
      "trace_extraction_stats": { boxed, fallback, none },
      "truncated_traces": int,
      "raw_constraints": [],             // ⚠️ 始终为空
      "per_trace": [
        {
          "trace_idx": int,
          "answer": str,
          "finish_reason": str,
          "extraction_method": str,
          "trace_len": int               // token 数，无 trace 文本
        }
      ]
    }
  ]
}
```

### 核心回答：Per-trace raw constraints **不可用**

原因：exp-001 运行时未传 `--save-intermediates` 标志。`run_full_mvp.py:371-372` 表明只有开启该标志才会保存 `raw_constraints`。`extract_constraints_for_ablation.py` 文档字符串明确确认：

> "Since raw_constraints were not saved during the exp-001 run (--save-intermediates was not effective)"

### 已保存到什么粒度

| 粒度 | 可用？ | 说明 |
|------|--------|------|
| Per-trace answer | 有 | trace_idx + answer + finish_reason + trace_len |
| Per-trace 完整 trace 文本 | **无**（主文件）/ 43题有（traces_k20.json） | 主实验未保存 |
| Aggregate constraint stats | 有 | total_extracted / unique_after_dedup |
| Per-constraint expression + z3_formula + weight + source_traces | **无** | `raw_constraints` 始终 `[]` |
| MaxSAT 结果 | 有 | satisfied/excluded/total_weight |
| SICA scores (per-answer) | 有 | 最终加权分数 |

### 可用的 intermediate 文件

| 文件 | 内容 | 规模 |
|------|------|------|
| `constraint_cache/` (800+ JSONs) | per_trace answer + aggregate stats only | 804题 |
| `constraint_cache_consolidated.json` (827KB) | 同上，合并版 | 804题 |
| `k_ablation/traces_k20.json` (1.7MB) | **完整 trace 文本** + answer | **仅43题**, K=20 |
| `constraint_ablation.json` (335KB) | per-problem 多方法对比结果 | 804题 |

### 对 CPU-only constraint filtering 实验的影响

无法直接做，因为没有原始约束文本。可选方案：
1. **重跑 constraint extraction**：主文件有完整 problem text，用 `sica/constraint_extractor.py` 重新从 LLM 生成 traces 并提取约束（需 API 调用）
2. **小规模 pilot**：`traces_k20.json` 有 43 题的完整 trace，可以只对这 43 题做 CPU-only 约束提取+过滤（无需重新生成 traces，只需 extraction 步骤）
3. **重跑 exp-001 子集 + `--save-intermediates`**：选 100-200 题重跑，保留 raw constraints

---
