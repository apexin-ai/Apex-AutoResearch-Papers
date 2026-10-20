# ssh prep v4 eval scripts

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-v4-eval-scripts_20260514T142517_result.json`
- **Structured JSON:** [`89b3cc9d848ca9788ec2.json`](../../sessions/89/89b3cc9d848ca9788ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**eval/recovery.py 参数确认**：`--model_path`、`--base_model`、`--output`、`--no_inject`、`--device cuda:0`（与预期一致）

**scripts/run_v4_eval.sh 已创建**，语法验证通过。支持：
- `bash scripts/run_v4_eval.sh taxei` → cuda:0
- `bash scripts/run_v4_eval.sh random` → cuda:1
- `bash scripts/run_v4_eval.sh both` → 并行启动

脚本自动查找最新 run 目录下最大 step 的 checkpoint，并验证 `adapter_config.json` 存在后再执行。

**v4 训练进度**：step 1705/3387（epoch 1.51/3），约 54 分钟后完成，final checkpoint 将在 step 3387。

**v4-vanilla-eval-r2**：PID 61793 已停止，失败原因 — `checkpoints/mini_vanilla_sft_v4/v0-20260514-122641/checkpoint-1635` 缺少 `adapter_config.json`。

---
