# eval quick status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_quick-status-check_20260522T021523_result.json`
- **Structured JSON:** [`e29ede163b2dc3c5a096.json`](../../sessions/e2/e29ede163b2dc3c5a096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

### 结果文件
全部 6 个 50r 结果文件 **均未生成**，eval 全部还在跑。

### 4 个 GPU 上的 Eval 进程

| GPU | PID | 实验 | 当前进度 | 启动时间 |
|-----|-----|------|----------|----------|
| GPU 0 | 632709 | `ablation_occ_detach_s0` | T9: 50% (25/50) | 09:34 |
| GPU 1 | 615702 | `ablation_random_occ_s0` | T9: 68% (34/50) | 09:32 |
| GPU 2 | 760227 | `ablation_occ_detach_s1` | T4: 16% (8/50) | 10:00 |
| GPU 3 | 760427 | `ablation_random_occ_s1` | T4: 20% (10/50) | 10:00 |

每个进程占用 ~16.7GB 显存。

### 进度估算
- **s0 两组**（GPU 0/1）：已跑到 Task 9（共 10 个 task），约还需 15-25 分钟完成
- **s1 两组**（GPU 2/3）：才跑到 Task 4，约还需 40-50 分钟完成

---
