# check verify 022 running

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify-022-running_20260517T074542_result.json`
- **Structured JSON:** [`d22385dd8a584227cb09.json`](../../sessions/d2/d22385dd8a584227cb09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### 1. 019a_v2 (PID 629444)
**仍在运行**，但实际已完成训练。进程还活着（bash wrapper），但 metrics.jsonl 最后记录到 step 202500（目标 200000 已达），最终 eval_return = **58.56**，train_return ≈ 79.0。进程可能在做最后的 checkpoint 保存或已进入 idle 状态。

### 2. exp_022 (PID 660840)
**已崩溃退出**（exit code 1），退出时间 `2026-05-17T07:44:06Z`。

**崩溃原因**：`torch.compile` 失败 —— `AssertionError: duplicate template name`，出在 `torch._inductor.kernel.flex_attention`。这是 PyTorch inductor 的已知 bug，发生在 `self._wm = torch.compile(self._wm)` 这行 (`dreamer.py:105`)。

exp_022 的启动命令里可能没有传 `--compile False`。metrics.jsonl 只写了 4 行（seed episodes），训练还没真正开始就挂了。

### 3. tmux sessions
只有 `exp_019a_v2_pickcube_baseline` 和 `exp_019b_pickcube_civo_trigger`，没有 exp_022 的 session。

### 4. GPU 使用
- **GPU 0**: PID 629449 (643 MiB) + PID 649577 (2849 MiB) — 分别是 019a_v2 子进程和 019b
- **GPU 1**: PID 629449 (4152 MiB) — 019a_v2 的 MuJoCo 渲染

exp_022 没有占用任何 GPU。

### 结论
- 019a_v2 已完成 200k steps，可以清理
- **exp_022 需要重新启动**，加上 `--compile False` 参数避免 torch.compile bug

---
