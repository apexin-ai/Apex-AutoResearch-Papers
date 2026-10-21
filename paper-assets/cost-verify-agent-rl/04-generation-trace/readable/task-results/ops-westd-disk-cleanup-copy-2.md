# ops westd disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-cleanup_20260517T181404_result.json`
- **Structured JSON:** [`1dfc27acfc09dae08682.json`](../../sessions/1d/1dfc27acfc09dae08682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整分析：

## 磁盘占用摘要 (250G total, 240G used, 11G free)

| 路径 | 大小 | 说明 |
|------|------|------|
| `/root/autodl-tmp/provenance_weight_training/` | **118G** | 独立项目，61个模型目录，最后修改 May 16 |
| `/root/autodl-tmp/output/` | **26G** | models/(15G, 今天完成的5个实验) + detector_5pct/(5.6G) + detector_10pct/(5.6G, May 14) |
| `/root/autodl-tmp/checkpoints/reinforce_pp_baseline/` | **21G** | **RUNNING** (PID 40267, global_step_5) - 不可删 |
| `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/` | **3.3G** | 旧实验 - 可安全删除 |
| Ray 旧 session (4个) | ~8M | 可忽略 |
| wandb | 45M | 可忽略 |

## 需要你确认的决策

**能释放 118G 的关键问题**：`/root/autodl-tmp/provenance_weight_training/` 是一个完全独立的项目（内含 61 个训练好的 model checkpoint，名字如 `uniform_seed42`, `tau_0.5_seed42`, `adaptive_seed42` 等），不属于 cost-verify-agent-rl。最后修改时间 May 16。

1. **可以删除 `provenance_weight_training/` 整个目录吗？** (释放 118G)
2. **`/root/autodl-tmp/output/`** 中的内容：
   - `detector_5pct/` + `detector_10pct/` (共 11.2G, May 14) — 与 provenance 项目同类，可以删？
   - `models/` 下 5 个今天完成的实验 (15G: `grid_b0_3_seed123`, `batch_adaptive_tau_rho06_seed42`, `bs8_auto_nmin_seed42`, `rho02_adaptive_tau09_seed42`, `random_reweight_v2_seed42`) — 可以删？
3. **`checkpoints/exp021_ragen_sft_v4/`** (3.3G) — 我判断可安全删除，确认？

如果 1+2+3 全部确认，可释放 **~147G**，远超 30GB 目标。

两个 RUNNING 实验进程均正常（PID 40267, 85798 confirmed alive）。等你确认后立即执行清理。

---
