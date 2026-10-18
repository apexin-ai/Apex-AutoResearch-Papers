# urgent westd 41074 collect and redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd-41074-collect-and-redeploy_20260525T224015_result.json`
- **Structured JSON:** [`0ab0ec801da123619cef.json`](../../sessions/0a/0ab0ec801da123619cef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**zeromask_random 结果收集** ✓
- `eval_openvla_zeromask_random_k09_object_seed42`: **SR = 71.8%**（10 tasks, 500 episodes, 246 min）
- 对比 hard-prune random k=0.9 = 62.8% → zeromask 71.8% >> hard-prune 62.8%
- 结论：zero_mask（保留位置，置零值）显著优于 hard-prune（直接删除），说明**位置扰动是主要性能损失来源**，不只是信息丢失

**GPU 重部署** ✓
- GPU2: `eval_openvla_attn_k085_long_seed42` 已启动（PID 199285, 16GB loaded）
- GPU3: zeromask_l2norm 仍在运行（PID 5519），无需操作

**当前 westd-41074 状态**:
| GPU | 占用 | 实验 |
|-----|------|------|
| 0 | 16GB, 78% | 其他实验 |
| 1 | 27GB, 90% | 其他实验 |
| 2 | 16GB, 69% | attn_k085_long (新部署) |
| 3 | 16GB, 68% | zeromask_l2norm (进行中) |

---
