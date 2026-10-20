# fix exp 004 sim sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_004_sim_sweep_20260515T165922_result.json`
- **Structured JSON:** [`fe403e68612482048128.json`](../../sessions/fe/fe403e68612482048128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就位，v6 正在正常运行。总结：

**诊断结果**：v5 在 73/120 seeds 后因 `/tmp` (tmpfs 3.9GB) 磁盘满失败（Errno 122: Disk quota exceeded）。CmdStanPy MCMC 采样产生的临时文件耗尽了 tmpfs。

**当前状态**：
- **v6 已由并行 worker 启动**（PID 863060，tmux session `exp_004_sim_sweep_v6`）
- `TMPDIR=/home/ubuntu/tmp_cmdstan`（50GB /home 分区），已确认生效
- `--resume` 模式：跳过已成功的 73 seeds，补跑剩余 47 seeds
- `--parallel 2 --chains-parallel 2`
- Registry 已注册为 RUNNING

**需要补跑的条件**：

| 条件 | 缺失 seeds |
|------|-----------|
| auc0.55_n100 | 3 (disk fail) |
| auc0.65_n20 | 10 (全部 disk fail) |
| auc0.65_n50 | 10 (7 disk fail + 3 未跑) |
| auc0.65_n100 | 10 (完全缺失) |
| auc0.8_n100 | 1 |
| auc0.9_n50 | 3 |
| auc0.9_n100 | 10 (全部 disk fail) |

**预估耗时**：按 N=20 ~300s/seed、N=50 ~700s/seed、N=100 ~3400s/seed 估算，47 seeds 约需 10-15 小时。

---
