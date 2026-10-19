# ops check multieval processes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-multieval-processes_20260528T030400_result.json`
- **Structured JSON:** [`480ba11fb8791adefffe.json`](../../sessions/48/480ba11fb8791adefffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### westd-35807 — 3/3 存活 ✅

| PID | 任务 | 运行时长 | GPU 占用 | 当前进度 |
|-----|------|---------|---------|---------|
| 960254 (→960263) | lora_s0_eseed42 | ~29 min | cuda:0, 8991 MiB | Task 3/?, Ep 10/50 |
| 960399 (→960408) | lora_s0_eseed123 | ~29 min | cuda:1, 8356 MiB | Task 2/?, 刚开始 |
| 960545 (→960554) | sdf_l01_s0_eseed42 | ~29 min | cuda:3, 8991 MiB | Task 3/?, Ep 10/50 |

三个都在正常跑 eval，日志持续输出。

### westd-45947 — 0/2 存活 ❌

| PID | 任务 | 状态 | 退出原因 |
|-----|------|------|---------|
| 594651 | sdf_l01_s0_eseed123 | 已退出 (code=1) | FileNotFoundError |
| 594793 | sdf_l01_s0_eseed256 | 已退出 (code=1) | FileNotFoundError |

**两个都在启动阶段就崩了**，相同错误：

```
FileNotFoundError: No such file or directory:
/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/30000/model.safetensors
```

checkpoint 路径 `/root/autodl-tmp/checkpoints/...` 在 westd-45947 上不存在。需要把该 checkpoint 同步到 45947，或修改 eval 配置指向正确路径后重跑这两个 seed。

---
