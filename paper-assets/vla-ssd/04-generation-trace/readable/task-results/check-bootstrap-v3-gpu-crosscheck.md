# check bootstrap v3 gpu crosscheck

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v3_gpu_crosscheck_20260523T072421_result.json`
- **Structured JSON:** [`f54a94e3071bc070aad9.json`](../../sessions/f5/f54a94e3071bc070aad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 没死，Director 误报。** 双卡都在正常工作。

## 状态汇报

| 卡 | 进程 | 当前任务 | 阶段 |
|---|---|---|---|
| cuda:0 (PID 725179) | 活跃，R 状态 | `openvla / goal / untrained` | bootstrap 阶段（1000 iter，100 workers 并行） |
| cuda:1 (PID 725751) | 活跃，42% GPU | `tracvla / goal / untrained` | extraction 阶段（1350/5000 samples） |

**已完成条件：2/20**
- `openvla_goal/trained.json` (15:03 完成)
- `tracvla_goal/trained.json` (15:13 完成)

**当前进行中：2 条 untrained 条件**
- cuda:0: openvla goal untrained — 已进入 bootstrap 计算，即将完成
- cuda:1: tracvla goal untrained — 还在提取特征 (1350/5000)

**nvidia-smi 显示 GPU 0 利用率 0% 是正常的** — bootstrap 阶段是 CPU-bound（kernel matrix + RidgeCV），GPU 仅在 extraction 阶段活跃。cuda:1 正在 extraction 所以显示 42% GPU 利用率。

无需重启，两卡均在正常推进。

---
