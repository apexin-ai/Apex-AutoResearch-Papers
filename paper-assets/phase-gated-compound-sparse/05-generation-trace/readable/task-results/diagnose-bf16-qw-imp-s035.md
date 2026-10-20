# diagnose bf16 qw imp s035

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bf16_qw_imp_s035_20260514T093508_result.json`
- **Structured JSON:** [`a4eee32faeea139aec82.json`](../../sessions/a4/a4eee32faeea139aec82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**bf16_qw_imp_s035 诊断完成：SUCCESS**

Registry 已更新为 DONE/success，cron 已清除。关键结果：

| Phase | II median | II mean | PPL dense→both |
|-------|-----------|---------|----------------|
| high_sparsity | 0.023 [0.015, 0.038] | 0.164 [0.084, 0.250] | 1.074→2.344 |
| mid_sparsity | 0.958 [0.171, 3.558] | 8.073 [2.022, 16.895] | 1.133→20.991 |
| low_sparsity | 8.236 [6.156, 10.923] | 18.967 [14.501, 23.975] | 1.152→58.036 |

- Overall: **PASS**（CI overlap test PASS, sign reversal test FAIL）
- 50 problems 全部完成
- s=0.35 时 II 单调递增（high < mid < low），PPL 退化也明显递增，与 dose-response 预期一致
- 对比 s=0.10：s=0.35 的 II 值大约高 2 个数量级，PPL 退化也远更剧烈（low_sparsity both: 58 vs 3.2）

---
