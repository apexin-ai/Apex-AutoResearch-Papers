# diagnose eval pass k8 standard 20 grpo qwen math v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pass_k8_standard_20_grpo_qwen_math_v2_20260516T232326_result.json`
- **Structured JSON:** [`0864bf56385f4b0dd8d3.json`](../../sessions/08/0864bf56385f4b0dd8d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**这是一个监控误报，实验实际已成功完成。**

| 项目 | 详情 |
|------|------|
| 根本原因 | 监控系统 false positive：eval 脚本正常退出后未写 sentinel 文件、未接 W&B，监控轮询时发现进程已死，5 次后判定为 failed |
| 实际结果 | GSM8K pass@8 = **0.9100 ± 0.0202** |
| 结果文件 | `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json` ✓ |
| 运行时间 | 05:54 ~ 07:05（约 1h11m），200 题全部完成 |

无需重跑。如要避免未来类似误报，可在 eval 脚本末尾加 sentinel 文件写入。

---
