# ops verify sim sweep v7 local

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-sim-sweep-v7-local_20260516T022742_result.json`
- **Structured JSON:** [`47f90a9d5ca30e0b8812.json`](../../sessions/47/47f90a9d5ca30e0b8812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## sim_sweep_v7 结果

**路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/`

**状态: 仍在运行中 (8/12 条件完成)**

v7 进程活跃（tmux session `exp_004_sim_sweep_v7`，2 个并行 worker + 4 个 CmdStan 采样器线程）。

### 12 条件详情

| 条件 | 成功 seeds | 状态 | 备注 |
|------|-----------|------|------|
| auc0.55_n20 | 10/10 | DONE | |
| auc0.55_n50 | 10/10 | DONE | |
| auc0.55_n100 | 7/10→10/10 | DONE | v7 补完 |
| auc0.65_n20 | **7/10** | **运行中** | seed 7 正在采样，~600s/seed |
| auc0.65_n50 | **0/10** | **待跑** | 文件仍是旧 TMPDIR 错误 |
| auc0.65_n100 | **0/10** | **待跑** | 文件仍是旧 TMPDIR 错误 |
| auc0.8_n20 | 10/10 | DONE | |
| auc0.8_n50 | 10/10 | DONE | |
| auc0.8_n100 | 9/10→10/10 | DONE | v7 补完 |
| auc0.9_n20 | 10/10 | DONE | |
| auc0.9_n50 | 7/10→10/10 | DONE | v7 补完 |
| auc0.9_n100 | **4/10** | **运行中** | seed 4 正在采样，~5000s/seed |

### 关键发现

- **Reviewer 的"12/12 完成"说法不正确** — 实际 8/12 DONE，4 条件未完成
- **之前 Agent 的"5/10"** 可能指的是 v7 启动前只有 5 个条件有 remaining seeds 需要 resume
- **两个 worker 正在处理**: auc0.65_n20（快完成，~30min）和 auc0.9_n100（还要 ~8h）
- **auc0.65_n50 和 auc0.65_n100** 尚未被 v7 重跑（文件时间戳 May 15 17:21 < v7 启动 18:11），排队等前面两个完成
- 项目 checkpoint 记录 `conditions_ok: 9`（与 sweep_summary.json 的 8 条记录矛盾，可能是 checkpoint 更新滞后于文件写入）

### 预计剩余时间

- auc0.65_n20: ~30 min（3 seeds × ~10min）
- auc0.9_n100: ~8-10h（6 seeds × ~80-90min）
- auc0.65_n50: ~3h（10 seeds × ~18min） — 排队中
- auc0.65_n100: ~10h（10 seeds × ~60min） — 排队中
- **总计**: 约 **10-13 小时**（两个 worker 并行）

### 建议

**仍在运行中，不是 success 也不需要补跑** — 等 v7 自然完成即可。如果 auc0.65_n50/n100 的 TMPDIR race 问题在 v7 的隔离修复下仍然失败，那么 9/12（当前 8 + auc0.9_n100 即将完成）对 Claim 1 identifiability 已经足够（checkpoint 已标注 "9/12 sufficient for Claim 1"）。

---
