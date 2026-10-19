# verify preparing gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_preparing-gpu-status_20260521T041722_result.json`
- **Structured JSON:** [`4b3b3de451fb61d0013c.json`](../../sessions/4b/4b3b3de451fb61d0013c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| exp_id | server | PID | status | SR | 备注 |
|--------|--------|-----|--------|----|------|
| eval-obs-only-object-norm003-seed76 | bjb1-32546 | 825126 | RUNNING | — | elapsed 44min, cuda:0 (4802MiB, 29%) |
| eval-obs-only-object-norm003-seed62-r3 | bjb1-32546 | 814262 | RUNNING | — | elapsed 1h01m, cuda:1 (4802MiB, 31%) |
| eval-obs-only-object-norm003-seed63-r3 | bjb1-32546 | 814859 | RUNNING | — | elapsed 1h01m, cuda:3 (4802MiB, 27%) |
| eval-obs-only-object-norm01-seed76 | bjb1-32546 | 815198 | RUNNING | — | elapsed 1h01m, cuda:4 (4802MiB, 29%) |
| eval-obs-only-object-norm01-seed77 | bjb1-32546 | 815988 | RUNNING | — | elapsed 1h01m, cuda:5 (4802MiB, 36%) |
| eval-obs-only-object-norm003-seed77 | bjb2-28827 | 979376 | RUNNING | — | elapsed 1h01m, cuda:1 (4801MiB, 19%) |
| eval-obs-only-object-norm003-seed78 | bjb2-28827 | 980035 | RUNNING | — | elapsed 1h01m, cuda:2 (4802MiB, 28%) |
| eval-obs-only-object-norm005-seed76 | bjb2-28827 | 981080 | RUNNING | — | elapsed 1h01m, cuda:3 (4801MiB, 25%) |
| eval-obs-only-object-norm005-seed77 | bjb2-28827 | 982671 | RUNNING | — | elapsed 1h01m, cuda:4 (4801MiB, 26%) |
| eval-pi05-baseline-object-seed42-r2 | bjb2-40593 | 811001 | **已完成** | **0.0%** | 10 tasks × 20 rollouts 全部失败 |

**汇总**：9 个 PREPARING 实验全部正常运行中（~1 小时），GPU 显存和利用率正常。π0.5 baseline r2 已完成但 SR=0.0%（与 r1 一致，该 baseline 在 object benchmark 上确实是 0%）。

---
