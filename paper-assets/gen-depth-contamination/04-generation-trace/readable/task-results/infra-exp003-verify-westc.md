# infra exp003 verify westc

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp003_verify_westc_20260513T153846_result.json`
- **Structured JSON:** [`ce0a99300530dc8e426d.json`](../../sessions/ce/ce0a99300530dc8e426d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 状态验证结果

### 1. tmux session
- **名称**: `exp_003_decoding_ablation`
- **状态**: 运行中（PID 29458，May 12 14:43 启动）

### 2. 实际 PID
- 主进程 PID: **38871**（`run_pipeline.py`，100% CPU）
- shell 包裹 PID: 38868（`run_exp003_ablation.sh 3`）

### 3. GPU 利用率
- GPU 利用率: 45%
- 显存: 3921 MiB / 24564 MiB (16%)

### 4. 进度

| Config | 描述 | 状态 |
|--------|------|------|
| 1 | greedy | ✅ 完成（6 depths + 分析） |
| 2 | nucleus p=0.9, t=1.0 | ✅ 完成（6 depths + 分析） |
| 3 | nucleus p=0.95, t=0.7 | 🔄 **运行中** — depth 4: **304/313 (97%)**，depth 0-3 已完成 |
| 4 | nucleus p=0.95, t=1.2 | ⏳ 未开始 |

**当前位置**: Config 3/4，depth 5/6（depth_4 即将完成）

### 5. 预估剩余时间

每个 depth 约 313 batches × 6.25s ≈ 33 min：

- Config 3 剩余: depth_4 收尾 (~1 min) + depth_5 (~33 min) + 特征提取/分析 (~10 min) ≈ **~44 min**
- Config 4 全量: 6 depths + 分析 ≈ **~3.5 小时**
- **总剩余: ~4.25 小时**

**结论**: 实验正常运行，监控系统的 failed 标记是误报。

---
