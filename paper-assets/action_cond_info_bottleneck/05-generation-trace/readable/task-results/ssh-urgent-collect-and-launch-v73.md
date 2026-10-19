# ssh urgent collect and launch v73

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-collect-and-launch-v73_20260517T183729_result.json`
- **Structured JSON:** [`43161d5133b57e8c70d0.json`](../../sessions/43/43161d5133b57e8c70d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练脚本都存在。现在的情况：

## 当前状态

### v7.2 Eval 已有结果（2/4 suites 完成）

| Suite | α=0.0 | α=1.0 |
|-------|-------|-------|
| libero_spatial | 59.4% | 61.0% |
| libero_object | 65.6% | 66.2% |
| libero_goal | **进行中** (α=0.0 在 task 8/10 ep38/50, 97.4% SR) | **进行中** |
| libero_10 | 未开始 | 未开始 |

### 训练启动：**被阻塞**

两个 eval 进程（PID 40598 / 44022）仍占用 GPU 0 和 GPU 1。按 C004 约束不能在占用的 GPU 上启动训练。

**估算剩余时间**：
- α=0.0 goal 还剩约 15 分钟完成，然后 libero_10 大约需要 2 小时
- α=1.0 进度稍慢，总计可能还需 2.5-3 小时

**两个选择**：
1. **等 eval 全部跑完** (~2.5-3h)，然后启动训练
2. **Kill eval 进程，立即启动训练**，goal/libero_10 的结果丢失（spatial 和 object 的结果已保存）

你要哪个方案？

---
