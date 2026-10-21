# diag eval variance check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_variance_check_20260523T195812_result.json`
- **Structured JSON:** [`0313cb182891b3b461b0.json`](../../sessions/03/0313cb182891b3b461b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**结论：eval 正常运行中，无需干预。**

### GPU 状态
- GPU 0: 56461/97887 MiB 已用（58%），利用率瞬时 0%（采样间隙，正常）

### 进程状态
| 角色 | PID | 启动时间 | 状态 |
|------|-----|---------|------|
| 总调度 `run_eval_variance.sh` | 46190 | 02:40 | 运行中 |
| 当前 eval `train.py evalvar-seed7hk-s0` | 57842 | 03:49 | 运行中，CPU 4.5% |
| `ray::TaskRunner.run` | 59882 | 03:50 | 运行中，CPU 78.2% |
| `ray::WorkerDict.generate` | 60058 | 03:50 | 运行中，CPU 34.7% |
| Ray IDLE workers | 多个 | 03:50 | 待命 |

### 进度（summary.log）
- seed300 s0 — 完成
- seed300 s1 — 完成
- seed300 s2 — 完成（耗时 23min）
- **seed7hk s0 — 03:49:50 启动，当前正在运行**（第 4/9 轮）
- seed7hk s1, s2, 第三个 checkpoint 的 3 轮 — 待执行

### 其他
- PID 42499（h-sweep 残留）已不存在
- 日志最后更新：03:53，显示 wandb run `zcqqnd4c` 已初始化，WorkerDict 正在加载模型权重进入推理阶段
- 每轮约 23 分钟，剩余 5 轮预计约 2 小时完成

---
