# exp v5 full classify

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_v5_full_classify_20260512T211725_result.json`
- **Structured JSON:** [`48b0e004488e1efca09b.json`](../../sessions/48/48b0e004488e1efca09b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full results summary:

---

## datagen_classify_v2 结果 — P1 GATE: FAIL

### Post-process
| 类别 | 数量 | 比例 |
|------|------|------|
| true_success | 187 | 37.4% |
| truncated_success (CSF) | 4 | 0.8% |
| true_failure | 309 | 61.8% |

309 failures 中 91 为 PCB pattern，251/309 matched expert（58 unmatched）。

### error_type 分布（PCB override 后）
| error_type | N | % | correction_span mean | median |
|------------|---|---|---------------------|--------|
| action | 2 | 0.8% | 7.50 | 7.5 |
| verification | 82 | 32.7% | 10.44 | 8.0 |
| planning | 167 | 66.5% | 11.34 | 9.0 |

### llm_original_type（LLM 原始输出）
planning=247 (98.4%), action=4 (1.6%), verification=0

### 三版 KW 分析
| 版本 | N | H | p | ordinal |
|------|---|---|---|---------|
| with_override (Full) | 251 | 2.23 | 0.135 | ✓ |
| with_override (Dedup) | 144 | 1.33 | 0.249 | ✓ |
| without_override (Full) | 251 | 0.15 | 0.698 | ✗ |
| without_override (Dedup) | 144 | 0.08 | 0.778 | ✗ |
| pcb_excluded | — | SKIPPED | — | — |

### P1 Gate
**FAIL** — with_override p=0.135（未达 0.05），根本原因：action 组仅 N=2，LLM 把 98.4% 判为 planning。Ordinal ordering 成立（7.5 < 10.4 < 11.3）但统计不显著。Task-type stratified 0/6 显著。

---
