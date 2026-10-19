# ops emergency eval launch l1 20k

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_eval_launch_l1_20k_20260526T232735_result.json`
- **Structured JSON:** [`57e3fbc95b0b68327734.json`](../../sessions/57/57e3fbc95b0b68327734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
GPU 状态:
- cuda:0: PID 399885 (eval_safelibero 20K, 8356 MiB) — 正在运行
- cuda:1: PID 271266 (λ=0.1 s0 train, 27036 MiB, 100%) ✅
- cuda:2: PID 274407 (λ=0.1 s1 train, 27036 MiB, 100%) ✅
- cuda:3: PID 341425 (spatial LoRA ctrl, 27028 MiB, 100%) ✅

旧 PID 399880: 存活 — 是 eval 的 bash 包装进程，子进程 399885 是实际 python 进程

eval 启动结果: 已经在运行，无需重新启动
- PID: 399885 (wrapper: 399880)
- model_type: lora_baseline
- 验证 1 (ps): ✅ 运行 08:11
- 验证 2 (nvidia-smi): ✅ cuda:0 占用 8356 MiB
- 验证 3 (log): ✅ Task 0 已完成 40/50 episodes (ep10=success, ep20/30/40=fail)
```

Reviewer 判断有误 — eval 实际已在运行。之前的混淆是因为 PID 399880 是 bash 包装进程，实际 python 进程是子进程 399885。Registry 已更新。

---
