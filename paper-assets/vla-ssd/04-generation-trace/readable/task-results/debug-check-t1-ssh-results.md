# debug check t1 ssh results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_t1_ssh_results_20260518T045322_result.json`
- **Structured JSON:** [`d17acec34709093bf778.json`](../../sessions/d1/d17acec34709093bf778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程状态正常（State: R, running），276 线程，9 GB 内存。日志最后更新于 12:49，正在处理 seed 6/20。

## 汇总

### SSH & GPU
- 连接正常
- GPU 0: 0% util, 0 MiB | GPU 1: 0% util, 691 MiB（两卡空闲）

### Random-Subset Ablation 进度
- **状态**: 运行中，Phase 2 完成 6/20 random seeds
- **Phase 1**: 10 tasks × 50 demos = 63,728 frames cached (23 min, 46.2 fps)
- **结果文件**: 尚未生成（脚本在全部完成后才写 JSON）

### 已有中间结果（关键）

| Condition | R² | R² Increase |
|-----------|-----|-------------|
| Baseline (no ablation) | 0.5169 | — |
| **Dominant-24** | 0.5592 | **+0.0423** |
| Random seed 0 | 0.5896 | +0.0727 |
| Random seed 1 | 0.5845 | +0.0676 |
| Random seed 2 | 0.5811 | +0.0642 |
| Random seed 3 | 0.5893 | +0.0724 |
| Random seed 4 | 0.6040 | +0.0871 |
| Random seed 5 | 0.6021 | +0.0852 |

### ⚠️ 关键负向结果信号

1. **Dominant-24 increase = +0.0423**，不是预期的 +0.059
2. **所有 6 个 random-24 subsets 的 increase 都高于 dominant-24**
   - Random-24 均值: **+0.0749** (SD ≈ 0.009)
   - Dominant-24 只有 +0.0423，**低于所有 random samples**
3. 如果这个趋势持续到 20 个 seeds 完成，dominant-24 将处于分布的最底部（percentile ≈ 0%），z-score 为负
4. 这意味着：**ablating dominant heads 对 action prediction probe 的提升反而不如 random heads**——dominant heads 可能并非 instruction-action 耦合的关键通道

剩余 14 个 seeds 预计还需约 15-20 分钟完成。

---
