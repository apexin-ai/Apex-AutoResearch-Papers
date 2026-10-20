# eval mvp 004 dedup final

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_004_dedup_final_20260515T004418_result.json`
- **Structured JSON:** [`c77a07ef479313609584.json`](../../sessions/c7/c77a07ef479313609584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前进度汇总：

**步骤 1-2 完成**：
- 原始 211 行 → 去重后 204 行 ✓
- 原始文件备份为 `mvp_v4_full_original_211.jsonl`

**步骤 3 完成 — 去重后原始评估**：
| Gate | All-mode | 阈值 | 状态 | Excl-Unknown | 状态 |
|------|----------|------|------|-------------|------|
| C1 disagree_rate | 39.6% (76/192) | ≥10% | PASS | 35.7% (45/126) | PASS |
| C2 diagnostic_rate | 86.8% (66/76) | ≥40% | PASS | 84.4% (38/45) | PASS |
| C3 error_types | 3 types | ≥2 | PASS | 2 types | PASS |
| C4 targeted_vs_blind | +6.2pp (T:60/96 B:54/96) | >5pp | PASS | -1.7pp (T:34/59 B:35/59) | FAIL |
| C5 localization | 85.4% (35/41) | ≥60% | PASS | 89.3% (25/28) | PASS |

C4 去重后从 +7.2pp 降至 +6.2pp，All-mode 仍 PASS。Excl-Unknown C4 仍 FAIL。

**步骤 4 进行中**：
- repair_only.py 已启动（PID 66854），204 条数据，86 个 repair target
- 之前跑的两个错误进程（197 条数据）已终止
- 预计约 170 分钟完成，会定期轮询进度

---
