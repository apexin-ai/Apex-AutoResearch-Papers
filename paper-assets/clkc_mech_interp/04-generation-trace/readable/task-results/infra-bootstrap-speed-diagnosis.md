# infra bootstrap speed diagnosis

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bootstrap-speed-diagnosis_20260522T080912_result.json`
- **Structured JSON:** [`a7b6555664f0b5a7ca23.json`](../../sessions/a7/a7b6555664f0b5a7ca23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇报如下：

## 诊断结果

### 当前进度（运行 ~76 分钟）

| | Qwen | Llama |
|---|---|---|
| 当前方向 | EN→EN（第1/4个方向） | EN→EN（第1/4个方向） |
| 已完成 | ~748/8000 总迭代 (9.4%) | ~507/8000 总迭代 (6.3%) |
| 每轮耗时 | ~6.1s (36层 LR) | ~9.0s (32层 LR) |
| CPU 占用 | 549% (~5.5核) | 546% (~5.5核) |
| **预估剩余** | **~12.3 小时** | **~18.7 小时** |

### 数据维度
- Qwen: train=798, test=168, 36 layers, dim=4096
- Llama: train=1096, test=272, 32 layers, dim=4096

### 瓶颈原因

1. **总计算量巨大**: 4方向 × 2000 seeds × 36层 = **288,000 次 LR fit**（Qwen），256,000 次（Llama）
2. **完全串行**: bootstrap seeds 循环和 layers 循环都是顺序执行，**零并行**
3. **线程严重不足**: `OMP_NUM_THREADS=4, MKL_NUM_THREADS=4`，服务器有 **208 核**，仅用 ~11 核（两进程合计）
4. **全层扫描**: 每轮跑全部 36/32 层，peak 集中在 L13-L23 附近

### 优化建议

**方案：kill 后用优化脚本重跑**（省 15+ 小时）

| 优化措施 | 预期加速 | 说明 |
|----------|---------|------|
| `joblib.Parallel(n_jobs=32)` 并行化 seed 循环 | ~20-30x | 每个 seed 完全独立 |
| `OMP_NUM_THREADS=8` | ~1.5x | lbfgs 内部矩阵运算并行 |
| 只跑 peak±5 层 (11层 vs 36层) | ~3x | 如果只需要 peak 统计量 |

保守估计：仅加 joblib n_jobs=32 → Qwen 从 12.3h 降到 **~25 分钟**，Llama ~35 分钟。

是否要 kill 现有进程并写优化版脚本重跑？

---
