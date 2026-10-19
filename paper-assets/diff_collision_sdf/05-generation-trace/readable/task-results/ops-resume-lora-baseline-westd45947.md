# ops resume lora baseline westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume_lora_baseline_westd45947_20260525T043754_result.json`
- **Structured JSON:** [`94516a1b5a176522380b.json`](../../sessions/94/94516a1b5a176522380b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。

```
1. GPU 异常处理结果：GPU 0 自动恢复（启动训练后 100% util + 27089 MiB，之前的 0 MiB 是 stale state）。gpu-reset 不支持（Not Supported），但无需 reset。
2. Phase 2 LoRA 检查：有 Phase 1/2 区分，line 113 已用 >= （无 M033 问题）。resume 时 phase=1→在 step 16000 首次 on_step_start 正确触发 phase 2 解冻。
3. s0 resume：PID=2275, 从 step=16000 resume, 目标 step=30000, Phase 2 已在 step 16000 解冻 33.47M LoRA params
4. s1 resume：PID=2353, 从 step=16000 resume, 目标 step=30000, Phase 2 已在 step 16000 解冻 33.47M LoRA params
5. GPU 状态：GPU 0 = 27089 MiB / 100%, GPU 1 = 27089 MiB / 100%（两卡正常训练中）
6. 磁盘余量：根=12G avail (61% used), 数据盘=53G avail (79% used)
```

---
