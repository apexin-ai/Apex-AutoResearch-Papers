# monitor training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260526T123651_result.json`
- **Structured JSON:** [`a106e8eb71747c92e0ee.json`](../../sessions/a1/a106e8eb71747c92e0ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 个实验全部正常运行中，状态汇总：

| 服务器:GPU | exp_id | 进度 | 速度 | ETA (UTC) |
|---|---|---|---|---|
| 10894:0 | reverse_cutoff_s2_v2 | 12893/50005 (26%) | 1.07 it/s | May 27 ~06:30 |
| 10894:1 | full_occ_ln_v2_s0 | 1901/50005 (4%) | 1.08 it/s | May 27 ~09:10 |
| 10894:2 | full_occ_ln_v2_s1 | 1893/50005 (4%) | 1.08 it/s | May 27 ~09:20 |
| 10894:3 | detach_ln_v2_s0 | 1894/50005 (4%) | 1.09 it/s | May 27 ~09:12 |
| 34685:0 | vanilla_v2_s1 | 13621/50005 (27%) | 1.09 it/s | May 27 ~06:11 |
| 34685:1 | vanilla_v2_s2 | 13690/50005 (27%) | 1.09 it/s | May 27 ~06:11 |
| 34685:2 | detach_ln_s3 | 13615/50005 (27%) | 1.09 it/s | May 27 ~06:11 |
| 34685:3 | cutoff_25k_s1_v2 | 12149/50005 (24%) | 1.08 it/s | May 27 ~06:37 |

GPU 状态正常，显存占用均 ~64%。westd-34685 全部 GPU 利用率 96-99%；westd-10894 的 cuda:1 利用率偏低 (55%)，其余正常。

34685 上 vanilla_v2_s1/s2 和 detach_ln_s3 的日志在 `/tmp/` 而非 `~/runs/occsafe_vla/`。10894 上 3 个新实验刚启动约 30 分钟。报告已写入 `artifacts/training_status_20260526.md`。

---
