# monitor n500 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_n500_progress_check_20260515T013936_result.json`
- **Structured JSON:** [`550a7b5a807c64732b6a.json`](../../sessions/55/550a7b5a807c64732b6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 76% | 33.4/97.9 GB | 正常运行 |
| 1 | 79% | 33.9/97.9 GB | 正常运行 |
| 2 | 98% | 34.1/97.9 GB | 正常运行 |
| 3 | 78% | 34.7/97.9 GB | 正常运行 |

### s025 进度（当前运行中）

| Condition | GPU | 进度 | 开始时间 | 已耗时 | 预估剩余 | 预估完成 |
|-----------|-----|------|----------|--------|----------|----------|
| ds_imp_s025 | 0 | **318/500** | 06:55 | ~2h46m | ~95 min | ~11:16 |
| ds_rand_s025 | 1 | **364/500** | 06:31 | ~3h10m | ~71 min | ~10:52 |
| qw_imp_s025 | 2 | **476/500** | 06:28 | ~3h13m | ~10 min | ~09:51 |
| qw_rand_s025 | 3 | **457/500** | 06:37 | ~3h04m | ~17 min | ~09:58 |

Qwen 两个 condition 即将完成（~10-20 min），s030 将自动启动。DeepSeek 还需 ~1-1.5h。

### s015 + s020 数据完整性
8 个已完成 condition 全部 `problem_id` 计数一致（每文件 1500 条），日志均正常结束：

| Condition | 状态 |
|-----------|------|
| ds_imp_s015 | ✓ 完成 |
| ds_imp_s020 | ✓ 完成 |
| ds_rand_s015 | ✓ 完成 |
| ds_rand_s020 | ✓ 完成 |
| qw_imp_s015 | ✓ 完成 |
| qw_imp_s020 | ✓ 完成 |
| qw_rand_s015 | ✓ 完成 |
| qw_rand_s020 | ✓ 完成 |

### s030 状态
4 个 s030 目录均不存在，等 s025 对应 condition 完成后由脚本自动创建并启动。

### 无异常
4 张卡负载正常，无 GPU 空闲或进程挂起迹象。

---
