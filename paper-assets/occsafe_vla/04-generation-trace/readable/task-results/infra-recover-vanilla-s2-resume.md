# infra recover vanilla s2 resume

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_recover_vanilla_s2_resume_20260520T203937_result.json`
- **Structured JSON:** [`238189bbd6a58cc5ef52.json`](../../sessions/23/238189bbd6a58cc5ef52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

| 项目 | 状态 |
|------|------|
| **s0** (PID 100203) | 运行中，已 11h19m |
| **s1** (PID 97847) | 运行中，已 11h19m |
| **s2** (PID 225562) | 已从 35000_chkpt resume，~1.04 it/s |
| **35000_chkpt** | 完整（~15GB，含 config.json + 4 model shards + lora + action_head + proprio） |
| **40000_chkpt** | 已删除（不完整，缺 model safetensors） |
| **cleanup 进程** | 已 kill (PID 152257) |
| **新 monitor** | PID 226827，watching 100203/97847/225562 |
| **eval 参数** | 已修复 `--num_trials_per_task` → `--num_rollouts`，移除无效 `--gpu_id` |
| **预估 s2 完成** | 15005 steps / 1.04 it/s ≈ **4.0h**（约 08:45 UTC） |

注意：进度条显示 48/50005 但 `max_steps=50005` + `resume_step=35000`，实际只跑 15005 步。如果代码实现是从 0 重新计数到 50005 而非从 35000 到 50005，需要确认训练逻辑——建议等到 step ~5000 时检查 checkpoint 命名是否正确（应存为 40000_chkpt）。

---
