# ops check sim sweep v5 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-sim-sweep-v5-completion_20260515T053021_result.json`
- **Structured JSON:** [`ff5409117aed98abab4e.json`](../../sessions/ff/ff5409117aed98abab4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果：

**exp_004_sim_sweep_v5 → 异常退出（磁盘满）**

| 类别 | 条件 | 详情 |
|---|---|---|
| 完全成功 (4) | auc0.55_n20, auc0.55_n50, auc0.8_n20, auc0.8_n50 | 10/10 seeds |
| 部分成功 (3) | auc0.55_n100 (7/10), auc0.8_n100 (6/10), auc0.9_n20 (6/10) | 剩余 seed 磁盘满 |
| 全部失败 (2) | auc0.65_n20 (0/10), auc0.65_n50 (0/7) | 全部 `Errno 122` |
| 未启动 (3) | auc0.65_n100, auc0.9_n50, auc0.9_n100 | 进程已死 |

**根因**：CmdStan 临时文件写满根分区 /tmp（根分区 30G 当时 100%，现已回落到 80%），导致后续 MCMC sampling 无法写入 CSV 输出文件。TMPDIR 设的是 `/home/ubuntu/tmp_cmdstan` 但 CmdStan 内部仍使用 /tmp 写部分中间文件。

**总计**：97/120 seeds 已执行，59 成功。需要 v6 用 `--resume` 补完剩余 61 个 seed（含重跑失败的）。

---
