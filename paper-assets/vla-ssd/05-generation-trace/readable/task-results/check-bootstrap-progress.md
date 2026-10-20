# check bootstrap progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_progress_20260522T152845_result.json`
- **Structured JSON:** [`ca952a4d244397473e07.json`](../../sessions/ca/ca952a4d244397473e07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Clustered Bootstrap 实验进度报告

### GPU 状态

| GPU | 利用率 | 显存 | 当前任务 |
|-----|--------|------|----------|
| 0 | 0% | 2.1/95.6 GB | OpenVLA goal trained — **bootstrap 阶段 (CPU-bound)** |
| 1 | 24% | 8.7/95.6 GB | TracVLA goal trained — **特征提取阶段** |

### GPU 0 (`bootstrap_cuda0`) — OpenVLA + NORA

**脚本计划**: OpenVLA 3 suites × 2 conditions + NORA 3 suites × 2 conditions = **12 runs**

**当前进度**: Run 1/12 (openvla goal trained)
- 特征提取完成 (5000 samples, 219s)
- RidgeCV 拟合完成
- Kernel 矩阵预计算完成
- **10000 次 bootstrap 迭代进行中** (自 22:55:41 开始，CPU 累计时间 1303 分钟)

### GPU 1 (`bootstrap_cuda1`) — TracVLA

**脚本计划**: TracVLA 3 suites × 2 conditions + long × 2 conditions = **8 runs** (有 skip 已存在结果的逻辑)

**当前进度**: Run 1/8 (tracvla goal trained)
- 特征提取中: Task 2/10, 1300/5000 samples (~26%)
- 启动于 23:28:10, CPU 累计 14 分钟

### 已完成结果文件

```
results/clustered_bootstrap/
├── openvla_goal/trained.json    (22:40, 可能来自之前的运行)
├── openvla_long/                (空)
├── tracvla_long/                (空)
```

仅 **1 个** 结果文件完成。

### 预估

Bootstrap 阶段是瓶颈——openvla 第一个 run 的 bootstrap 已用 1303 分钟 CPU 时间，仍未完成。按此速度：
- **GPU 0**: 12 runs，当前 run 1 还未完成，预计需要很长时间（天级别）
- **GPU 1**: 8 runs，当前 run 1 仍在提取阶段

10000 次 bootstrap 迭代耗时极长。如果每个 run 的 bootstrap 阶段都需要 20+ 小时，整个实验可能需要 **数天** 才能完成。建议考虑是否需要减少 `n_bootstrap` 或优化 bootstrap 实现。

---
