# ops diag signals 05B s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diag_signals_05B_s123_v2_20260516T123003_result.json`
- **Structured JSON:** [`de5282c1efc6c8ad7b34.json`](../../sessions/de/de5282c1efc6c8ad7b34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中已清除或过期）。

## 诊断结果：exp_002_signals_05B_s123_v2 — 成功

**完成内容**：4 dosages × 3 benchmarks × 3 signals = 全部 12 组信号完整输出

| Dosage | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| d000_s123 | ✓ | ✓ | ✓ |
| d005_s123 | ✓ | ✓ | ✓ |
| d025_s123 | ✓ | ✓ | ✓ |
| d100_s123 | ✓ | ✓ | ✓ |

每组均含 s1_embedding + s2_minkpp + s4_selfcritique + signals_merged。

**退出原因**：shell 脚本在所有信号计算完成后触发了 bash 语法错误（`run_05B_s123_signals.sh` line 39-40 的 `continue`/`fi` 位置错误），但不影响实际产出。

**Registry 已更新为 `conclusion: success`。**

---
