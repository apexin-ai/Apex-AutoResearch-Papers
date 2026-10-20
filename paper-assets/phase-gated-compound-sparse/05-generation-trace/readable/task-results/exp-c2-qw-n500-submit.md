# exp c2 qw n500 submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c2-qw-n500-submit_20260514T135120_result.json`
- **Structured JSON:** [`318940f9bf10bafb9dbe.json`](../../sessions/31/318940f9bf10bafb9dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并运行中。

**状态汇总：**
- **GPU 2** (`c2_qw_n500_gpu2`): Qwen importance × 4 sparsity (s015→s020→s025→s030)，串行执行
- **GPU 3** (`c2_qw_n500_gpu3`): Qwen random × 4 sparsity (s015→s020→s025→s030)，串行执行
- 模型：`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`，bf16，~30GB 显存
- 两路均已开始处理 problem 1/500

**预计完成时间：** 参考 DeepSeek n=50 单 condition 约 20-30 分钟，n=500 约 10× ≈ 3-5 小时/condition，4 conditions 串行 ≈ **12-20 小时**（预计明天上午完成）。

---
