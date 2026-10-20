# data gate12 evidence files

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_gate12-evidence-files_20260514T122208_result.json`
- **Structured JSON:** [`b7dcccbf087f6a0ceb2e.json`](../../sessions/b7/b7dcccbf087f6a0ceb2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个证据文件已生成：

| 文件 | 大小 | Verdict |
|------|------|---------|
| `eval_results/gate1_injection_validity.json` | 714 B | **PASS** |
| `eval_results/gate2_recovery_quality.json` | 44.9 KB | **PASS** |

**Gate 1** — 760 条注入全部合法（100%），4 个算子均 100%：
- P1_step_order_swap: 188
- P2_sub_goal_deletion: 192
- C1_context_truncation: 191
- C4_observation_masking: 189

**Gate 2** — 60 条采样（每算子 15 条），strong=18, moderate=42, weak=0，pass rate=100% ≥ 75% 阈值。

---
