# submit sft 3B d100 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sft_3B_d100_v2_20260514T043849_result.json`
- **Structured JSON:** [`6ad70c31b1d828240f58.json`](../../sessions/6a/6ad70c31b1d828240f58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**总结：**

1. **eval_3B_d000_s123 已完成**，registry 更新为 DONE (success)：
   - MMLU: 63.62% | GSM8K: 17.59% | ARC-Challenge: 82.94% | HumanEval: 8.54%

2. **exp_001_sft_d100_3B 已提交到 GPU 3**（PID 291373）：
   - tmux session: `exp_001_sft_d100_3B`
   - 日志确认正在运行：数据格式化进度 20%/66533 samples
   - `libnvJitLink.so.13` 警告无害，训练正常推进
   - registry 状态: RUNNING

注意：因 `submit_training_job` MCP 工具不在当前 session，我手动通过 tmux 提交并设置了 exit sentinel（`/tmp/agent-ml-exit/exp_001_sft_d100_3B.exit`），与框架的 cron 监控兼容。`--gpu 0` 配合 `CUDA_VISIBLE_DEVICES=3` 正确映射到物理卡 3。

---
