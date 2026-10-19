# ssh verify connector only eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_connector_only_eval_20260518T010342_result.json`
- **Structured JSON:** [`1d9aa3a26d444aedfea7.json`](../../sessions/1d/1d9aa3a26d444aedfea7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

| 检查项 | 状态 |
|--------|------|
| GPU 1 显存占用 | **6001MiB**，有进程 (PID 759167) |
| eval 进程存活 | **存活** — `eval_acib.py` 运行中 |
| 日志状态 | **正常** — rollout 进行中，~27% (77/280 steps) |

注意：进程实际跑在 GPU 1（nvidia-smi 显示 PID 759167 在 GPU 1），但命令行参数写的是 `--gpu 0`。这可能是因为 `CUDA_VISIBLE_DEVICES=1` 被设置，使得逻辑 GPU 0 映射到物理 GPU 1。

当前 `running_success_rate=0.0%` — 这是 connector-only baseline 的 eval，前期 success rate 低属正常，需等全部 episode 完成后看最终结果。

GPU 0 上另有活跃训练进程 (PID 745668, 15276MiB)，符合预期。

---
