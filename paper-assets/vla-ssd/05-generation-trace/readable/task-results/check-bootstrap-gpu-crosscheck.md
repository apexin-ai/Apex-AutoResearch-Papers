# check bootstrap gpu crosscheck

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_gpu_crosscheck_20260523T041453_result.json`
- **Structured JSON:** [`856d53d7353ac5f51092.json`](../../sessions/85/856d53d7353ac5f51092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态正常，无需重启。**

| 卡 | 显存 | GPU利用率 | 状态 |
|---|---|---|---|
| GPU 0 | 691MiB | 0% | nora_goal untrained — **已进入 bootstrap 阶段**（CPU密集，100 workers 并行，GPU 空闲是正常的） |
| GPU 1 | 12641MiB | 26% | nora 相关任务 — 仍在 feature extraction（3700/5000 samples） |

**已完成 12 个 JSON**：
- openvla: goal/long/object/spatial 全部 trained+untrained ✓
- tracvla: goal trained+untrained ✓, spatial trained（缺 untrained）
- nora: goal trained（untrained 正在跑）

**GPU 利用率低的原因**：GPU 0 已完成特征提取，当前在做 1000 次 bootstrap 重采样——这是纯 CPU 计算（RidgeCV + kernel matrix），GPU 自然空闲。GPU 1 在做特征提取但该模型（nora）推理本身显存占用不高，利用率 26% 属正常范围。

两个 tmux session 和所有 python 进程均存活，进度正常推进。

---
