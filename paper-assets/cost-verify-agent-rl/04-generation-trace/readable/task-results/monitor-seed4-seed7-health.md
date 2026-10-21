# monitor seed4 seed7 health

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_seed4_seed7_health_20260521T130137_result.json`
- **Structured JSON:** [`933044c4bb1126618c9d.json`](../../sessions/93/933044c4bb1126618c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是汇总报告。

---

## 训练健康度报告

### Seed 4 (fb1o765g) — bjb1 cuda:0,1 — Step 9/15 进行中

**进程状态**: PID 302056 运行 4h20m，正在 step 9 的 rollout 阶段（GPU 占用 21.8GB/卡，利用率 0%，正常——ALFWorld rollout 是 CPU-bound）

**Checkpoint**: `global_step_5` (21GB)，下一个在 step 10

**磁盘**: `/root/autodl-tmp/` 212G/250G (85%) — 剩余 39G，够用但偏紧

#### response_length 趋势 — 确认膨胀

| Step | train/response_length | response_length/mean | response_length/max |
|------|-----------------------|----------------------|---------------------|
| 1 | 3,798 | (截断) | (截断) |
| 5 | (截断) | 12,330 | 16,380 |
| 7 | 7,547 | 13,774 | 16,377 |

- `train/response_length`（per-response tokens）从 step 1 的 **3,798 → step 7 的 7,547**，接近翻倍
- `response_length/mean`（全 trajectory）从 step 5 的 12,330 → step 7 的 13,774，持续上升
- **response_length/max 已达 16,377**，逼近 max_model_len 限制（response_length config = 1024 per turn, max_model_len = 20,480）
- `response/aborted_ratio` 目前仍为 0.0，但已在边界

#### Val/Train Success Rate

| Step | val success | train success | train pass@8 | val-core/reward/mean@32 |
|------|------------|--------------|-------------|-------------------------|
| 0 | 9.38% | — | — | 0.9375 |
| 5 | **21.88%** | — | — | **2.1875** |
| 7 | — | 12.5% | 56.25% | — |

- Val success 从 9.4% 提升到 21.9%（step 5），有学习效果
- Train success 在 12.5-13.3% 波动，偏低

#### Actor/Critic 指标

| Step | actor/ppo_kl | actor/entropy | critic/score/mean | actor/grad_norm |
|------|-------------|--------------|-------------------|-----------------|
| 1 | -0.000274 | 0.0473 | 1.33 | 0.94 |
| 7 | 0.00497 | 0.0313 | 1.25 | 1.25 |

- KL 非常小，策略未大幅偏离参考
- Entropy 在下降（0.047 → 0.031），策略变得更确定性
- Grad norm 稳定

#### Seed 4 告警
1. **response_length 膨胀已确认**：per-response 从 3.8K→7.5K（~2x），全 trajectory 逼近 context window 上限。如果趋势继续，后续 step 会出现截断/abort
2. train success 没有跟上 response_length 的增长，可能是 reward hacking（生成更长但不更有效的 response）

---

### Seed 7 (p6vwsrfk) — westd cuda:0,1 — Step 1/15 刚完成

**进程状态**: PID 226699 运行 40min，GPU 占用 95.5/97.2GB（97-100% 利用率），正在 step 2 训练阶段

**Step 1 指标**（初始表现比 Seed 4 好很多）：

| 指标 | Seed 7 step 1 | Seed 4 step 1 |
|------|--------------|---------------|
| train/success | **31.25%** | 13.28% |
| train/pass@8 | **87.5%** | 56.25% |
| train/response_length | 1,992 | 3,798 |
| response_length/mean | 10,319 | (截断) |
| critic/score/mean | 3.125 | 1.328 |
| actor/ppo_kl | -0.000230 | -0.000274 |

Seed 7 起步强劲，response_length 也更短。W&B 上 `_step=0`，metrics 尚未同步。

---

### Seed 6 (2bbyvsdr) — westd cuda:2,3 — 已完成

**进程 920749 已退出，EXIT_CODE=0**。成功完成全部 15 步。

最终 val 指标：
- `val-core/unknown/reward/best@32/mean` = **10.0**（完美）
- `val-aux/unknown/reward/best@16/mean` = 9.92
- Checkpoint 已保存至 `global_step_15`
- GPU 已释放（westd cuda:2,3 = 0 MiB）

---

### 异常和注意事项

1. **W&B 数据缺失**：三个 run（fb1o765g, p6vwsrfk, 2bbyvsdr）在 W&B API 上均返回空数据，包括已完成的 Seed 6。所有指标只能从服务器日志提取。可能是 W&B logging 配置问题。
2. **Seed 4 response_length 膨胀是实质性风险**：当前 step 7 的 max 已达 16,377，还剩 8 步训练，趋势若不变将导致 trajectory 截断。
3. **bjb1 磁盘 85%**：当前安全但 step 10 会保存新 checkpoint（~21GB），会升至约 93%。如果保留旧 checkpoint（max_actor_ckpt_to_keep=3），可能需要清理。

---
