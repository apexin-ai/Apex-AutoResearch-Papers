# check server status 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-34685_20260527T033752_result.json`
- **Structured JSON:** [`e7a4cedf7c1272c863d2.json`](../../sessions/e7/e7a4cedf7c1272c863d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 训练状态报告

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 99% | 62.2 / 97.9 GB |
| cuda:1 | 91% | 62.2 / 97.9 GB |
| cuda:2 | 99% | 62.2 / 97.9 GB |
| cuda:3 | 99% | 63.0 / 97.9 GB |

### 训练进度（全部在跑）
| 实验 | PID | Step | 进度 | 运行时间 | ETA (剩余) |
|------|-----|------|------|----------|------------|
| detach_ln_v2_s1 | 681204 | 15,183/50,005 | 30% | 4h03m | ~8h55m |
| detach_ln_s4 | 677648 | 15,241/50,005 | 30% | 4h04m | ~8h57m |
| ablation_occ_detach_s4 | 735982 | 12,393/50,005 | 25% | 3h20m | ~9h39m |
| mvp_occ_s4 | 736344 | 12,386/50,005 | 25% | 3h20m | ~9h43m |

预计完成时间：
- detach_ln_v2_s1 / detach_ln_s4：~May 28 01:00 UTC（北京 09:00）
- ablation_occ_detach_s4 / mvp_occ_s4：~May 28 02:00 UTC（北京 10:00）

**全部在 DDL (May 28 12:00 UTC) 之前完成，余量充足。**

### 已有梯度分析 checkpoint（50K）
| 实验 | 状态 |
|------|------|
| vanilla_v2_s1 | ✓ 存在 |
| detach_ln_s3 | ✓ 存在 |
| mvp_occ_s0 | ✗ 不存在 |
| mvp_occ_s1 | ✗ 不存在 |
| ablation_occ_detach_s0 | ✗ 不存在 |

---
