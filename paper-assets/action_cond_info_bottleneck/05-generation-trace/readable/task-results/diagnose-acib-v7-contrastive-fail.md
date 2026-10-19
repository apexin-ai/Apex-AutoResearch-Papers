# diagnose acib v7 contrastive fail

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_acib_v7_contrastive_fail_20260516T134642_result.json`
- **Structured JSON:** [`0ebd4b8a5560635ae423.json`](../../sessions/0e/0ebd4b8a5560635ae423.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**关键发现：acib_v7_contrastive 当前正在运行，未失败。**

EXIT_CODE=129 来自之前的 run（PID 960110，磁盘满后那次）。当前已有新的 tmux session 在跑：

| 项目 | 状态 |
|------|------|
| **acib_v7_contrastive** | PID 21363, 运行中, 当前 step ~6400/20000 |
| **acib_v7_seed2** | PID 27427, 运行中, 当前 step ~200/20000 |

### 详细状态

**失败根因**：前一次 run 的 SIGHUP（信号 129）— 最可能是 SSH 断连或旧 tmux session 被关闭。当前实例从 20:45 重启，运行正常。

**Checkpoint**：`checkpoint-5000` 存活（1.3GB），位于 `/root/acib/outputs/acib_v7_contrastive/checkpoint-5000/checkpoint.pt`

**GPU**：
- GPU 0: RTX PRO 6000 Blackwell, 16GB/98GB used, 98% util → contrastive
- GPU 1: RTX PRO 6000 Blackwell, 16GB/98GB used, 98% util → seed2

**磁盘**：
- 根分区: 14G/30G used (46%) — 充足
- 数据盘: 75G/250G used (30%) — 充足

**seed2 注意**：有 4 个 DataLoader worker 子进程（PID 28132-28135），正常行为。

### 结论

两个实验都在正常训练中，无需干预。contrastive 预计还需 ~(20000-6400)/1.8/3600 ≈ 2.1 小时完成；seed2 预计 ~3 小时完成。

---
