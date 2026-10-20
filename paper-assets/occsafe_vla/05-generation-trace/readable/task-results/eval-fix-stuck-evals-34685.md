# eval fix stuck evals 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fix_stuck_evals_34685_20260526T232112_result.json`
- **Structured JSON:** [`8f606a8ebfe7bdfddae7.json`](../../sessions/8f/8f606a8ebfe7bdfddae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

杀掉重复进程后 cuda:3 显存从 33553 MiB 降到 16778 MiB，正常。

**结果汇总：**

| Eval | GPU | 状态 | 进度 |
|------|-----|------|------|
| vanilla_v2_s1_eval | cuda:0 | RUNNING | Task 8/10 (80%) |
| vanilla_v2_s2_eval | cuda:1 | RUNNING (之前已正常) | Task 7-8/10 |
| detach_ln_s3_eval | cuda:2 | RUNNING (nohup) | Task 3/10 (30%) |
| cutoff_25k_s1_v2_eval | cuda:3 | RUNNING (tmux) | Task 0/10 (刚启动) |

**做了什么：**
1. 发现 2 个"stuck"实验实际已被其他 agent 通过 nohup 修复并在运行（用了正确的 `evaluate_safelibero.py`）
2. 杀掉 cuda:3 上重复的 nohup 进程 (PID 567681)，保留 registry 追踪的 tmux 进程
3. 将 3 个 eval 的 registry 状态从 PREPARING 更新为 RUNNING（vanilla_v2_s1_eval, detach_ln_s3_eval, cutoff_25k_s1_v2_eval）

4 张卡全部在跑 eval，各占 ~17GB 显存。

---
