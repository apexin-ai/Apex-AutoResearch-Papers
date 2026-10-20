# diagnose gsm8k profiling ds

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k_profiling_ds_20260515T163742_result.json`
- **Structured JSON:** [`ae594dc84510d02d3b02.json`](../../sessions/ae/ae594dc84510d02d3b02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：gsm8k_profiling_ds 实验实际成功完成，Cron 误报 failed。**

- **DS importance**: 50/50 完成，Verdict PASS — importance masking 在 high/mid sparsity phase 的 II 显著正向（sparsity 0.3 时 II=+73.8 / +291.4），low_sparsity II≈0（符合预期）
- **DS random**: 50/50 完成，Verdict FAIL — random masking 无法区分 phase 类型，所有 phase 均有正 II（非选择性损失）
- **误报原因**: 进程正常退出后 PID 消失，Cron 检测到 "process dead" 但未检查 exit code（exit code = 0）；该脚本不使用 W&B，"无 W&B metrics" 判定也是误判
- **gsm8k_profiling_qw**: PID 245313/245314 健康运行中，GPU 利用率 96-97%，预计 ~1-2h 完成

Registry 已更新为 DONE/success。诊断报告已写入 artifacts。

---
