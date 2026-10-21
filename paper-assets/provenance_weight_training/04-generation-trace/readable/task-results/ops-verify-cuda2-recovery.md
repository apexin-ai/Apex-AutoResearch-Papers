# ops verify cuda2 recovery

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_cuda2_recovery_20260515T233944_result.json`
- **Structured JSON:** [`28c5b8a2928821c6079b.json`](../../sessions/28/28c5b8a2928821c6079b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### cuda:2 冲突修复确认

| 项目 | 结果 |
|------|------|
| PID 265617 (grid_b_low_serial) | **已死亡** (ps 返回空) |
| cuda:2 显存 | 46523 MiB / 97887 MiB (~47.5%) — 从 ~93GB 降到 ~46GB |
| contamination_60_ess_only 速度 | **2.12 s/it** — 从 ~4.5s/it 恢复正常 |

### 4 个 contamination_60 实验状态

| GPU | 实验 | PID | 进度 | 速度 | ETA |
|-----|------|-----|------|------|-----|
| cuda:0 | contamination_60_seed42_r2 | 257977 | 2699/6103 (44%) | 2.27 s/it | ~2h09m |
| cuda:1 | contamination_60_uniform_seed42 | 250074 | 3796/6103 (62%) | 2.11 s/it | ~1h21m |
| cuda:2 | contamination_60_ess_only_seed42 | 265017 | 202/6103 (3%) | 2.12 s/it | ~3h28m |
| cuda:3 | contamination_60_grid_b0_5_seed42 | 255781 | 3060/6103 (50%) | 2.11 s/it | ~1h47m |

### 最先空出的 GPU

**cuda:1** (~1h21m 后完成) → 可用于重启 grid_b_low。其次是 cuda:3 (~1h47m)。

4 张卡显存均为 ~46.5GB，利用率 94-99%，全部正常单进程运行。

---
