# check progress and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_progress_and_eval_20260523T064107_result.json`
- **Structured JSON:** [`2c81d39c274fda93dbbf.json`](../../sessions/2c/2c81d39c274fda93dbbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度更新：
- bs8_nmin4_uniform_seed123_r2: 92% (5618/6103), ~21 min 剩余
- bs8_nmin4_adaptive_seed123_r2: 90% (5515/6103), ~26 min 剩余
- rho03_adaptive_seed456_r2: 82% (5002/6103), ~64 min 剩余（GPU 0 被 eval 占了部分资源，速度变慢了）

3 个 watcher 脚本在后台运行，训练完成后自动启动 eval。先汇报当前已有的结果。

---

**当前状态汇总：**

**训练状态：**

| 实验 | 状态 | step | 预估剩余 |
|------|------|------|----------|
| rho03_uniform_seed456 | **已完成 + eval 完成** | 6103/6103 | - |
| bs8_nmin4_uniform_seed123_r2 | 训练中 (GPU 3) | 5618/6103 | ~21 min |
| bs8_nmin4_adaptive_seed123_r2 | 训练中 (GPU 1) | 5515/6103 | ~26 min |
| rho03_adaptive_seed456_r2 | 训练中 (GPU 0) | 5002/6103 | ~64 min |

**已完成的 eval：**

| 实验 | holdout_ppl | owt_ppl | wiki_ppl |
|------|-------------|---------|----------|
| rho03_uniform_seed456 | 17.419 | 18.109 | 15.168 |

**未完成的实验：** 3 个 watcher 脚本已部署在后台，训练完成后将自动在对应 GPU 上启动 3 个 eval（holdout/owt/wiki）。预估时间：
- bs8_nmin4_uniform_seed123_r2：eval 约 15:20 开始
- bs8_nmin4_adaptive_seed123_r2：eval 约 15:25 开始
- rho03_adaptive_seed456_r2：eval 约 16:05 开始

每组 eval（3 个数据集）约需 10-12 分钟。

---
