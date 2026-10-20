# ssh diag v4 vanilla checkpoint

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diag-v4-vanilla-checkpoint_20260514T142730_result.json`
- **Structured JSON:** [`23dcfd790edbe2e50c49.json`](../../sessions/23/23dcfd790edbe2e50c49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行中，已完成 8/47 episodes（6 OK, 2 FAIL）。bitsandbytes 警告无影响。

### 诊断结果

1. **checkpoint-1635 完整**，三个 checkpoint（545/1090/1635）都有 `adapter_config.json`
2. **之前 eval 失败原因**：路径错误。正确路径需包含 `v0-20260514-201441` 子目录层级：
   ```
   checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635
   ```
3. **Eval 已在运行**：PID 62345，GPU 1，日志 `/root/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log`，输出到 `eval_results/v4_vanilla_eval.json`

按当前速度（~2min/episode），预计 ~80 分钟完成全部 47 episodes。需要我稍后检查完成状态吗？

---
