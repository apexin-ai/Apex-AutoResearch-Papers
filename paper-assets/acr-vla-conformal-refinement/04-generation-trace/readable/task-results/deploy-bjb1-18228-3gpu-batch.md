# deploy bjb1 18228 3gpu batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-3gpu-batch_20260520T193957_result.json`
- **Structured JSON:** [`af919288d49c800e17f2.json`](../../sessions/af/af919288d49c800e17f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**GPU 占用确认：**
| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| 0 | eval-obs-only-object-norm005-seed45 | 524561 | 5730 MiB |
| 1 | eval-obs-only-object-norm01-seed48 (已有) | 507385 | ~1 MiB* |
| 2 | eval-obs-only-object-norm01-seed50 | 526048 | 5730 MiB |
| 3 | eval-obs-only-object-norm003-seed46 | 527531 | 5730 MiB |

*GPU1 的 507385 在验证时显示 1 MiB，可能已完成或处于空闲阶段。

3个 cron 已注册（120s 轮询）。Registry 中 norm005-seed45 和 norm003-seed46 卡在 DEPLOYED 状态（状态机不允许 DEPLOYED→RUNNING），norm01-seed50 已正常设为 RUNNING。

---
