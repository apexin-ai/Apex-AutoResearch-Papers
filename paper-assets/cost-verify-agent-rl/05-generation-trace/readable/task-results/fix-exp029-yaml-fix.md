# fix exp029 yaml fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_yaml_fix_20260516T193649_result.json`
- **Structured JSON:** [`eb0ba7a05844a43c895a.json`](../../sessions/eb/eb0ba7a05844a43c895a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

| 项目 | 结果 |
|------|------|
| **进程状态** | PID 901155 已死（退出码2，hydra 参数解析错误） |
| **崩溃原因** | 日志显示 `ambiguous option: --config`，YAML 语法错误导致 hydra 无法正确解析配置 |
| **配置修复** | `optimizer_offload: True` 从 `ppo_mini_batch_size` 下的非法子键移至正确路径 `actor_rollout_ref.actor.fsdp_config.optimizer_offload` (第48-49行) |
| **YAML 验证** | `YAML_OK` |
| **GPU 状态** | 干净，无残留进程占用 |

可以重新启动 exp029。

---
