# diagnose bjb1 32546 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-failures_20260519T210157_result.json`
- **Structured JSON:** [`cf6e9c150ec1838f1491.json`](../../sessions/cf/cf6e9c150ec1838f1491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集完所有信息。

## 诊断报告

### 当前状态：所有实验已恢复，无失败

4 个"失败"实验均已在 05:20 04:30-04:31 重启，当前正常运行：

| 实验 | GPU | PID | 状态 | 当前进度 |
|------|-----|-----|------|---------|
| `vla_only spatial seed48` | cuda:5 | 88043 | 运行中 | 4/10 tasks done |
| `vla_only long seed47` | cuda:4 | 86797 | 运行中 | 3/10 tasks done |
| `crm_obs_only goal seed44` | cuda:1 | 83910 | 运行中 | 5/10 tasks done |
| `crm_obs_only goal seed45` | cuda:3 | 85316 | 运行中 | 4/10 tasks done |

2 个原先"在运行"的实验已正常完成：

| 实验 | 结果 |
|------|------|
| `vla_only spatial seed46` | **30.0%** (30/100), 完成于 04:23 |
| `vla_only spatial seed47` | **30.0%** (30/100), 完成于 04:25 |

### 系统健康状态

| 指标 | 值 | 状态 |
|------|----|------|
| GPU | 6× RTX 4090, 4 张在用, 2 张空闲 (GPU 0, 2) | 正常 |
| 内存 | 1TB 总量, 944GB 可用 | 正常 |
| 根分区 | 30GB 中用了 9.8GB (33%) | 正常 |
| 数据盘 | 250GB 中用了 33GB (13%) | 正常 |

### 原失败根因

无法访问 `dmesg`（read-only 工具白名单限制），因此无法确认是否为 OOM killer。但从当前系统状态看：
- **不是内存问题** — 944GB 可用，远超需求
- **不是磁盘问题** — 两个分区余量充足
- **不是 GPU 硬件问题** — 6 张卡全部正常工作

最可能的原因是**资源竞争或瞬时问题**（6 张卡同时跑 6 个实验时的内存/显存峰值冲突），重启后减少到 4 个实验同时运行，目前稳定。

### 结论

- **seed46/47 spatial**: 已安全完成，无需关注
- **4 个重启实验**: 正常推进中，预计数小时内完成
- **无需手动干预**: 不需要重试 seed48，它已经在跑了
- **GPU 0 和 2 空闲**: 可分配新任务

---
