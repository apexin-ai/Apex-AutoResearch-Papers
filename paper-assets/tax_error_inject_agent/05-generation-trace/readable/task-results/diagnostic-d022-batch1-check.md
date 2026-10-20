# diagnostic d022 batch1 check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_d022-batch1-check_20260515T091641_result.json`
- **Structured JSON:** [`aae5d49f81f7481df074.json`](../../sessions/aa/aae5d49f81f7481df074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 组实验全部完成。汇总如下：

## D022 Batch 1 训练状态

| 实验 | 状态 | train_loss | runtime | checkpoint | EXIT_CODE |
|------|------|-----------|---------|------------|-----------|
| v4-taxei-fixed-inject25-s0 | **完成** | 0.4258 | 56m 6s (3365s) | checkpoint-1635 ✅ | 0 |
| v4-taxei-fixed-inject25-s123 | **完成** | 0.4253 | 55m 56s (3356s) | checkpoint-1635 ✅ | 0 |
| v4-taxei-fixed-inject50-s0 | **完成** | 0.4342 | 52m 25s (3145s) | checkpoint-1635 ✅ | 0 |
| v4-taxei-fixed-inject50-s123 | **完成** | 0.4348 | 52m 55s (3175s) | checkpoint-1635 ✅ | 0 |

**关键指标：**
- 所有进程已退出（PID 不存在），GPU 全部空闲（0% utilization, 0 MiB）
- 4 组均训练到 1635/1635 steps（epoch 3.0），`EXIT_CODE=0`
- 每组都有 3 个 checkpoint（545, 1090, 1635），路径：`/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject{25,50}_s{0,123}/v0-20260515-153*/`
- inject50 比 inject25 训练略快（~52m vs ~56m），因为 inject50 的 token 序列更短（memory 17.99GB vs 18.76GB）
- 最终 token accuracy 均在 0.89-0.92 之间，loss 收敛正常

---
