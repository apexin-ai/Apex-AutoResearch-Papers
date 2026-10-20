# eval volctrl and gsm8k d000

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_volctrl-and-gsm8k-d000_20260523T060726_result.json`
- **Structured JSON:** [`00f7458249f0e6b64a4c.json`](../../sessions/00/00f7458249f0e6b64a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中。任务已在 tmux session `eval_falcon3` 中运行。

**已提交的 eval：**
- **Eval 1** (`eval_falcon3_volctrl_s42`): Falcon3-7B + volume_control adapter → MMLU, ARC-Challenge, GSM8K
- **Eval 2** (`eval_falcon3_d000_gsm8k_s42`): Falcon3-7B base (无 adapter) → GSM8K

输出路径：
- `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_volume_control_s42_aligned/`
- `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_d000_s42_aligned/`

日志：`/root/autodl-tmp/exp001/logs/eval_falcon3_all.log`

tmux session: `eval_falcon3`，GPU 0，`CUDA_VISIBLE_DEVICES=0` 已显式设置。

---
