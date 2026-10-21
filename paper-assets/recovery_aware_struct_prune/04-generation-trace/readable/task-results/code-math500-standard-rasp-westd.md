# code math500 standard rasp westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_math500_standard_rasp_westd_20260518T130004_result.json`
- **Structured JSON:** [`241a7b0616e000cb3265.json`](../../sessions/24/241a7b0616e000cb3265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正在加载 MATH 数据集。任务正常运行。

**汇报：**

- **PID**: 2261
- **tmux session**: `math500_standard_grpo_fair`
- **状态**: 从头跑（无已有结果文件，脚本不支持 resume）
- **GPU**: cuda:1 @ westd-29022，已占用 10421 MiB
- **日志**: `~/runs/recovery_aware_struct_prune/math500_standard_grpo_fair.log`
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair.json`
- **预计时长**: 参考 unpruned eval，500 题大约 30-60 分钟（剪枝模型更小，可能更快）

Standard eval 完成后，下一个 worker 负责启动 RASP GRPO MATH-500 eval（模型路径 `grpo_stage2_rasp_20_fair`）。

---
