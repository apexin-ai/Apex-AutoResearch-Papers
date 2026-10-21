# code w10 gtc results collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_gtc_results_collect_20260517T063832_result.json`
- **Structured JSON:** [`66a8e321b224f9e914a9.json`](../../sessions/66/66a8e321b224f9e914a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

最终汇总：

---

## GTC Results Summary

### SciERC (551 docs)
| Metric | Baseline (full_s1) | GTC Consensus | Delta |
|--------|-------------------|---------------|-------|
| Lines in output | 551 | 551 | 0 |
| ET% | 0.0% | 0.0% | 0 |
| RV% | 0.0% | 0.0% | 0 |
| DR% | 0.93% | 0.93% | 0 |
| CF% | 9.9% | 9.9% | 0 |
| E_F1 | 0.3098 | 0.3098 | 0 |
| R_F1 | 0.0836 | 0.0836 | 0 |
| GTC skips (total log lines) | - | 672 | - |
| GTC skips (unique entities) | - | 258 | - |

### DocRED (50 docs)
| Metric | Baseline (full_s1, same 50 docs) | GTC Consensus | Delta |
|--------|----------------------------------|---------------|-------|
| Lines in output | 50 | 50 | 0 |
| ET% | 0.0% | 0.0% | 0 |
| RV% | 0.0% | 0.0% | 0 |
| DR% | 8.69% | 8.69% | 0 |
| CF% | 2.4% (20/840) | 2.4% (20/840) | 0 |
| E_F1 | 0.5908 | 0.5908 | 0 |
| R_F1 | 0.0833 | 0.0833 | 0 |
| GTC skips (total log lines) | - | 601 | - |
| GTC skips (unique entities) | - | 213 | - |

### 结论

**GTC (Type Consensus) 在两个数据集上完全没有效果。** `parsed_output` 和 baseline 完全相同（仅 metadata 字段 `decoding_strategy`/`num_beams`/`inference_time_seconds` 有差异）。

**原因：所有 consensus 修改尝试都因 DR (Domain/Range) constraint 冲突被 SKIP 了。** GTC 的设计是"Layer 3 respects Layer 2's DR constraints"——当 consensus 想把 entity type 改成全局一致的 type 时，如果这个 type 不满足当前 relation 的 domain/range 约束，就被跳过。结果是 100% 的 consensus 尝试都被 DR conflict 否决了，GTC 相当于 no-op。

---
