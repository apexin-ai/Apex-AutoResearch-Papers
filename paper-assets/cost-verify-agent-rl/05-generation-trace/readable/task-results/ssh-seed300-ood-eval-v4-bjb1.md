# ssh seed300 ood eval v4 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed300_ood_eval_v4_bjb1_20260522T203948_result.json`
- **Structured JSON:** [`fdd2a83e9fac5f85c913.json`](../../sessions/fd/fdd2a83e9fac5f85c913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**v4 eval 已在运行中**，无需重新启动。

### Runtime Config 验证（从 log config dump 确认）
| 参数 | 实际值 | 要求 | 状态 |
|------|--------|------|------|
| `enable_think` | `True` | `True` | ✓ |
| `enable_response_mask` (顶层) | `False` | `False` | ✓ |
| `enable_response_mask` (嵌套) | `False` | `False` | ✓ |
| `context_window_mode` | `full` | `full` | ✓ |
| `seed.val` | `321` | `321` | ✓ |
| `val_only` | `True` | `True` | ✓ |
| OOD tasks | `AlfworldSG_OOD` × 134 | 134 | ✓ |
| `val_kwargs.temperature` | `0.4` | `0.4` | ✓ |

### 运行状态
- **PID**: 456544（主进程），459788（TaskRunner）
- **启动时间**: 04:37 UTC (May 23)
- **Log**: `/root/autodl-tmp/logs/ood_eval_v4_seed300.log`（1732 行）
- **W&B run**: `wf27jcg8`（seed300-step5-ood-eval）
- **GPU 0**: 已分配（8133 MiB used），utilization 0%（刚完成模型加载/数据集加载阶段，尚未开始 rollout）
- **磁盘**: `/root/autodl-tmp` 119GB free（充足）

模型加载和 W&B 初始化已完成，正在进入 eval rollout 阶段。

---
