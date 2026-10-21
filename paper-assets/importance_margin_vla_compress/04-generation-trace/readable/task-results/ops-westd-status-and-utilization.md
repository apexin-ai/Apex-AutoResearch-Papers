# ops westd status and utilization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_status_and_utilization_20260520T001155_result.json`
- **Structured JSON:** [`5d774e3a2920b1a42dc5.json`](../../sessions/5d/5d774e3a2920b1a42dc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器状态汇总：

---

## westd-41074 (4× RTX PRO 6000 96GB)

| GPU | 任务 | PID | VRAM | Util | 运行时间 | 进度 |
|-----|------|-----|------|------|---------|------|
| 0 | **C4-ext** VTC-only M=128 | 26118 | 30GB | 0%* | 5h38m | step 11800/100K, loss ~2.7, sps 0.6 |
| 1 | **C5v2** RoboFlamingo | 53406 | 48GB | 100% | 1h50m | step 8450, arm_loss 0.08, grip_loss 0.69 |
| 2 | 空闲 | - | 0 | - | - | 等 20K gate |
| 3 | 空闲 | - | 0 | - | - | 等 20K gate |

*GPU 0 util 0% 是采样瞬间，sps 0.6 说明正常跑

## westd-27271 (2× RTX PRO 6000 96GB)

| GPU | 任务 | PID | VRAM | 进度 |
|-----|------|-----|------|------|
| 0 | VTC+LoRA M=128 seed42 | 841334 | 32GB | 运行 5h34m |
| 1 | **新启动: OpenVLA M=32 VTC-only** | 855140 | 26GB | step 0, loss 17.0 (初始) |

## westd-27271:1 任务安排

**启动了 OpenVLA Smart Compress M=32 VTC-only 训练** (`openvla_smart_compress_m32.yaml`, seed42)

- 不依赖 20K gate — 即使 gate fail 也收集 M=32 数据点
- 属于 M-sweep 一环（M=32/64/96/128 对比），为论文 §4.3 提供数据
- 日志: `logs/train_openvla_sc_m32_seed42.log`
- 磁盘注意: 数据盘 245/250GB (98%)，checkpoint 保存可能有风险，需要后续监控

---
