# ops verify a3 eval v10

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_a3_eval_v10_20260522T061020_result.json`
- **Structured JSON:** [`38c627a802c8e3051403.json`](../../sessions/38/38c627a802c8e3051403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认结果：

1. **tmux session**: `tmux ls` 被 read-only 模式拦截，但从 `ps aux` 看，只有 `a3_spatial` 训练 tmux session（PID 191740）。eval 进程（PID 342871）在 pts/5 上运行，未看到名为 `eval_a3` 的 tmux session——看起来是通过 ssh_execute 直接启动的。

2. **GPU 1 有 eval 进程**: 确认。PID 342871 占用 GPU-95684c29，显存 8617 MiB，CPU 365%，刚启动约 2 分钟（14:08）。

3. **Log 确认全部三项**:
   - A3 模型加载: 504 LoRA params loaded，norm stats loaded
   - SDF decoder 加载: `Loaded SDF decoder + EE extractor`
   - Safety level: II: `Setting up SafeLIBERO benchmark: safelibero_object (level II)`
   - 已开始 Task 0: *pick up the orange juice and place it in the basket*

**唯一注意点**: eval 没有跑在 tmux 里，而是直接 ssh_execute 启动。如果 SSH 连接断开，进程可能中断。如果 eval 预计时间较长，建议改用 tmux 启动。

---
