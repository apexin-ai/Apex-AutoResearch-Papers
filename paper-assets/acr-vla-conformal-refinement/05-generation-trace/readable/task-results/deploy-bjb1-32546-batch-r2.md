# deploy bjb1 32546 batch r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-batch-r2_20260528T061749_result.json`
- **Structured JSON:** [`937f880a7c23e2581cf7.json`](../../sessions/93/937f880a7c23e2581cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**6 张 GPU 全部被占用，无法部署。** 违反约束 C001（显存 < 500 MiB 才可提交）。

当前状态：

| GPU | 显存占用 | GPU利用率 |
|-----|---------|----------|
| cuda:0 | 10,353 / 24,564 MiB | 24% |
| cuda:1 | 10,806 / 24,564 MiB | 59% |
| cuda:2 | 10,835 / 24,564 MiB | 51% |
| cuda:3 | 2,904 / 24,564 MiB | 36% |
| cuda:4 | 3,080 / 24,564 MiB | 36% |
| cuda:5 | 3,547 / 24,564 MiB | 53% |

6 个残留 tmux sessions：
- `eval-ksweep-k20-obs-obj-s43`
- `eval-ksweep-k20-obs-object-s44`
- `eval-random-selection-object-seed43-v2`
- `pi05-crm-always-on-goal-s43`
- `pi05-crm-always-on-goal-s44`
- `pi05-crm-always-on-object-s44`

需要你确认：是否 kill 这 6 个 tmux session 腾出 GPU？还是等它们跑完？

---
