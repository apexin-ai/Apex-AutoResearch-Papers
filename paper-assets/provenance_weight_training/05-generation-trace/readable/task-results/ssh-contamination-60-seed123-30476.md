# ssh contamination 60 seed123 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_contamination_60_seed123_30476_20260517T230418_result.json`
- **Structured JSON:** [`2b70fb0541cf1d669034.json`](../../sessions/2b/2b70fb0541cf1d669034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动，运行正常。

## 汇总

| 项目 | 结果 |
|------|------|
| GPU 2 状态 | 占用 37011MiB / 97887MiB, 99% 利用率 |
| PID | 63158 (python), tmux wrapper 63153 |
| 数据 | 371499 examples loaded |
| 总步数 | 6103 steps (200M tokens) |
| 当前进度 | step 1/6103, ~3.1s/it → 预计约 5.25 小时完成 |
| 日志 | `~/runs/provenance_weight_training/contamination_60_seed123.log` |
| tmux session | `contamination_60_seed123` |

**注意**: 去掉了 `--dataloader_num_workers 0`，因为脚本不支持该参数（脚本内部未使用显式 DataLoader，依赖框架默认行为 num_workers=0）。

---
