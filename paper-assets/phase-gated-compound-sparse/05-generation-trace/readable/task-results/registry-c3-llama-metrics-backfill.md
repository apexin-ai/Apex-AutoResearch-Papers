# registry c3 llama metrics backfill

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_c3_llama_metrics_backfill_20260516T025245_result.json`
- **Structured JSON:** [`1b89026f8bc4c228e96d.json`](../../sessions/1b/1b89026f8bc4c228e96d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入成功。完整 metrics 结构：

| 字段 | 值 |
|------|-----|
| **imp_vs_rand d_z** | s015=0.19, s020=0.26, s025=0.29, s030=0.34（单调递增） |
| **phase_gradient_importance d_z** | 全部 large（1.00–1.12） |
| **phase_gradient_random d_z** | 全部 small（0.35–0.45） |
| **s030 Bonferroni p** | 0.029（显著） |
| **cross_arch delta** | LLaMA d_z 比 DeepSeek 高 0.20–0.59 |

Registry `c3_llama` metrics 字段已更新，包含 imp_vs_rand_dz、phase_gradient_{importance,random}_dz、median_diff、wilcoxon_p（含 Bonferroni 校正）、CI、cross_arch_comparison 等全部结构化数值。

---
