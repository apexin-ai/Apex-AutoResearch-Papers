# diag bf16 qw imp s010

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bf16_qw_imp_s010_20260514T093254_result.json`
- **Structured JSON:** [`b13f5dac279d9db8227f.json`](../../sessions/b1/b13f5dac279d9db8227f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中已清理或过期）。

---

**诊断结论：bf16_qw_imp_s010 — SUCCESS**

- 50/50 problems 全部完成，无 error
- Overall verdict: **PASS**（ci_overlap_test 通过：high_sparsity vs mid_sparsity CI 不重叠）
- 关键 metrics（II @ s=0.1）：

| Phase | II median | II mean | PPL dense→both |
|-------|-----------|---------|----------------|
| high_sparsity | +0.0001 | -0.089 | 1.074→1.228 |
| mid_sparsity | -0.036 | -0.084 | 1.133→1.741 |
| low_sparsity | -0.044 | -0.243 | 1.152→3.204 |

- Registry 已更新：status=DONE, conclusion=success, metrics 已填入
- Cron 无需删除（当前 session 无活跃 cron）

---
