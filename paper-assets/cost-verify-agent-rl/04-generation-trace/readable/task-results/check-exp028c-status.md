# check exp028c status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_status_20260516T000951_result.json`
- **Structured JSON:** [`45156a548730ab13ba28.json`](../../sessions/45/45156a548730ab13ba28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report.

---

## exp028c_selfguide_recipe — 训练状态报告

### 进程状态
- **PID 824675**: 存活，已运行 2h34m
- **GPU**: cuda:0 96%, cuda:1 95%, 各使用 29GB / 98GB VRAM — 满载运行
- 日志最后输出 07:50:59 +0800（输出缓冲，实际仍在计算）

---

### 已完成 Step Metrics

| Metric | Step 0 (val baseline) | Step 1 (train) | Log-W&B 一致 |
|--------|----------------------|----------------|-------------|
| success | 6.25% | **13.28%** | ✓ |
| pass@8 / pass@1 | pass@1: 6.25% | pass@8: **37.5%** | ✓ |
| action_is_valid | 74.49% | **76.43%** | ✓ |
| kl_loss | — | 0.01280 | ✓ |
| entropy | — | 0.2634 | ✓ |
| grad_norm | — | 16.88 | ✓ |
| pg_loss | — | 0.00828 | ✓ |
| ppo_kl | — | 0.01921 | ✓ |
| pg_clipfrac | — | 4.44% | ✓ |
| critic/score/mean | — | 0.843 | ✓ |
| time_per_step | — | 3252s (~54min) | ✓ |

**Step 1 日志与 W&B 完全一致，交叉验证通过。**

---

### Step 2 验证结论: `still_in_progress`

- 日志和 W&B 均只有 step 0（val）和 step 1（train），**无 step 2 数据**
- W&B `_step: 1` 确认最新已记录 step 为 1
- 日志中 18,267 行 "Skipping non-numeric metric" 警告（07:50:59 +0800）表明 step 2 rollout 已完成，当前正在 compute 阶段（old_log_prob → ref → update_actor）
- **Registry 中 step_2_train success=6.25% 不可信** — 该值与 step_0 val success 完全一致，疑为混淆。step 2 真实 metrics 尚未产出
- 预计 step 2 完成时间：~08:25 +0800（基于 step 1 compute 阶段 ~35min）

---

### 异常信号检查

- **grad_norm 16.88**: 正常（pre-clip 值，clip_grad=1.0 会截断）
- **kl_loss 0.0128**: 健康水位，远低于警戒线
- **entropy 0.2634**: 偏低但 Qwen3 模型典型值
- **pg_clipfrac 4.44%**: 保守更新（lr=1e-6 符合预期）
- **无 collapse / loss spike / gradient explosion 信号**

---

### 进度与 ETA

| 指标 | 值 |
|------|-----|
| 已完成 steps | 1 / 100 (1%) |
| 每 step 耗时 | ~54 min |
| 总预计耗时 | ~90 hours |
| 剩余耗时 | ~89 hours (~3.7 天) |

---
