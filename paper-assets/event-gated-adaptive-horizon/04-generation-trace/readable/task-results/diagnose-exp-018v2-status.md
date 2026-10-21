# diagnose exp 018v2 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_018v2_status_20260516T135355_result.json`
- **Structured JSON:** [`2dffd8eda7251790c35c.json`](../../sessions/2d/2dffd8eda7251790c35c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**PID 588656 已死。** 进程在启动阶段就崩溃了，从未进入训练循环。

**死因：`torch.compile()` 的 PyTorch Inductor bug**

```
dreamer.py:50  →  self._wm = torch.compile(self._wm)
  → torch._inductor/kernel/flex_attention.py:786
  → AssertionError: duplicate template name
```

这是 PyTorch Inductor 的已知 bug（常见于 2.6.x 某些版本），在编译 world model 时 Triton 模板名冲突导致 crash。

**训练进度：step 0**。metrics.jsonl 只有 4 条 seed episode 记录（随机策略收集的初始数据），之后 agent 初始化时调用 `torch.compile` 就挂了。logdir 也只有初始化阶段的文件。

**修复方案**：在 `dreamer.py:50` 禁用 `torch.compile`，改为直接使用 `self._wm`（不编译），或者加条件判断跳过 compile。这样可以立即重新提交实验。

---
