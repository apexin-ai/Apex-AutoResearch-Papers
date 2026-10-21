# fix exp004 sim sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp004_sim_sweep_20260515T165902_result.json`
- **Structured JSON:** [`c4c2cda327de4e720451.json`](../../sessions/c4/c4c2cda327de4e720451.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**诊断结果**：v1-v5 全部因 `/tmp` tmpfs（3.9GB）被 CmdStanPy MCMC 临时文件撑满导致 `[Errno 122] Disk quota exceeded`。

**已有结果**（12 conditions × 10 seeds = 120 runs）：
| 状态 | Conditions |
|------|-----------|
| 完成 (10/10) | auc0.55_n20, auc0.55_n50, auc0.8_n20, auc0.8_n50, auc0.9_n20 |
| 部分完成 | auc0.55_n100 (7/10), auc0.8_n100 (9/10), auc0.9_n50 (7/10) |
| 全部失败 | auc0.65_n20 (0/10), auc0.65_n50 (0/7), auc0.9_n100 (0/10) |
| 缺失 | auc0.65_n100 |

**修复**：`TMPDIR=/home/ubuntu/tmp_cmdstan`（50GB 可用），`--resume` 跳过已完成的 seeds。

**已提交**：tmux session `exp_004_sim_sweep_v6`，`--parallel 2 --chains-parallel 2`，registry 已更新为 RUNNING。需要完成约 47 个 remaining runs。

---
