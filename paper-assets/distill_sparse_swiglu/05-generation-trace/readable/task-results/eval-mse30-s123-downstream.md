# eval mse30 s123 downstream

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mse30_s123_downstream_20260522T092556_result.json`
- **Structured JSON:** [`3f7f5e5ebbe7f33407ff.json`](../../sessions/3f/3f7f5e5ebbe7f33407ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并运行：

- **exp_id**: `mse30_s123_downstream`，parent=`mse30_s123`
- **Server/GPU**: westd-41718 cuda:0，PID=399560
- **Log**: `/root/runs/distill_sparse_swiglu/mse30_s123_downstream.log`
- **Status**: RUNNING（spec 已写入，含 seed=123、checkpoint_source、eval_data、git_commit）
- **进度**: checkpoint 加载完成，模型级稀疏度 0.273（uniform 30% 目标合理），lm-eval 已进入 arc_challenge ~84%
- **注意**: 项目用 `submit_training_job` 提交对应 Agent 角色工具，Worker 角色只能 `ssh_execute`，按 C002 用 nohup + 日志重定向；功能等价
- **注意**: remote 项目目录不是 git repo，`git_commit` 按 skill 规范标为 `no-git: &lt;reason>`

---
