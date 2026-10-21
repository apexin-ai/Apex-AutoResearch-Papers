# diagnose eval random prune k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_random_prune_k05_20260517T091043_result.json`
- **Structured JSON:** [`696800b098777105d866.json`](../../sessions/69/696800b098777105d866.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**两个实验都没有失败（没有 crash）。它们正常运行完毕并产出了结果文件，但成功率为 0%。**

监控系统报告 "process dead" 是误判，实际情况是：

### 实验 1: eval_random_prune_k05
- **状态**: 正常完成，结果已保存到 `eval_results/eval_random_prune_k05_object.json`
- **结果**: Overall SR = 0.0% (0/500), 所有 10 个 task 全部 0%
- **模式**: `random_prune`
- **日志位置**: `eval_results/eval_random_prune_k05.log`
- **运行时间**: 16:09 ~ 16:49（约 40 分钟）

### 实验 2: eval_stage1only_k09
- **状态**: 正常完成，结果已保存到 `eval_results/eval_stage1only_k09_object.json`
- **结果**: Overall SR = 0.0% (0/500), 所有 10 个 task 全部 0%
- **模式**: `acis_prune`
- **日志位置**: `logs/eval_stage1only_k09.log`（不在 `eval_results/` 下）
- **运行时间**: 与实验 1 几乎同时段

### 根因分析

没有 traceback、OOM、CUDA error。进程正常退出。监控系统的 "process dead with no sentinel/W&B" 判定是因为这两个 eval 脚本没有集成 W&B logging 也没有写 sentinel 文件，监控无法确认进程状态而误判为失败。

### 真正的问题

两个实验虽然没有 crash，但 **0% 成功率** 表明模型推理有实质性问题：
- 所有 episode 都跑满 280 步后 FAIL，说明模型输出的 action 没有完成任何 task
- `random_prune` 和 `acis_prune` 模式下 keep_ratio 过于激进（k=0.5 和 k=0.9），pruning 后模型能力完全丧失
- 或者 stage1_done checkpoint 本身在 pruning 模式下根本不工作（可能需要 stage2 fine-tune 后才有效）

### 修复建议

1. **监控误报**: 给 eval 脚本加 sentinel 文件输出（eval 结束后 `touch .sentinel_done`），或注册 W&B run
2. **0% SR 问题**:
   - 检查 `k=0.5` 的 random_prune 是否保留了太少的 token/layer（对比 baseline 的 SR）
   - 确认 stage1_done checkpoint 是否适合直接做 pruned inference，还是必须经过 stage2 fine-tune
   - 对比已有的 `eval_random_prune_object.json`（不带 k05 后缀的版本）看之前跑过的结果如何

---
