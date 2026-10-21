# ops deploy cuda4 obs only norm02

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-cuda4-obs-only-norm02_20260515T051835_result.json`
- **Structured JSON:** [`a1a7e69bfacab064ed4c.json`](../../sessions/a1/a1a7e69bfacab064ed4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**执行摘要：**

| 步骤 | 状态 |
|------|------|
| 杀掉 pid 39397 + 孤儿子进程 39406 | ✓ |
| checkpoint `crm_best.pt` 存在 (1.3MB) | ✓ |
| 注册 `eval-acr-object-obs-only-norm02` | ✓ RUNNING |
| 提交到 bjb1-32546 cuda:4 | ✓ pid 44270, tmux `eval-acr-object-obs-only-norm02` |
| `max_correction_norm = 0.2` 确认覆盖 | ✓ 日志已确认 |
| GPU 4 内存 7449 MiB | ✓ 正常 |

注意：`/root/autodl-tmp/crm_cache_v4/object/` 目录不存在，但运行中的 object 实验都没用 cache 路径参数，不影响执行。

---
