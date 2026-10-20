# diag bf16 ds imp s010

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bf16_ds_imp_s010_20260514T093224_result.json`
- **Structured JSON:** [`fa6cfc3e5aa0f3f9318e.json`](../../sessions/fa/fa6cfc3e5aa0f3f9318e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 session 无 cron job，无需删除。

**诊断完成。** bf16_ds_imp_s010 实验总结：

- **状态**: DONE / negative
- **执行**: 50/50 problems 全部完成，无 error
- **结论**: 两项统计检验均 FAIL（ci_overlap_test, sign_reversal_test），importance masking 在 s=0.10 下未能支持 C2 单调递增 claim
- **关键数据**:
  - high_sparsity II: median=+0.003, mean=-0.200（极端负偏，skewness=-15.7）
  - low_sparsity II: median=+0.015, mean=-0.107（skewness=-11.2）
  - mid_sparsity II: median=+0.006, mean=-0.013（相对对称）
  - low_sparsity 的 KV pruning perplexity 异常高（5.00 vs dense 1.23），暗示 s=0.10 对 low-sparsity phase 的 KV cache 破坏严重
- **Registry**: 已更新为 DONE/negative，metrics 已写入
- **Cron**: 当前 session 无对应 cron

---
