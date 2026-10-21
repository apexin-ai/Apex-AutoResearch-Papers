# ssh start 14b eval batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_start-14b-eval-batch_20260519T013459_result.json`
- **Structured JSON:** [`300524bcc49d19468320.json`](../../sessions/30/300524bcc49d19468320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 项目 | 状态 |
|------|------|
| 脚本创建 | `/root/contamcal-irt-calibration/exp001/run_eval_14b_batch.sh` |
| tmux session | `eval_14b_batch` 运行中 |
| GPU 0 占用 | 32735MiB / 97887MiB, 94% util |
| PID | **93852** (`python3.12`) |
| 进度 | d000 MMLU eval 进行中，491/14042 (~3%), ~17 it/s |

按当前速度估算：MMLU 14042 items × 5 doses ≈ 70k items，~17 it/s → 约 68 分钟完成 MMLU 部分，加上 ARC（~1.2k × 5）总计约 75 分钟。

---
