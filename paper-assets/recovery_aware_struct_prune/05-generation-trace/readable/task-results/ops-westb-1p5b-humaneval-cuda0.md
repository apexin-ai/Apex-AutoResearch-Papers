# ops westb 1p5b humaneval cuda0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_1p5b_humaneval_cuda0_20260519T122211_result.json`
- **Structured JSON:** [`53e7677cddfb28d5edd5.json`](../../sessions/53/53e7677cddfb28d5edd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，进程正常。

**结果汇报：**

| 项目 | 值 |
|---|---|
| **运行 checkpoint** | `sft_standard_20_1p5b` (SFT Standard, 最高优先级) |
| **服务器/GPU** | westb-23072 cuda:0 |
| **PID** | 890559 |
| **exp_id** | `eval_humaneval_sft_standard_20_1p5b_2048` |
| **日志** | `~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log` |
| **预计完成** | ~30-40 min (约 20:55-21:05) |

**westb 上所有可用 1.5B checkpoints：**
- `sft_standard_20_1p5b` ← 当前在跑
- `grpo_rasp_20_1p5b`
- `sft_rasp_20_1p5b`
- `grpo_standard_20_1p5b` (已传 westd 待启动)
- `sft_cka_only_20_1p5b` (westd 已在跑)
- `pruned_cka_only_20_1p5b` / `pruned_rasp_20_1p5b` / `pruned_standard_20_1p5b` (剪枝基底)

**修复内容：** eval_humaneval.py 第 18 行添加 `import sys`，第 81 行 subprocess 改用 `sys.executable`。

---
