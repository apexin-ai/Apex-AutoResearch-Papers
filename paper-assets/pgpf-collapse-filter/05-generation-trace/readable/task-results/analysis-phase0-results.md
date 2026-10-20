# analysis phase0 results

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase0_results_20260513T062920_result.json`
- **Structured JSON:** [`335534483b2556a59383.json`](../../sessions/33/335534483b2556a59383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 PID 10520 仍然存活。实验还在训练中，还没有到分析阶段。

## Phase 0 实验状态报告

**实验 ID**: `phase0_ortho_v2`
**当前状态**: 仍在训练中（非 ANALYZING 完成状态）

### 关键发现

| 项目 | 结果 |
|------|------|
| 训练进度 | 最后日志记录到 step 50/750（日志缓冲未刷新，进程仍在运行） |
| PID 10520 | **存活**（/proc/10520 存在） |
| correlation_matrix.json | **不存在** — 训练未完成，尚未进入分析阶段 |
| scatter_plots.png / correlation_heatmap.png | **不存在** |
| checkpoint/ | 空目录 |
| 日志最后修改时间 | 14:30:19 CST（Python stdout 缓冲导致日志写入滞后） |

### 产出文件列表

```
/root/autodl-tmp/pgpf/outputs/phase0/
├── checkpoint/       (空)
└── run.log           (8534 bytes, 训练进度日志)
```

### 预估完成时间

- 训练速度：~1.5-2s/step
- 剩余约 700 步 × ~1.7s ≈ **20 分钟**（从日志停写时算起）
- 训练后还需要 generation + scoring + correlation 分析

### 结论

**无法判断 PASS/FAIL** — 实验尚未完成。注册表状态 `ANALYZING` 与实际不符，训练仍在进行中。建议 **15-20 分钟后重新检查**。

已使用 SSH 调用：8/10 次。未更新注册表（无结果可记录）。

---
