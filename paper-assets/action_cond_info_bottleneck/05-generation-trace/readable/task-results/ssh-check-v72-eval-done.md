# ssh check v72 eval done

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_v72_eval_done_20260517T224555_result.json`
- **Structured JSON:** [`257f4c5d3f3092ee07cd.json`](../../sessions/25/257f4c5d3f3092ee07cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 进程状态
两个 eval 均**正常完成**（日志末尾 "End of eval"，进程已退出）。

### 2. libero_10 结果

| | α=0.0 | α=1.0 |
|---|---|---|
| **libero_10 pc_success** | **41.4%** | **44.4%** |

### 3. 完整 4-suite 结果

| Suite | α=0.0 | α=1.0 |
|---|---|---|
| libero_spatial | 59.4 | 61.0 |
| libero_object | 65.6 | 66.2 |
| libero_goal | 78.6 | 78.0 |
| libero_10 | 41.4 | 44.4 |
| **4-suite AVG** | **61.25%** | **62.40%** |

### 4. GPU 状态
两块 GPU（RTX PRO 6000, 98GB each）均空闲，0MiB 占用，可立即启动 v7.3。

---
