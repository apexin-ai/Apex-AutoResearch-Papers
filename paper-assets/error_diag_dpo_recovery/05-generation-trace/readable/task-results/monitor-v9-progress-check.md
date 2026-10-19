# monitor v9 progress check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9-progress-check_20260513T082104_result.json`
- **Structured JSON:** [`42cc5f03b7f139e793b0.json`](../../sessions/42/42cc5f03b7f139e793b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v9 ICL 数据收集进度报告

### 进程状态
| GPU | PID | 运行时间 | 状态 |
|-----|-----|---------|------|
| cuda0 | 884782 | 3m56s | 存活 |
| cuda1 | 885180 | 3m54s | 存活 |
| cuda4 | 885698 | 3m52s | 存活 |

3 个进程均正常，**刚启动约 4 分钟**（`etime` 格式是 mm:ss）。

### 完成进度
| GPU | 已完成 | 总量 | 成功 | SR |
|-----|--------|------|------|-----|
| cuda0 | 2/1107 | 0.2% | 2 | 100% |
| cuda1 | 4/1107 | 0.4% | 4 | 100% |
| cuda4 | 2/1107 | 0.2% | 2 | 100% |

**总计：8/3321 (0.2%)，SR 8/8 = 100%**（样本太少，SR 不具参考性）

### 按 task_type（全部成功）
- pick_clean_then_place: 4
- pick_cool_then_place: 2
- pick_and_place: 1
- pick_two_obj: 1
- look_at_obj: 1

### GPU 利用率
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 11% | 11573/24564 MiB |
| 1 | 0% | 11477/24564 MiB |
| 4 | 29% | 11593/24564 MiB |
| 2,3,5 | 空闲 | 0 MiB |

### 预估剩余时间
每 task 耗时差异大（首 task ~110s 含 warmup，后续 30-55s）。按 post-warmup 均速估算：
- **乐观**（~35s/task）：~10-11 小时
- **保守**（~60s/task）：~18-19 小时

现在样本太少，建议跑到 50+ tasks 后再看更准确的速度和 SR。

### 异常
无。进程正常运行，GPU 显存加载正常（~11.5GB/卡，符合 14B-AWQ 预期），SR 暂时 100% 但样本量不足以判断。

---
