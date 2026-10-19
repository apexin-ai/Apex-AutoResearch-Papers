# monitor m1 progress and z check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m1_progress_and_z_check_20260513T012551_result.json`
- **Structured JSON:** [`45d8da48c737eaf586b1.json`](../../sessions/45/45d8da48c737eaf586b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### M1 进程
- **状态**: RUNNING (PID 577864)
- **运行时长**: 4h38m
- **当前活跃 repos**: mahmoud/boltons (450/737), cantools/cantools (350/1440), pygments/pygments (450/1430), oauthlib/oauthlib (700/940), pyupio/safety (250/759), Cog-Creators/Red-DiscordBot (450/460), joke2k/faker (150/360), jaraco/inflect (100/133), marshmallow-code/webargs, keleshev/schema

### 进度
| 指标 | 值 |
|------|-----|
| 已产出 JSON | 5,353 |
| 已跳过 (skip_log) | 660 |
| 已处理合计 | ~6,013 / 59,136 (**10.2%**) |
| 已启动 repos | 24 / 222 |
| M1 目录大小 | 2.1G |

### 磁盘
| 总量 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| 169G | 153G | **17G** | **91%** |

按当前速率（~5.3K instances / 4.6h），跑完 59K instances 预计还需 **~46 小时**。M1 目录增长到约 21G，磁盘可能不够（仅剩 17G）。需要关注磁盘。

### Z% 统计（基于已有 5,353 instances）
| 指标 | 值 |
|------|-----|
| 有 call_graph 的 instance | 5,128 / 5,353 (95.8%) |
| 无 call_graph | 225 (4.2%) |
| **Z%（有 CG 的 instance 中）** | **3,795 / 5,128 = 74.0%** |
| Z%（全部 instance 中） | 3,795 / 5,353 = 70.9% |

Z% 很高——约 74% 的 instance 通过 call graph 关联到了 gold patch 之外的文件，说明跨文件依赖在数据集中非常普遍。

---
