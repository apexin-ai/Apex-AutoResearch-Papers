# fix kill duplicates clean cache

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-duplicates-clean-cache_20260521T155430_result.json`
- **Structured JSON:** [`b5ec344f5c38db19f861.json`](../../sessions/b5/b5ec344f5c38db19f861.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证通过。

---

## 汇总

### 1. 进程清理

| Shard | 保留 | Kill | 原因 |
|-------|------|------|------|
| **s1** | bjb1-32546 PID 178365 (s1-r2, 2600) | bjb1-18228 PID 773431 (old s1, 错位) | 唯一有效版本 |
| **s2** | bjb1-32546 PID 178514 (s2-r2, 2900) | bjb1-18228 PID 773432 (old s2, 错位) | 唯一有效版本 |
| **s3** | bjb1-32546 PID 178661 (s3-r2, 2900) | bjb1-18228 PID 773433 (old s3, 错位) | 唯一有效版本 |
| **s4** | bjb1-32546 PID 178940 (s4-r2, 2700) | bjb1-18228 PID 773434 (old s4, 错位) | 唯一有效版本 |
| **s5** | bjb1-32546 PID 175531 (s5-fix, **3300**) | bjb1-32546 PID 179293 (s5-r2, 3100) | fix 快 200 |
| **s6** | bjb1-32546 PID 182292 (s6-r2, cuda:5, **3200**) | bjb1-32546 PID 175680 (s6-fix, 3200) | 约束：保留 cuda:5 r2 |
| **s7** | bjb1-32546 PID 175827 (s7-fix, **3300**) | bjb1-18228 PID 783367 (s7-r2, 2900) | fix 快 400 |
| **s8** | bjb1-32546 PID 176106 (s8-fix, **3400**) | bjb1-18228 PID 783512 (s8-r2, 2900) | fix 快 500 |
| **s9** | bjb1-32546 PID 176451 (s9-fix, **3300**) | bjb1-18228 PID 783660 (s9-r2, 2900) | fix 快 400 |

### 2. Cache 清理

删除 8 个混合粒度文件（`/root/autodl-tmp/crm_cache_pi05/object/`）：
- **s5** (5 个 500-sample): `partial_s5_{400_900, 900_1400, 1400_1900, 1900_2400, 2400_2900}.pt`
- **s6** (3 个 500-sample): `partial_s6_{1700_2200, 2200_2700, 2700_3200}.pt`

保留：s5 34 个 100-sample 文件 (0-3400)，s6 32 个 100-sample 文件 (0-3200)

### 3. 验证结果

| 服务器 | GPU 进程数 | 显存分布 | 状态 |
|--------|-----------|---------|------|
| **bjb1-32546** | 9 进程/6 GPU | cuda:0/2/3 = 19.7G (双进程), cuda:1/4/5 = 9.9G (单进程) | 9 shard 运行中 |
| **bjb1-18228** | 1 进程/4 GPU | cuda:3 = 9.9G (spatial shard 6), cuda:0-2 = **空闲** | 仅 spatial s6 |
| **bjb2-40593** | 1 进程/1 GPU | 9.8G | shard 0 运行中 |

---
