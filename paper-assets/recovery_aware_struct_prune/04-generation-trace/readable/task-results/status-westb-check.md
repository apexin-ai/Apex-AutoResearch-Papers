# status westb check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westb-check_20260517T101232_result.json`
- **Structured JSON:** [`284091af3f3e33c8a1c9.json`](../../sessions/28/284091af3f3e33c8a1c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 实验状态汇总

### GPU 使用情况

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| cuda:0 | 14.8G / 97.9G | 99% | eval_gradient_postsft (PID 701500) |
| cuda:1 | 12.9G / 97.9G | 78% | eval_postprune_random_20 (PID 696141) |

### tmux sessions (3个)

| Session | 状态 |
|---------|------|
| `eval_gradient_postsft` | 活跃 |
| `scoring_ablation_random` | 活跃 |
| `scoring_ablation_v2` | 活跃（已完成，停在 shell 提示符） |

---

### 实验详情

**1. scoring_ablation_v2 (tmux session)** — **已完成**
- SFT recovery 已完成（epoch=2, train_loss=0.759, 34m44s）
- 模型已保存到 `sft_gradient_20`
- session 停在 shell 提示符，无进程运行

**2. eval_gradient_postsft (cuda:0)** — **运行中 (24%)**
- 评估 `sft_gradient_20` 模型，200 samples
- 进度：48/200，已运行约 2 分钟
- 预计剩余约 6-8 分钟

**3. scoring_ablation_random / eval_postprune_random_20 (cuda:1)** — **运行中 (64%)**
- 评估 `pruned_random_20` 模型，200 samples
- 进度：128/200，中间指标：**acc=0.37** (at 100), eos_rate=47%
- 已运行 1h15m，预计剩余约 40 分钟

**4. scoring_ablation_batch_v2 (cron 报告的)** — 实际就是 `scoring_ablation_v2`，SFT 阶段已完成，后续 eval 拆到了 `eval_gradient_postsft`

---

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 8.6G | 22G | 29% ✓ |
| 数据盘 `/root/autodl-tmp` | 250G | 231G | 20G | **93%** ⚠️ |

数据盘 93% 需要关注，仅剩 20G 可用。

---

### 结论
- 两个 eval 任务正在跑（cuda:0 和 cuda:1 各一个），**无空闲 GPU**
- `eval_gradient_postsft` 预计很快完成（~10 min），`eval_postprune_random_20` 约 40 min 后完成
- 数据盘偏满，后续实验前建议清理旧 checkpoint

---
