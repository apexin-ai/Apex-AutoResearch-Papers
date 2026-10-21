# ops gpu0 kill validate cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0-kill-validate-cleanup_20260514T045152_result.json`
- **Structured JSON:** [`3e58cdfd8a3d90ce39da.json`](../../sessions/3e/3e58cdfd8a3d90ce39da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动并正在运行。

---

## 执行结果汇总

| Step | 状态 | 详情 |
|------|------|------|
| **Step 1: Kill GPU0 v6** | ✓ 完成 | PID 36874 已自行结束。额外清理了两个残留进程 (PID 161201, 166392/166399) 和一个游离 tmux 父进程 (PID 544498, `plan-001b-gpu0-v3`)，该进程会反复在 GPU0 启动 router_sft_train |
| **Step 2: 数据验证** | ✓ 干净 | 25 行全部可解析，19 个唯一 episode (0-18)，部分 episode 有 2 个 variation。≥20 条达标 |
| **Step 3: 清理残留** | ✓ 释放 ~8G | 删除 `episodes_full.jsonl.gz` (6.9G, hardlink)、`episodes_full_844k.jsonl.bak` (8.3G)、`recovery_gz_hardlink.gz` (6.9G, 同一 hardlink)。磁盘 80% → 77% (可用 51G → 59G) |
| **Step 4: plan-002 dry-run** | ✓ 运行中 | tmux session `plan002-dryrun`，GPU0 PID 171059 占用 29.8G。batch_size=4 (原 32 OOM)，1163 steps，当前 3% (40/1163)，~1.37 it/s，预计 ~14 分钟完成 |

**注意**: `launch_plan002.sh` 里的 `--batch_size 32` 在此 GPU 上会 OOM，正式训练时需改为 batch_size=4 或 8，或加 gradient_accumulation_steps 补偿有效 batch size。

---
