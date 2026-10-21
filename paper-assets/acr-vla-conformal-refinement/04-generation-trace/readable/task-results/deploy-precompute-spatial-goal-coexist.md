# deploy precompute spatial goal coexist

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_precompute-spatial-goal-coexist_20260522T160922_result.json`
- **Structured JSON:** [`6796559e61d9a7c5b07b.json`](../../sessions/67/6796559e61d9a7c5b07b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，无 OOM。

**结果汇总：**

| 项目 | tmux session | GPU | 显存占用 | 状态 |
|------|-------------|-----|---------|------|
| Spatial | `precompute-spatial-fixed` | cuda:0 | 5541 MiB / 24564 MiB | 已开始处理 task 0 |
| Goal | `precompute-goal-fixed` | cuda:2 | 7340 MiB / 24564 MiB | 加载 env 中 |

- cuda:0 与 eval 共存：5.5GB + eval 无冲突
- cuda:2 与 eval 共存：7.3GB + eval 无冲突
- cuda:1、cuda:3-5 未受影响
- 预计每个 ~33min 完成

---
