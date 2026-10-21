# ops check contamination and gpu status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_contamination_and_gpu_status_20260524T205956_result.json`
- **Structured JSON:** [`60e927c4c63f87faec60.json`](../../sessions/60/60e927c4c63f87faec60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

---

## 实验状态汇总

### 1. contamination_20_tau07_seed42 (cuda:1) — **完成 ✓**
- 训练 6103/6103 steps，final checkpoint 已保存
- Eval 结果：

| Eval Set | Loss | PPL |
|----------|------|-----|
| Holdout | 2.853 | 17.35 |
| OWT | 2.893 | 18.06 |
| Wiki | 2.715 | 15.11 |

- Registry 已更新（conclusion: success, metrics 已录入）

### 2. random_subset_epoch_seed42 (cuda:0) — **训练完成，final eval 进行中**
- 训练 6103/6103 steps (100%)，耗时 12:07:38
- 正在跑 final holdout eval：3303/8477 (39%)，ETA ~26 min
- final checkpoint 尚未保存（eval 结束后保存）

### 3. detect_remove_q05_seed42 (cuda:2) — **进行中，41%**
- Step 2522/6103，ETA ~5:43（预计 ~10:45 左右完成）
- **注意**：这是一次从 step 0 开始的全新运行（tmux session 创建于 May 24 23:59），不是从 92% 继续的。之前的运行可能已经失败/被重启。

### 4. GPU 使用情况

| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 (RTX PRO 6000) | 74/98 GB | 83% | random_subset final eval |
| 1 (RTX PRO 6000) | 13/98 GB | 100% | contamination wiki eval (finishing) |
| 2 (RTX PRO 6000) | 74/98 GB | 100% | detect_remove_q05 training |
| 3 (RTX PRO 6000) | 46/98 GB | 99% | detect_remove_q03_seed42 (另一个实验) |

**注意事项**：
- 有 cron 在自动启动 eval 进程，导致产生了多个重复的 wiki eval 进程（已清理）
- detect_remove_q05 的 92% → 41% 落差需要确认原因——可能是之前的运行崩溃后被重新启动

---
