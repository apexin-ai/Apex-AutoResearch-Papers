# fix exp066 checkpoint

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp066-checkpoint_20260524T232943_result.json`
- **Structured JSON:** [`fa8b611700d30fcd475a.json`](../../sessions/fa/fa8b611700d30fcd475a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复成功！** Checkpoint 已开始保存：

```
latest.pt
checkpoint_10000.pt
```

## 诊断总结

**根因**：`--eval_every 999999` 导致整个 60K 训练在一次 `tools.simulate(steps=499999)` 调用中执行。`latest.pt` 和 `checkpoint_*.pt` 的保存代码在 simulate() **之后**，所以直到训练完全结束才会触发。

**修复**：杀掉旧进程（PID 488064），用 `--eval_every 5000` 重启（PID 490622）。这使外层循环每 5K 步返回一次，触发 checkpoint 保存。

**预期输出**：
- Checkpoint 间隔：每 5000 步（10K, 15K, 20K, ..., 60K）
- 总共 **11 个 checkpoint**（step 10000 到 60000）
- 另加每轮 eval 数据（之前被 999999 跳过了）

**代价**：
- 失去已跑的 32K 步（~4h），从头重跑需 ~8h
- Eval 开销极小（每 5K 步跑 10 ep walker_walk ≈ 30s）

**进程状态**：
- tmux session: `exp_066_timeseries_rssm_fidelity`
- PID: 490622, GPU 1, 2512 MiB
- 当前已到 step ~10000，正常推进中

---
