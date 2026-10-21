# deploy smolvla long reseed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-long-reseed_20260522T141707_result.json`
- **Structured JSON:** [`8d04cce15981bcd023fa.json`](../../sessions/8d/8d04cce15981bcd023fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部正常启动，正在加载 LIBERO long 环境。

**提交确认：**

| Seed | GPU | tmux session | PID | log |
|------|-----|-------------|-----|-----|
| 0 | cuda:0 | eval-vla-only-long-seed0 | 232609 | eval-vla-only-long-seed0.log |
| 1 | cuda:1 | eval-vla-only-long-seed1 | 232884 | eval-vla-only-long-seed1.log |
| 2 | cuda:2 | eval-vla-only-long-seed2 | 233564 | eval-vla-only-long-seed2.log |

**配置：** `--mode vla_only --benchmark long --n_rollouts 10`，`max_steps` 自动设为 520（long suite 官方值）。

**预计完成时间：** 参考之前 seed49/50/51 的运行时间，每个 eval 跑 10 tasks × 10 rollouts × 520 steps，约 2-4 小时。

---
